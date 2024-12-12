# Generated from CalculatorML.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,217,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,42,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,82,8,3,10,3,12,3,85,9,3,1,
        4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,1,4,1,4,1,5,1,5,1,5,1,
        5,5,5,102,8,5,10,5,12,5,105,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,117,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,5,8,132,8,8,10,8,12,8,135,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,
        9,143,8,9,10,9,12,9,146,9,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,
        5,11,156,8,11,10,11,12,11,159,9,11,1,11,1,11,1,11,1,11,1,11,1,11,
        5,11,167,8,11,10,11,12,11,170,9,11,1,11,1,11,1,11,1,11,5,11,176,
        8,11,10,11,12,11,179,9,11,1,11,1,11,3,11,183,8,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,197,8,12,1,13,
        1,13,1,13,4,13,202,8,13,11,13,12,13,203,1,14,1,14,1,14,1,14,5,14,
        210,8,14,10,14,12,14,213,9,14,1,14,1,14,1,14,0,1,6,15,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,0,5,1,0,2,3,1,0,4,5,1,0,30,31,2,0,
        30,32,35,35,1,0,20,22,234,0,31,1,0,0,0,2,41,1,0,0,0,4,43,1,0,0,0,
        6,67,1,0,0,0,8,86,1,0,0,0,10,97,1,0,0,0,12,116,1,0,0,0,14,118,1,
        0,0,0,16,123,1,0,0,0,18,138,1,0,0,0,20,149,1,0,0,0,22,182,1,0,0,
        0,24,196,1,0,0,0,26,198,1,0,0,0,28,205,1,0,0,0,30,32,3,2,1,0,31,
        30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,
        0,35,42,3,6,3,0,36,42,3,24,12,0,37,42,3,4,2,0,38,42,3,16,8,0,39,
        42,3,14,7,0,40,42,3,18,9,0,41,35,1,0,0,0,41,36,1,0,0,0,41,37,1,0,
        0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,0,43,44,
        5,28,0,0,44,45,5,1,0,0,45,46,3,6,3,0,46,5,1,0,0,0,47,48,6,3,-1,0,
        48,68,3,4,2,0,49,68,3,12,6,0,50,51,5,6,0,0,51,52,3,6,3,0,52,53,5,
        7,0,0,53,68,1,0,0,0,54,55,3,20,10,0,55,56,5,6,0,0,56,57,3,6,3,0,
        57,58,5,7,0,0,58,68,1,0,0,0,59,68,5,27,0,0,60,68,5,28,0,0,61,68,
        3,28,14,0,62,68,3,8,4,0,63,68,3,14,7,0,64,68,3,18,9,0,65,68,3,16,
        8,0,66,68,3,22,11,0,67,47,1,0,0,0,67,49,1,0,0,0,67,50,1,0,0,0,67,
        54,1,0,0,0,67,59,1,0,0,0,67,60,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,
        0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,83,
        1,0,0,0,69,70,10,15,0,0,70,71,7,0,0,0,71,82,3,6,3,16,72,73,10,14,
        0,0,73,74,7,1,0,0,74,82,3,6,3,15,75,76,10,13,0,0,76,77,7,2,0,0,77,
        82,3,6,3,14,78,79,10,12,0,0,79,80,7,3,0,0,80,82,3,6,3,13,81,69,1,
        0,0,0,81,72,1,0,0,0,81,75,1,0,0,0,81,78,1,0,0,0,82,85,1,0,0,0,83,
        81,1,0,0,0,83,84,1,0,0,0,84,7,1,0,0,0,85,83,1,0,0,0,86,87,5,8,0,
        0,87,92,3,10,5,0,88,89,5,9,0,0,89,91,3,10,5,0,90,88,1,0,0,0,91,94,
        1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,
        95,96,5,10,0,0,96,9,1,0,0,0,97,98,5,8,0,0,98,103,3,6,3,0,99,100,
        5,9,0,0,100,102,3,6,3,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,
        0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,
        10,0,0,107,11,1,0,0,0,108,109,5,11,0,0,109,110,5,6,0,0,110,111,5,
        28,0,0,111,117,5,7,0,0,112,113,5,12,0,0,113,114,5,6,0,0,114,115,
        5,28,0,0,115,117,5,7,0,0,116,108,1,0,0,0,116,112,1,0,0,0,117,13,
        1,0,0,0,118,119,5,13,0,0,119,120,5,6,0,0,120,121,3,6,3,0,121,122,
        5,7,0,0,122,15,1,0,0,0,123,124,5,14,0,0,124,125,5,28,0,0,125,126,
        5,15,0,0,126,127,3,6,3,0,127,128,5,16,0,0,128,129,3,6,3,0,129,133,
        5,17,0,0,130,132,3,2,1,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,
        1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,137,
        5,18,0,0,137,17,1,0,0,0,138,139,5,19,0,0,139,140,3,6,3,0,140,144,
        5,17,0,0,141,143,3,2,1,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,
        1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,
        5,18,0,0,148,19,1,0,0,0,149,150,7,4,0,0,150,21,1,0,0,0,151,152,5,
        23,0,0,152,153,3,6,3,0,153,157,5,17,0,0,154,156,3,2,1,0,155,154,
        1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,160,
        1,0,0,0,159,157,1,0,0,0,160,161,5,18,0,0,161,183,1,0,0,0,162,163,
        5,23,0,0,163,164,3,6,3,0,164,168,5,17,0,0,165,167,3,2,1,0,166,165,
        1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,
        1,0,0,0,170,168,1,0,0,0,171,172,5,18,0,0,172,173,5,24,0,0,173,177,
        5,17,0,0,174,176,3,2,1,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,
        1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,181,
        5,18,0,0,181,183,1,0,0,0,182,151,1,0,0,0,182,162,1,0,0,0,183,23,
        1,0,0,0,184,185,5,25,0,0,185,186,5,28,0,0,186,187,5,6,0,0,187,188,
        3,26,13,0,188,189,5,7,0,0,189,197,1,0,0,0,190,191,5,26,0,0,191,192,
        5,28,0,0,192,193,5,6,0,0,193,194,3,28,14,0,194,195,5,7,0,0,195,197,
        1,0,0,0,196,184,1,0,0,0,196,190,1,0,0,0,197,25,1,0,0,0,198,201,3,
        28,14,0,199,200,5,9,0,0,200,202,3,28,14,0,201,199,1,0,0,0,202,203,
        1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,27,1,0,0,0,205,206,5,
        8,0,0,206,211,3,6,3,0,207,208,5,9,0,0,208,210,3,6,3,0,209,207,1,
        0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,214,1,
        0,0,0,213,211,1,0,0,0,214,215,5,10,0,0,215,29,1,0,0,0,17,33,41,67,
        81,83,92,103,116,133,144,157,168,177,182,196,203,211
    ]

