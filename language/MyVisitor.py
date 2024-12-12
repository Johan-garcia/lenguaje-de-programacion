import math
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Ensure an interactive backend for GUI plots
import matplotlib.pyplot as plt
from CalculatorMLVisitor import CalculatorMLVisitor

class MyVisitor(CalculatorMLVisitor):
    def __init__(self):
        self.variables = {}
        self.models = {}

    def print_result(self, operation, result):
        """Método para imprimir resultados de manera consistente."""
        
        # Si el resultado es un array de NumPy
        if isinstance(result, np.ndarray):
            print("Resultado:")
            print(result)
        
        # Si el resultado es una lista (puede ser una lista 1D o 2D)
        elif isinstance(result, list):
            if result and isinstance(result[0], list):  # Matriz (lista de listas)
                print("Resultado:")
                for row in result:
                    print(row)
            else:  # Vector (lista 1D)
                print(f"Resultado: {result}")
        
        # Si el resultado es una variable (buscando en las variables definidas)
        elif result in self.variables:
            print(f"Resultado (variable '{result}'): {self.variables[result]}")
        
        # Si es un valor escalar
        else:
            print(f"Resultado: {result}")
        
        return result
        
        
    def visitPrintStatement(self, ctx):
        """Maneja la instrucción 'print'."""
        try:
            value = self.visit(ctx.expr())  # Evalúa la expresión dentro de los paréntesis
            self.print_result("Impresión", value)  # Llama a print_result para mostrar el resultado
            return value
        except Exception as e:
            self.print_result("Error en 'print'", f"Error: {e}")  # Llama a print_result en caso de error
            return None


    

    def visitProg(self, ctx):
        """Maneja el programa completo"""
        results = []
        for statement in ctx.statement():
            result = self.visit(statement)
            results.append(result)
        return results[-1] if results else None

    def visitStatement(self, ctx):
        """Maneja diferentes tipos de declaraciones"""
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.ml_statement():
            return self.visit(ctx.ml_statement())

    def visitAssignment(self, ctx):
        """Asigna el valor de una variable"""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())  # Evaluar la expresión que asigna el valor
        self.variables[var_name] = value  # Guardar el valor en las variables
        print(f"Asignment: {var_name} = {value}")  # Depuración: Verifica que la asignación sea correcta
        return value

    def visitNumber(self, ctx):
        """Maneja la conversión de tokens numéricos"""
        value = float(ctx.getText())
        return value

    def visitVariable(self, ctx):
        """Maneja variables"""
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise Exception(f"Variable '{var_name}' no definida")
        return self.variables[var_name]

    def visitAddSub(self, ctx):
        """Realiza operaciones de suma y resta para vectores y matrices"""
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        # Convierte a NumPy arrays si son listas anidadas
        left_np = np.array(left) if isinstance(left, list) and isinstance(left[0], (int, float, list)) else left
        right_np = np.array(right) if isinstance(right, list) and isinstance(right[0], (int, float, list)) else right

        # Verifica que las matrices tengan las mismas dimensiones para suma/resta
        if isinstance(left_np, np.ndarray) and isinstance(right_np, np.ndarray):
            if left_np.ndim > 1 and right_np.ndim > 1 and left_np.shape != right_np.shape:
                raise Exception("Las dimensiones de las matrices deben coincidir para suma/resta")

        result = left_np + right_np if ctx.getChild(1).getText() == '+' else left_np - right_np
        
        return self.print_result("Suma/Resta", result.tolist() if isinstance(result, np.ndarray) else result)

    def visitMulDiv(self, ctx):
        """Realiza multiplicación y división para vectores y matrices"""
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        # Convierte a NumPy arrays si son listas anidadas
        left_np = np.array(left) if isinstance(left, list) and isinstance(left[0], (int, float, list)) else left
        right_np = np.array(right) if isinstance(right, list) and isinstance(right[0], (int, float, list)) else right

        # Multiplicación de matrices o escalar
        if isinstance(left_np, np.ndarray) and isinstance(right_np, np.ndarray) and left_np.ndim > 1 and right_np.ndim > 1:
            result = np.dot(left_np, right_np)  # Multiplicación de matrices
        else:
            result = left_np * right_np if ctx.getChild(1).getText() == '*' else left_np / right_np

        return self.print_result("Multiplicación/División", result.tolist() if isinstance(result, np.ndarray) else result)

    def visitParens(self, ctx):
        """Maneja expresiones entre paréntesis"""
        return self.visit(ctx.expr())

    def visitForStatement(self, ctx):
        """Maneja el bucle 'for'."""
        var_name = ctx.ID().getText()  # Nombre de la variable de iteración
        start = int(self.visit(ctx.expr(0)))  # Valor inicial del rango
        end = int(self.visit(ctx.expr(1)))    # Valor final del rango

        # Iterar sobre el rango especificado
        for i in range(start, end + 1):
            self.variables[var_name] = i  # Define la variable de iteración
            for stmt in ctx.statement():
                result = self.visit(stmt)  # Evalúa la instrucción dentro del bucle
               

        del self.variables[var_name]  # Limpia la variable de iteración después del bucle
        return None

    def visitWhileStatement(self, ctx):
        """Maneja el bucle 'while'."""
        
        # Evaluar la condición del while
        condition = self.visit(ctx.expr())  # La condición se evalúa al principio

        # Continuar ejecutando el bucle mientras la condición sea verdadera
        while condition:
            for stmt in ctx.statement():  # Ejecuta cada instrucción dentro del bloque
                result = self.visit(stmt)  # Ejecutamos la declaración dentro del while
                if result is not None:
                    self.print_result("Iteración while", result)

            # Reevaluar la condición después de cada iteración
            condition = self.visit(ctx.expr())  # Evaluamos nuevamente la condición
        
        return None


    def visitIfStatement(self, ctx):
        """Maneja el condicional 'if'."""
        
        # Evaluar la condición completa dentro del 'if'
        condition = self.visit(ctx.expr())  # Evaluamos la condición completa

        # Depuración: Verifica qué valor tiene la condición
        print(f"Evaluación de la condición: {condition}")  # Verifica el valor de la condición
        print(f"Tipo de la condición: {type(condition)}")  # Verifica el tipo de la condición
        
        # Verificamos si la condición es un número
        if isinstance(condition, (int, float)):
            print(f"Condición de tipo número: {condition}")  # Depuración para verificar el tipo de condición
        
        # Evaluamos la condición: Si es verdadera, ejecutamos el bloque
        if condition:
            print("Condición verdadera, ejecutando el bloque de instrucciones.")
            for stmt in ctx.statement():  # Ejecuta cada instrucción dentro del bloque del if
                self.visit(stmt)
        else:
            print("Condición falsa, no se ejecuta el bloque de instrucciones.")
        
        return None


    def visitFunction(self, ctx):
        """Maneja funciones trigonométricas y genera su gráfica"""
        func = ctx.func().getText()
        arg = self.visit(ctx.expr())
        
        # Convertir el argumento a radianes si es necesario
        arg_rad = math.radians(arg) if isinstance(arg, (int, float)) else arg
        
        # Calcular el resultado de la función trigonométrica
        result = None
        if func == "sin":
            result = math.sin(arg_rad)
        elif func == "cos":
            result = math.cos(arg_rad)
        elif func == "tan":
            result = math.tan(arg_rad)
        
        # Imprimir el resultado
        self.print_result(f"Función {func}", result)

        # Generar y mostrar la gráfica de la función
        self.plot_trig_function(func)

        return result

    def plot_trig_function(self, func):
        """Genera la gráfica para la función trigonométrica"""
        x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # Valores de x de -2π a 2π
        y_vals = []

        # Calcular los valores de la función trigonométrica
        for x in x_vals:
            if func == "sin":
                y_vals.append(np.sin(x))
            elif func == "cos":
                y_vals.append(np.cos(x))
            elif func == "tan":
                y_vals.append(np.tan(x))

        # Crear la gráfica
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'función {func}')
        plt.title(f'Gráfica de {func}(x)')
        plt.xlabel('x (radianes)')
        plt.ylabel(f'{func}(x)')
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.grid(True)
        plt.legend(loc="upper right")

        # Mostrar la gráfica
        plt.show()



    def visitArray(self, ctx):
        """Convierte una expresión de array a una lista"""
        array = [self.visit(expr) for expr in ctx.expr()]
        return array

    def visitMatrix(self, ctx):
        """Convierte una matriz de la gramática a un NumPy array"""
        rows = [self.visit(row) for row in ctx.row()]
        matrix = np.array(rows)
        return matrix

    def visitRow(self, ctx):
        """Convierte una fila de la gramática a una lista de expresiones"""
        return [self.visit(expr) for expr in ctx.expr()]

    def visitMatrixOperation(self, ctx):
        """Maneja operaciones de matrices como transpuesta e inversa"""
        operation = ctx.getChild(0).getText()  # 'transpose' o 'inverse'
        matrix_name = ctx.ID().getText()       # Nombre de la matriz
        
        # Verifica si la matriz existe
        if matrix_name not in self.variables:
            raise Exception(f"Matriz no definida: {matrix_name}")
        
        matrix = self.variables[matrix_name]
        
        # Verifica que sea una matriz válida (de tipo numpy.ndarray)
        if not isinstance(matrix, np.ndarray) and not (isinstance(matrix, list) and isinstance(matrix[0], list)):
            raise Exception(f"El valor de {matrix_name} no es una matriz válida")
        
        # Convierte a NumPy array si es una lista de listas
        matrix = np.array(matrix) if isinstance(matrix, list) else matrix
        
        # Transposición
        if operation == 'transpose':
            result = np.transpose(matrix)
        # Inversa
        elif operation == 'inverse':
            if np.linalg.det(matrix) == 0:
                raise Exception(f"La matriz {matrix_name} no es invertible")
            result = np.linalg.inv(matrix)
        else:
            # Operación no reconocida
            raise Exception(f"Operación desconocida para matrices: {operation}")
        
        return self.print_result(operation, result)

    def visitTrainModel(self, ctx):
        """Entrena diferentes tipos de modelos de machine learning"""
        model_name = ctx.ID().getText()
        params = [self.visit(array) for array in ctx.ml_params().array()]

        # Guarda el modelo en el diccionario de variables
        if len(params) < 2:
            raise Exception("El entrenamiento requiere al menos características y etiquetas.")
        
        print(f"Entrenando modelo: {model_name}")
        
        if model_name.startswith("linear"):
            model = self.train_linear_regression(params[0], params[1])
            self.variables[model_name] = model
            self.plot_linear_regression(params[0], params[1], model)
        elif model_name.startswith("kmeans"):
            model = self.train_kmeans(params[0], int(params[1][0]))
            self.variables[model_name] = model
            self.plot_kmeans(params[0], model)
        elif model_name.startswith("mlp"):
            model = self.train_mlp(params[0], params[1])
            self.variables[model_name] = model
            self.plot_mlp(params[0], params[1], model)

        return model

    def train_linear_regression(self, features, labels):
        """Implementación simple de regresión lineal"""
        n = len(features)
        mean_x = sum(features) / n
        mean_y = sum(labels) / n

        numerator = sum((features[i] - mean_x) * (labels[i] - mean_y) for i in range(n))
        denominator = sum((features[i] - mean_x) ** 2 for i in range(n))
        slope = numerator / denominator
        intercept = mean_y - slope * mean_x
        
        print(f"Regresión Lineal: pendiente = {slope}, intercepto = {intercept}")
        return {"type": "linear_regression", "slope": slope, "intercept": intercept}

    def plot_linear_regression(self, features, labels, model):
        """Grafica los resultados de la regresión lineal"""
        print("Graficando regresión lineal...")
        slope = model["slope"]
        intercept = model["intercept"]
        predictions = [slope * x + intercept for x in features]

        plt.figure(figsize=(8, 6))
        plt.scatter(features, labels, color='blue', label='Puntos de Datos')
        plt.plot(features, predictions, color='red', label='Línea de Regresión')
        plt.xlabel('Características')
        plt.ylabel('Etiquetas')
        plt.title('Regresión Lineal')
        plt.legend()
        plt.show()
        plt.close()

    def train_kmeans(self, data, k):
        """Implementación simple de K-Means Clustering"""
        centroids = random.sample(data, k)
        print(f"Centroides iniciales: {centroids}")
        
        for _ in range(10):
            clusters = {i: [] for i in range(k)}
            for point in data:
                distances = [math.dist(point, centroid) for centroid in centroids]
                cluster_idx = distances.index(min(distances))
                clusters[cluster_idx].append(point)
            
            centroids = [self.calculate_mean(cluster) for cluster in clusters.values() if cluster]
            print(f"Centroides actualizados: {centroids}")
        
        return {"type": "kmeans", "centroids": centroids, "clusters": clusters}

    def plot_kmeans(self, data, model):
        """Grafica los resultados de K-Means"""
        print("Graficando K-means...")
        clusters = model["clusters"]
        centroids = model["centroids"]

        plt.figure(figsize=(8, 6))
        colors = ['red', 'blue', 'green', 'orange', 'purple']
        for idx, cluster in clusters.items():
            points = list(zip(*cluster))
            plt.scatter(points[0], points[1], color=colors[idx % len(colors)], label=f'Cluster {idx}')
        
        centroid_points = list(zip(*centroids))
        plt.scatter(centroid_points[0], centroid_points[1], color='black', marker='x', s=100, label='Centroides')
        plt.title('Clustering K-means')
        plt.legend()
        plt.show()
        plt.close()

    def calculate_mean(self, cluster):
        """Calcula el centroide de un cluster"""
        return [sum(dim) / len(cluster) for dim in zip(*cluster)]

    def train_mlp(self, inputs, outputs):
        """Implementación simple de Perceptrón Multicapa"""
        print("Entrenando MLP...")
        weights = [random.random() for _ in range(len(inputs[0]))]
        bias = random.random()
        lr = 0.01

        for epoch in range(1000):
            if epoch % 100 == 0:
                print(f"Época {epoch}: pesos = {weights}, sesgo = {bias}")
            
            for i, x in enumerate(inputs):
                y_pred = sum(w * xi for w, xi in zip(weights, x)) + bias
                error = outputs[i] - y_pred
                weights = [w + lr * error * xi for w, xi in zip(weights, x)]
                bias += lr * error
        
        print(f"MLP entrenado: pesos = {weights}, sesgo = {bias}")
        return {"type": "mlp", "weights": weights, "bias": bias}

    def plot_mlp(self, inputs, outputs, model):
        """Grafica los resultados del Perceptrón Multicapa"""
        print("Graficando MLP...")
        predictions = [sum(w * xi for w, xi in zip(model["weights"], x)) + model["bias"] for x in inputs]

        plt.figure(figsize=(8, 6))
        plt.scatter(range(len(outputs)), outputs, color='blue', label='Salidas Reales')
        plt.scatter(range(len(predictions)), predictions, color='red', marker='x', label='Predicciones')
        plt.xlabel('Índice de Muestra')
        plt.ylabel('Salida')
        plt.title('Predicciones MLP vs Salidas Reales')
        plt.legend()
        plt.show()
        plt.close()
