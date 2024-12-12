# Generated from CalculatorML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorMLParser import CalculatorMLParser
else:
    from CalculatorMLParser import CalculatorMLParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorMLParser.

class CalculatorMLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorMLParser#prog.
    def visitProg(self, ctx:CalculatorMLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#statement.
    def visitStatement(self, ctx:CalculatorMLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#assignment.
    def visitAssignment(self, ctx:CalculatorMLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#MatrixOp.
    def visitMatrixOp(self, ctx:CalculatorMLParser.MatrixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Variable.
    def visitVariable(self, ctx:CalculatorMLParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#MulDiv.
    def visitMulDiv(self, ctx:CalculatorMLParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#AddSub.
    def visitAddSub(self, ctx:CalculatorMLParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Parens.
    def visitParens(self, ctx:CalculatorMLParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#For.
    def visitFor(self, ctx:CalculatorMLParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#MatrixExpr.
    def visitMatrixExpr(self, ctx:CalculatorMLParser.MatrixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#AssignmentExpr.
    def visitAssignmentExpr(self, ctx:CalculatorMLParser.AssignmentExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#While.
    def visitWhile(self, ctx:CalculatorMLParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Function.
    def visitFunction(self, ctx:CalculatorMLParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Print.
    def visitPrint(self, ctx:CalculatorMLParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#ArrayExpr.
    def visitArrayExpr(self, ctx:CalculatorMLParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Number.
    def visitNumber(self, ctx:CalculatorMLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Comparison.
    def visitComparison(self, ctx:CalculatorMLParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#Comparaciones.
    def visitComparaciones(self, ctx:CalculatorMLParser.ComparacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#If.
    def visitIf(self, ctx:CalculatorMLParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#matrix.
    def visitMatrix(self, ctx:CalculatorMLParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#row.
    def visitRow(self, ctx:CalculatorMLParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#matrixOperation.
    def visitMatrixOperation(self, ctx:CalculatorMLParser.MatrixOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#printStatement.
    def visitPrintStatement(self, ctx:CalculatorMLParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#forStatement.
    def visitForStatement(self, ctx:CalculatorMLParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#whileStatement.
    def visitWhileStatement(self, ctx:CalculatorMLParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#func.
    def visitFunc(self, ctx:CalculatorMLParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#ifStatement.
    def visitIfStatement(self, ctx:CalculatorMLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#TrainModel.
    def visitTrainModel(self, ctx:CalculatorMLParser.TrainModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#PredictModel.
    def visitPredictModel(self, ctx:CalculatorMLParser.PredictModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#ml_params.
    def visitMl_params(self, ctx:CalculatorMLParser.Ml_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorMLParser#array.
    def visitArray(self, ctx:CalculatorMLParser.ArrayContext):
        return self.visitChildren(ctx)



del CalculatorMLParser