class CalculatorMLParser ( Parser ):

    grammarFileName = "CalculatorML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'['", "','", "']'", "'transpose'", "'inverse'", 
                     "'print'", "'for'", "'in'", "'..'", "'{'", "'}'", "'while'", 
                     "'sin'", "'cos'", "'tan'", "'if'", "'else'", "'train'", 
                     "'predict'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'>'", "'<'", "'=='", "'<='", "'>='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "ID", 
                      "WS", "GT", "LT", "EQ", "LEQ", "GEQ", "NEQ", "MATRIX_OP" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_matrix = 4
    RULE_row = 5
    RULE_matrixOperation = 6
    RULE_printStatement = 7
    RULE_forStatement = 8
    RULE_whileStatement = 9
    RULE_func = 10
    RULE_ifStatement = 11
    RULE_ml_statement = 12
    RULE_ml_params = 13
    RULE_array = 14

    ruleNames =  [ "prog", "statement", "assignment", "expr", "matrix", 
                   "row", "matrixOperation", "printStatement", "forStatement", 
                   "whileStatement", "func", "ifStatement", "ml_statement", 
                   "ml_params", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    NUMBER=27
    ID=28
    WS=29
    GT=30
    LT=31
    EQ=32
    LEQ=33
    GEQ=34
    NEQ=35
    MATRIX_OP=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.StatementContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalculatorMLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 519600448) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def ml_statement(self):
            return self.getTypedRuleContext(CalculatorMLParser.Ml_statementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(CalculatorMLParser.AssignmentContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.ForStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.PrintStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.WhileStatementContext,0)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CalculatorMLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.ml_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.printStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.whileStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculatorMLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CalculatorMLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(CalculatorMLParser.ID)
            self.state = 44
            self.match(CalculatorMLParser.T__0)
            self.state = 45
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MatrixOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrixOperation(self):
            return self.getTypedRuleContext(CalculatorMLParser.MatrixOperationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixOp" ):
                listener.enterMatrixOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixOp" ):
                listener.exitMatrixOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixOp" ):
                return visitor.visitMatrixOp(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculatorMLParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def forStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.ForStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class MatrixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrix(self):
            return self.getTypedRuleContext(CalculatorMLParser.MatrixContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixExpr" ):
                listener.enterMatrixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixExpr" ):
                listener.exitMatrixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixExpr" ):
                return visitor.visitMatrixExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(CalculatorMLParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpr" ):
                listener.enterAssignmentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpr" ):
                listener.exitAssignmentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpr" ):
                return visitor.visitAssignmentExpr(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.WhileStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class FunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(CalculatorMLParser.FuncContext,0)

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.PrintStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class ArrayExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(CalculatorMLParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalculatorMLParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)

        def LT(self):
            return self.getToken(CalculatorMLParser.LT, 0)
        def GT(self):
            return self.getToken(CalculatorMLParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class ComparacionesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)

        def EQ(self):
            return self.getToken(CalculatorMLParser.EQ, 0)
        def NEQ(self):
            return self.getToken(CalculatorMLParser.NEQ, 0)
        def GT(self):
            return self.getToken(CalculatorMLParser.GT, 0)
        def LT(self):
            return self.getToken(CalculatorMLParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparaciones" ):
                listener.enterComparaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparaciones" ):
                listener.exitComparaciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparaciones" ):
                return visitor.visitComparaciones(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(CalculatorMLParser.IfStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorMLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CalculatorMLParser.AssignmentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 48
                self.assignment()
                pass

            elif la_ == 2:
                localctx = CalculatorMLParser.MatrixOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.matrixOperation()
                pass

            elif la_ == 3:
                localctx = CalculatorMLParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(CalculatorMLParser.T__5)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(CalculatorMLParser.T__6)
                pass

            elif la_ == 4:
                localctx = CalculatorMLParser.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.func()
                self.state = 55
                self.match(CalculatorMLParser.T__5)
                self.state = 56
                self.expr(0)
                self.state = 57
                self.match(CalculatorMLParser.T__6)
                pass

            elif la_ == 5:
                localctx = CalculatorMLParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(CalculatorMLParser.NUMBER)
                pass

            elif la_ == 6:
                localctx = CalculatorMLParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(CalculatorMLParser.ID)
                pass

            elif la_ == 7:
                localctx = CalculatorMLParser.ArrayExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.array()
                pass

            elif la_ == 8:
                localctx = CalculatorMLParser.MatrixExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.matrix()
                pass

            elif la_ == 9:
                localctx = CalculatorMLParser.PrintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.printStatement()
                pass

            elif la_ == 10:
                localctx = CalculatorMLParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.whileStatement()
                pass

            elif la_ == 11:
                localctx = CalculatorMLParser.ForContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.forStatement()
                pass

            elif la_ == 12:
                localctx = CalculatorMLParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.ifStatement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorMLParser.MulDivContext(self, CalculatorMLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 70
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorMLParser.AddSubContext(self, CalculatorMLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 73
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = CalculatorMLParser.ComparisonContext(self, CalculatorMLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 76
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = CalculatorMLParser.ComparacionesContext(self, CalculatorMLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 79
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 41875931136) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expr(13)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.RowContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.RowContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix" ):
                return visitor.visitMatrix(self)
            else:
                return visitor.visitChildren(self)




    def matrix(self):

        localctx = CalculatorMLParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(CalculatorMLParser.T__7)
            self.state = 87
            self.row()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 88
                self.match(CalculatorMLParser.T__8)
                self.state = 89
                self.row()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(CalculatorMLParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = CalculatorMLParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(CalculatorMLParser.T__7)
            self.state = 98
            self.expr(0)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 99
                self.match(CalculatorMLParser.T__8)
                self.state = 100
                self.expr(0)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(CalculatorMLParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculatorMLParser.ID, 0)

        def getRuleIndex(self):
            return CalculatorMLParser.RULE_matrixOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixOperation" ):
                listener.enterMatrixOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixOperation" ):
                listener.exitMatrixOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixOperation" ):
                return visitor.visitMatrixOperation(self)
            else:
                return visitor.visitChildren(self)




    def matrixOperation(self):

        localctx = CalculatorMLParser.MatrixOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matrixOperation)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(CalculatorMLParser.T__10)
                self.state = 109
                self.match(CalculatorMLParser.T__5)
                self.state = 110
                self.match(CalculatorMLParser.ID)
                self.state = 111
                self.match(CalculatorMLParser.T__6)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(CalculatorMLParser.T__11)
                self.state = 113
                self.match(CalculatorMLParser.T__5)
                self.state = 114
                self.match(CalculatorMLParser.ID)
                self.state = 115
                self.match(CalculatorMLParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = CalculatorMLParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(CalculatorMLParser.T__12)
            self.state = 119
            self.match(CalculatorMLParser.T__5)
            self.state = 120
            self.expr(0)
            self.state = 121
            self.match(CalculatorMLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculatorMLParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.StatementContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = CalculatorMLParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(CalculatorMLParser.T__13)
            self.state = 124
            self.match(CalculatorMLParser.ID)
            self.state = 125
            self.match(CalculatorMLParser.T__14)
            self.state = 126
            self.expr(0)
            self.state = 127
            self.match(CalculatorMLParser.T__15)
            self.state = 128
            self.expr(0)
            self.state = 129
            self.match(CalculatorMLParser.T__16)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519600448) != 0):
                self.state = 130
                self.statement()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(CalculatorMLParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.StatementContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = CalculatorMLParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(CalculatorMLParser.T__18)
            self.state = 139
            self.expr(0)
            self.state = 140
            self.match(CalculatorMLParser.T__16)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519600448) != 0):
                self.state = 141
                self.statement()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(CalculatorMLParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = CalculatorMLParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculatorMLParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.StatementContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.StatementContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = CalculatorMLParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(CalculatorMLParser.T__22)
                self.state = 152
                self.expr(0)
                self.state = 153
                self.match(CalculatorMLParser.T__16)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519600448) != 0):
                    self.state = 154
                    self.statement()
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 160
                self.match(CalculatorMLParser.T__17)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(CalculatorMLParser.T__22)
                self.state = 163
                self.expr(0)
                self.state = 164
                self.match(CalculatorMLParser.T__16)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519600448) != 0):
                    self.state = 165
                    self.statement()
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 171
                self.match(CalculatorMLParser.T__17)
                self.state = 172
                self.match(CalculatorMLParser.T__23)
                self.state = 173
                self.match(CalculatorMLParser.T__16)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 519600448) != 0):
                    self.state = 174
                    self.statement()
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 180
                self.match(CalculatorMLParser.T__17)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ml_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_ml_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PredictModelContext(Ml_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.Ml_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculatorMLParser.ID, 0)
        def array(self):
            return self.getTypedRuleContext(CalculatorMLParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredictModel" ):
                listener.enterPredictModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredictModel" ):
                listener.exitPredictModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredictModel" ):
                return visitor.visitPredictModel(self)
            else:
                return visitor.visitChildren(self)


    class TrainModelContext(Ml_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorMLParser.Ml_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculatorMLParser.ID, 0)
        def ml_params(self):
            return self.getTypedRuleContext(CalculatorMLParser.Ml_paramsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrainModel" ):
                listener.enterTrainModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrainModel" ):
                listener.exitTrainModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrainModel" ):
                return visitor.visitTrainModel(self)
            else:
                return visitor.visitChildren(self)



    def ml_statement(self):

        localctx = CalculatorMLParser.Ml_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ml_statement)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = CalculatorMLParser.TrainModelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(CalculatorMLParser.T__24)
                self.state = 185
                self.match(CalculatorMLParser.ID)
                self.state = 186
                self.match(CalculatorMLParser.T__5)
                self.state = 187
                self.ml_params()
                self.state = 188
                self.match(CalculatorMLParser.T__6)
                pass
            elif token in [26]:
                localctx = CalculatorMLParser.PredictModelContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(CalculatorMLParser.T__25)
                self.state = 191
                self.match(CalculatorMLParser.ID)
                self.state = 192
                self.match(CalculatorMLParser.T__5)
                self.state = 193
                self.array()
                self.state = 194
                self.match(CalculatorMLParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ml_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ArrayContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ArrayContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_ml_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMl_params" ):
                listener.enterMl_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMl_params" ):
                listener.exitMl_params(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMl_params" ):
                return visitor.visitMl_params(self)
            else:
                return visitor.visitChildren(self)




    def ml_params(self):

        localctx = CalculatorMLParser.Ml_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ml_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.array()
            self.state = 201 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 199
                self.match(CalculatorMLParser.T__8)
                self.state = 200
                self.array()
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorMLParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorMLParser.ExprContext,i)


        def getRuleIndex(self):
            return CalculatorMLParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CalculatorMLParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(CalculatorMLParser.T__7)
            self.state = 206
            self.expr(0)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 207
                self.match(CalculatorMLParser.T__8)
                self.state = 208
                self.expr(0)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(CalculatorMLParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         




