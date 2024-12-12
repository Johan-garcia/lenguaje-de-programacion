# Generated from CalculatorML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorMLParser import CalculatorMLParser
else:
    from CalculatorMLParser import CalculatorMLParser

# This class defines a complete listener for a parse tree produced by CalculatorMLParser.
class CalculatorMLListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorMLParser#prog.
    def enterProg(self, ctx:CalculatorMLParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#prog.
    def exitProg(self, ctx:CalculatorMLParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#statement.
    def enterStatement(self, ctx:CalculatorMLParser.StatementContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#statement.
    def exitStatement(self, ctx:CalculatorMLParser.StatementContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#assignment.
    def enterAssignment(self, ctx:CalculatorMLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#assignment.
    def exitAssignment(self, ctx:CalculatorMLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#MatrixOp.
    def enterMatrixOp(self, ctx:CalculatorMLParser.MatrixOpContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#MatrixOp.
    def exitMatrixOp(self, ctx:CalculatorMLParser.MatrixOpContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Variable.
    def enterVariable(self, ctx:CalculatorMLParser.VariableContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Variable.
    def exitVariable(self, ctx:CalculatorMLParser.VariableContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#MulDiv.
    def enterMulDiv(self, ctx:CalculatorMLParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#MulDiv.
    def exitMulDiv(self, ctx:CalculatorMLParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#AddSub.
    def enterAddSub(self, ctx:CalculatorMLParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#AddSub.
    def exitAddSub(self, ctx:CalculatorMLParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Parens.
    def enterParens(self, ctx:CalculatorMLParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Parens.
    def exitParens(self, ctx:CalculatorMLParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#For.
    def enterFor(self, ctx:CalculatorMLParser.ForContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#For.
    def exitFor(self, ctx:CalculatorMLParser.ForContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#MatrixExpr.
    def enterMatrixExpr(self, ctx:CalculatorMLParser.MatrixExprContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#MatrixExpr.
    def exitMatrixExpr(self, ctx:CalculatorMLParser.MatrixExprContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#AssignmentExpr.
    def enterAssignmentExpr(self, ctx:CalculatorMLParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#AssignmentExpr.
    def exitAssignmentExpr(self, ctx:CalculatorMLParser.AssignmentExprContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#While.
    def enterWhile(self, ctx:CalculatorMLParser.WhileContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#While.
    def exitWhile(self, ctx:CalculatorMLParser.WhileContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Function.
    def enterFunction(self, ctx:CalculatorMLParser.FunctionContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Function.
    def exitFunction(self, ctx:CalculatorMLParser.FunctionContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Print.
    def enterPrint(self, ctx:CalculatorMLParser.PrintContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Print.
    def exitPrint(self, ctx:CalculatorMLParser.PrintContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#ArrayExpr.
    def enterArrayExpr(self, ctx:CalculatorMLParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#ArrayExpr.
    def exitArrayExpr(self, ctx:CalculatorMLParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Number.
    def enterNumber(self, ctx:CalculatorMLParser.NumberContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Number.
    def exitNumber(self, ctx:CalculatorMLParser.NumberContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Comparison.
    def enterComparison(self, ctx:CalculatorMLParser.ComparisonContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Comparison.
    def exitComparison(self, ctx:CalculatorMLParser.ComparisonContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#Comparaciones.
    def enterComparaciones(self, ctx:CalculatorMLParser.ComparacionesContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#Comparaciones.
    def exitComparaciones(self, ctx:CalculatorMLParser.ComparacionesContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#If.
    def enterIf(self, ctx:CalculatorMLParser.IfContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#If.
    def exitIf(self, ctx:CalculatorMLParser.IfContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#matrix.
    def enterMatrix(self, ctx:CalculatorMLParser.MatrixContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#matrix.
    def exitMatrix(self, ctx:CalculatorMLParser.MatrixContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#row.
    def enterRow(self, ctx:CalculatorMLParser.RowContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#row.
    def exitRow(self, ctx:CalculatorMLParser.RowContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#matrixOperation.
    def enterMatrixOperation(self, ctx:CalculatorMLParser.MatrixOperationContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#matrixOperation.
    def exitMatrixOperation(self, ctx:CalculatorMLParser.MatrixOperationContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#printStatement.
    def enterPrintStatement(self, ctx:CalculatorMLParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#printStatement.
    def exitPrintStatement(self, ctx:CalculatorMLParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#forStatement.
    def enterForStatement(self, ctx:CalculatorMLParser.ForStatementContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#forStatement.
    def exitForStatement(self, ctx:CalculatorMLParser.ForStatementContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#whileStatement.
    def enterWhileStatement(self, ctx:CalculatorMLParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#whileStatement.
    def exitWhileStatement(self, ctx:CalculatorMLParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#func.
    def enterFunc(self, ctx:CalculatorMLParser.FuncContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#func.
    def exitFunc(self, ctx:CalculatorMLParser.FuncContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#ifStatement.
    def enterIfStatement(self, ctx:CalculatorMLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#ifStatement.
    def exitIfStatement(self, ctx:CalculatorMLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#TrainModel.
    def enterTrainModel(self, ctx:CalculatorMLParser.TrainModelContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#TrainModel.
    def exitTrainModel(self, ctx:CalculatorMLParser.TrainModelContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#PredictModel.
    def enterPredictModel(self, ctx:CalculatorMLParser.PredictModelContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#PredictModel.
    def exitPredictModel(self, ctx:CalculatorMLParser.PredictModelContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#ml_params.
    def enterMl_params(self, ctx:CalculatorMLParser.Ml_paramsContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#ml_params.
    def exitMl_params(self, ctx:CalculatorMLParser.Ml_paramsContext):
        pass


    # Enter a parse tree produced by CalculatorMLParser#array.
    def enterArray(self, ctx:CalculatorMLParser.ArrayContext):
        pass

    # Exit a parse tree produced by CalculatorMLParser#array.
    def exitArray(self, ctx:CalculatorMLParser.ArrayContext):
        pass



del CalculatorMLParser