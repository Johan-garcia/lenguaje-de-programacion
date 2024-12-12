from antlr4 import *
from CalculatorMLLexer import CalculatorMLLexer
from CalculatorMLParser import CalculatorMLParser
from MyVisitor import MyVisitor

def main():
    # Inicializar el visitor fuera del bucle para mantener el estado
    visitor = MyVisitor()

    print("Bienvenido a CalculatorML - Un lenguaje para Machine Learning")
    print("Escribe 'exit' para salir")
    
    while True:
        # Entrada por consola
        try:
            code = input("CalculatorML> ")
            
            # Salir del programa
            if code.lower() == 'exit':
                print("Saliendo de CalculatorML...")
                break
            
            # Crear flujo de entrada y lexer
            input_stream = InputStream(code)
            lexer = CalculatorMLLexer(input_stream)
            stream = CommonTokenStream(lexer)

            # Analizar la entrada
            parser = CalculatorMLParser(stream)
            tree = parser.prog()

            # Visitar el árbol
            result = visitor.visit(tree)
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
