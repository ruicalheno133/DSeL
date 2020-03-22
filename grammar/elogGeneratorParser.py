# Generated from elogGenerator.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\6")
        buf.write("\5*\n\5\r\5\16\5+\3\6\3\6\3\6\3\6\3\7\3\7\6\7\64\n\7\r")
        buf.write("\7\16\7\65\3\b\3\b\3\b\7\b;\n\b\f\b\16\b>\13\b\3\t\3\t")
        buf.write("\3\t\3\n\7\nD\n\n\f\n\16\nG\13\n\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fV\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\5\ra\n\r\3\r\2\2\16\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\2\2\2`\2\32\3\2\2\2\4\34\3\2\2")
        buf.write("\2\6\"\3\2\2\2\b\'\3\2\2\2\n-\3\2\2\2\f\61\3\2\2\2\16")
        buf.write("\67\3\2\2\2\20?\3\2\2\2\22E\3\2\2\2\24H\3\2\2\2\26U\3")
        buf.write("\2\2\2\30`\3\2\2\2\32\33\5\4\3\2\33\3\3\2\2\2\34\35\7")
        buf.write("\5\2\2\35\36\7\6\2\2\36\37\7\7\2\2\37 \7\23\2\2 !\5\6")
        buf.write("\4\2!\5\3\2\2\2\"#\5\b\5\2#$\5\f\7\2$%\5\22\n\2%&\5\20")
        buf.write("\t\2&\7\3\2\2\2\')\7\b\2\2(*\5\n\6\2)(\3\2\2\2*+\3\2\2")
        buf.write("\2+)\3\2\2\2+,\3\2\2\2,\t\3\2\2\2-.\7\26\2\2./\7\3\2\2")
        buf.write("/\60\7\24\2\2\60\13\3\2\2\2\61\63\7\t\2\2\62\64\5\16\b")
        buf.write("\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2")
        buf.write("\2\2\66\r\3\2\2\2\67<\7\26\2\289\7\4\2\29;\7\26\2\2:8")
        buf.write("\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\17\3\2\2\2><\3")
        buf.write("\2\2\2?@\7\n\2\2@A\7\25\2\2A\21\3\2\2\2BD\5\24\13\2CB")
        buf.write("\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\23\3\2\2\2GE\3")
        buf.write("\2\2\2HI\7\13\2\2IJ\7\26\2\2JK\5\26\f\2K\25\3\2\2\2LM")
        buf.write("\7\f\2\2MV\7\r\2\2NO\7\f\2\2OP\7\17\2\2PV\5\30\r\2QR\7")
        buf.write("\f\2\2RV\7\16\2\2ST\7\f\2\2TV\7\20\2\2UL\3\2\2\2UN\3\2")
        buf.write("\2\2UQ\3\2\2\2US\3\2\2\2V\27\3\2\2\2WX\7\22\2\2Xa\7\25")
        buf.write("\2\2YZ\7\21\2\2Za\7\25\2\2[\\\7\22\2\2\\]\7\25\2\2]^\7")
        buf.write("\21\2\2^a\7\25\2\2_a\3\2\2\2`W\3\2\2\2`Y\3\2\2\2`[\3\2")
        buf.write("\2\2`_\3\2\2\2a\31\3\2\2\2\b+\65<EU`")
        return buf.getvalue()


class elogGeneratorParser ( Parser ):

    grammarFileName = "elogGenerator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'-'", "'GENERATE'", "'LOG'", "'OUTPUT'", 
                     "'ACTIVITIES'", "'TRACES'", "'CASES'", "'COLUMN'", 
                     "'TYPE'", "'String'", "'Number'", "'Int'", "'Timestamp'", 
                     "'MAX'", "'MIN'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "GENERATE", 
                      "LOG", "OUTPUT", "ACTIVITIES", "TRACES", "CASES", 
                      "COLUMN", "TYPE", "STRING_TYPE", "NUMBER_TYPE", "INT_TYPE", 
                      "TIMESTAMP_TYPE", "MAX", "MIN", "FILENAME", "ID", 
                      "INT", "TEXT", "IGNORE" ]

    RULE_s = 0
    RULE_g_type = 1
    RULE_body = 2
    RULE_activities = 3
    RULE_a_mapping = 4
    RULE_traces = 5
    RULE_t_list = 6
    RULE_count = 7
    RULE_columns = 8
    RULE_column = 9
    RULE_c_type = 10
    RULE_int_options = 11

    ruleNames =  [ "s", "g_type", "body", "activities", "a_mapping", "traces", 
                   "t_list", "count", "columns", "column", "c_type", "int_options" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    GENERATE=3
    LOG=4
    OUTPUT=5
    ACTIVITIES=6
    TRACES=7
    CASES=8
    COLUMN=9
    TYPE=10
    STRING_TYPE=11
    NUMBER_TYPE=12
    INT_TYPE=13
    TIMESTAMP_TYPE=14
    MAX=15
    MIN=16
    FILENAME=17
    ID=18
    INT=19
    TEXT=20
    IGNORE=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g_type(self):
            return self.getTypedRuleContext(elogGeneratorParser.G_typeContext,0)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = elogGeneratorParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.g_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class G_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GENERATE(self):
            return self.getToken(elogGeneratorParser.GENERATE, 0)

        def LOG(self):
            return self.getToken(elogGeneratorParser.LOG, 0)

        def OUTPUT(self):
            return self.getToken(elogGeneratorParser.OUTPUT, 0)

        def FILENAME(self):
            return self.getToken(elogGeneratorParser.FILENAME, 0)

        def body(self):
            return self.getTypedRuleContext(elogGeneratorParser.BodyContext,0)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_g_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG_type" ):
                return visitor.visitG_type(self)
            else:
                return visitor.visitChildren(self)




    def g_type(self):

        localctx = elogGeneratorParser.G_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_g_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(elogGeneratorParser.GENERATE)
            self.state = 27
            self.match(elogGeneratorParser.LOG)
            self.state = 28
            self.match(elogGeneratorParser.OUTPUT)
            self.state = 29
            self.match(elogGeneratorParser.FILENAME)
            self.state = 30
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def activities(self):
            return self.getTypedRuleContext(elogGeneratorParser.ActivitiesContext,0)


        def traces(self):
            return self.getTypedRuleContext(elogGeneratorParser.TracesContext,0)


        def columns(self):
            return self.getTypedRuleContext(elogGeneratorParser.ColumnsContext,0)


        def count(self):
            return self.getTypedRuleContext(elogGeneratorParser.CountContext,0)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = elogGeneratorParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.activities()
            self.state = 33
            self.traces()
            self.state = 34
            self.columns()
            self.state = 35
            self.count()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActivitiesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIVITIES(self):
            return self.getToken(elogGeneratorParser.ACTIVITIES, 0)

        def a_mapping(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(elogGeneratorParser.A_mappingContext)
            else:
                return self.getTypedRuleContext(elogGeneratorParser.A_mappingContext,i)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_activities

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActivities" ):
                return visitor.visitActivities(self)
            else:
                return visitor.visitChildren(self)




    def activities(self):

        localctx = elogGeneratorParser.ActivitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_activities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(elogGeneratorParser.ACTIVITIES)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.a_mapping()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==elogGeneratorParser.TEXT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_mappingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(elogGeneratorParser.TEXT, 0)

        def ID(self):
            return self.getToken(elogGeneratorParser.ID, 0)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_a_mapping

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_mapping" ):
                return visitor.visitA_mapping(self)
            else:
                return visitor.visitChildren(self)




    def a_mapping(self):

        localctx = elogGeneratorParser.A_mappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_a_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(elogGeneratorParser.TEXT)
            self.state = 44
            self.match(elogGeneratorParser.T__0)
            self.state = 45
            self.match(elogGeneratorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TracesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRACES(self):
            return self.getToken(elogGeneratorParser.TRACES, 0)

        def t_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(elogGeneratorParser.T_listContext)
            else:
                return self.getTypedRuleContext(elogGeneratorParser.T_listContext,i)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_traces

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTraces" ):
                return visitor.visitTraces(self)
            else:
                return visitor.visitChildren(self)




    def traces(self):

        localctx = elogGeneratorParser.TracesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_traces)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(elogGeneratorParser.TRACES)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.t_list()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==elogGeneratorParser.TEXT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(elogGeneratorParser.TEXT)
            else:
                return self.getToken(elogGeneratorParser.TEXT, i)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_t_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_list" ):
                return visitor.visitT_list(self)
            else:
                return visitor.visitChildren(self)




    def t_list(self):

        localctx = elogGeneratorParser.T_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_t_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(elogGeneratorParser.TEXT)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==elogGeneratorParser.T__1:
                self.state = 54
                self.match(elogGeneratorParser.T__1)
                self.state = 55
                self.match(elogGeneratorParser.TEXT)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASES(self):
            return self.getToken(elogGeneratorParser.CASES, 0)

        def INT(self):
            return self.getToken(elogGeneratorParser.INT, 0)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_count

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCount" ):
                return visitor.visitCount(self)
            else:
                return visitor.visitChildren(self)




    def count(self):

        localctx = elogGeneratorParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_count)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(elogGeneratorParser.CASES)
            self.state = 62
            self.match(elogGeneratorParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(elogGeneratorParser.ColumnContext)
            else:
                return self.getTypedRuleContext(elogGeneratorParser.ColumnContext,i)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_columns

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumns" ):
                return visitor.visitColumns(self)
            else:
                return visitor.visitChildren(self)




    def columns(self):

        localctx = elogGeneratorParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==elogGeneratorParser.COLUMN:
                self.state = 64
                self.column()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLUMN(self):
            return self.getToken(elogGeneratorParser.COLUMN, 0)

        def TEXT(self):
            return self.getToken(elogGeneratorParser.TEXT, 0)

        def c_type(self):
            return self.getTypedRuleContext(elogGeneratorParser.C_typeContext,0)


        def getRuleIndex(self):
            return elogGeneratorParser.RULE_column

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = elogGeneratorParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(elogGeneratorParser.COLUMN)
            self.state = 71
            self.match(elogGeneratorParser.TEXT)
            self.state = 72
            self.c_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class C_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Token

        def TYPE(self):
            return self.getToken(elogGeneratorParser.TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(elogGeneratorParser.STRING_TYPE, 0)

        def int_options(self):
            return self.getTypedRuleContext(elogGeneratorParser.Int_optionsContext,0)


        def INT_TYPE(self):
            return self.getToken(elogGeneratorParser.INT_TYPE, 0)

        def NUMBER_TYPE(self):
            return self.getToken(elogGeneratorParser.NUMBER_TYPE, 0)

        def TIMESTAMP_TYPE(self):
            return self.getToken(elogGeneratorParser.TIMESTAMP_TYPE, 0)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_c_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC_type" ):
                return visitor.visitC_type(self)
            else:
                return visitor.visitChildren(self)




    def c_type(self):

        localctx = elogGeneratorParser.C_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_c_type)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(elogGeneratorParser.TYPE)
                self.state = 75
                localctx.t = self.match(elogGeneratorParser.STRING_TYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(elogGeneratorParser.TYPE)
                self.state = 77
                localctx.t = self.match(elogGeneratorParser.INT_TYPE)
                self.state = 78
                self.int_options()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(elogGeneratorParser.TYPE)
                self.state = 80
                localctx.t = self.match(elogGeneratorParser.NUMBER_TYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.match(elogGeneratorParser.TYPE)
                self.state = 82
                localctx.t = self.match(elogGeneratorParser.TIMESTAMP_TYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_optionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.minv = None # Token
            self.maxv = None # Token

        def MIN(self):
            return self.getToken(elogGeneratorParser.MIN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(elogGeneratorParser.INT)
            else:
                return self.getToken(elogGeneratorParser.INT, i)

        def MAX(self):
            return self.getToken(elogGeneratorParser.MAX, 0)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_int_options

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_options" ):
                return visitor.visitInt_options(self)
            else:
                return visitor.visitChildren(self)




    def int_options(self):

        localctx = elogGeneratorParser.Int_optionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_int_options)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(elogGeneratorParser.MIN)
                self.state = 86
                localctx.minv = self.match(elogGeneratorParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(elogGeneratorParser.MAX)
                self.state = 88
                localctx.maxv = self.match(elogGeneratorParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(elogGeneratorParser.MIN)
                self.state = 90
                localctx.minv = self.match(elogGeneratorParser.INT)
                self.state = 91
                self.match(elogGeneratorParser.MAX)
                self.state = 92
                localctx.maxv = self.match(elogGeneratorParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





