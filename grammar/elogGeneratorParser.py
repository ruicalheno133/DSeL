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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("s\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\6\5,\n\5\r\5\16\5-\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\6\7\66\n\7\r\7\16\7\67\3\b\3\b\3\b\7\b=\n\b\f\b\16\b")
        buf.write("@\13\b\3\t\3\t\3\t\3\n\7\nF\n\n\f\n\16\nI\13\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\fT\n\f\f\f\16\fW\13")
        buf.write("\f\3\f\3\f\3\f\7\f\\\n\f\f\f\16\f_\13\f\3\f\3\f\5\fc\n")
        buf.write("\f\3\r\3\r\3\r\3\r\5\ri\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16q\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\2\2\2q\2\34\3\2\2\2\4\36\3\2\2\2\6$\3\2\2\2\b)")
        buf.write("\3\2\2\2\n/\3\2\2\2\f\63\3\2\2\2\169\3\2\2\2\20A\3\2\2")
        buf.write("\2\22G\3\2\2\2\24J\3\2\2\2\26b\3\2\2\2\30h\3\2\2\2\32")
        buf.write("p\3\2\2\2\34\35\5\4\3\2\35\3\3\2\2\2\36\37\7\5\2\2\37")
        buf.write(" \7\6\2\2 !\7\7\2\2!\"\7\24\2\2\"#\5\6\4\2#\5\3\2\2\2")
        buf.write("$%\5\b\5\2%&\5\f\7\2&\'\5\22\n\2\'(\5\20\t\2(\7\3\2\2")
        buf.write("\2)+\7\b\2\2*,\5\n\6\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-")
        buf.write(".\3\2\2\2.\t\3\2\2\2/\60\7\30\2\2\60\61\7\3\2\2\61\62")
        buf.write("\7\25\2\2\62\13\3\2\2\2\63\65\7\t\2\2\64\66\5\16\b\2\65")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\r")
        buf.write("\3\2\2\29>\7\30\2\2:;\7\4\2\2;=\7\30\2\2<:\3\2\2\2=@\3")
        buf.write("\2\2\2><\3\2\2\2>?\3\2\2\2?\17\3\2\2\2@>\3\2\2\2AB\7\n")
        buf.write("\2\2BC\7\27\2\2C\21\3\2\2\2DF\5\24\13\2ED\3\2\2\2FI\3")
        buf.write("\2\2\2GE\3\2\2\2GH\3\2\2\2H\23\3\2\2\2IG\3\2\2\2JK\7\13")
        buf.write("\2\2KL\7\30\2\2LM\5\26\f\2M\25\3\2\2\2NO\7\f\2\2Oc\7\r")
        buf.write("\2\2PQ\7\f\2\2QU\7\17\2\2RT\5\30\r\2SR\3\2\2\2TW\3\2\2")
        buf.write("\2US\3\2\2\2UV\3\2\2\2Vc\3\2\2\2WU\3\2\2\2XY\7\f\2\2Y")
        buf.write("]\7\16\2\2Z\\\5\32\16\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2")
        buf.write("]^\3\2\2\2^c\3\2\2\2_]\3\2\2\2`a\7\f\2\2ac\7\20\2\2bN")
        buf.write("\3\2\2\2bP\3\2\2\2bX\3\2\2\2b`\3\2\2\2c\27\3\2\2\2de\7")
        buf.write("\22\2\2ei\7\27\2\2fg\7\21\2\2gi\7\27\2\2hd\3\2\2\2hf\3")
        buf.write("\2\2\2i\31\3\2\2\2jk\7\22\2\2kq\7\26\2\2lm\7\21\2\2mq")
        buf.write("\7\26\2\2no\7\23\2\2oq\7\27\2\2pj\3\2\2\2pl\3\2\2\2pn")
        buf.write("\3\2\2\2q\33\3\2\2\2\13-\67>GU]bhp")
        return buf.getvalue()


class elogGeneratorParser ( Parser ):

    grammarFileName = "elogGenerator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'-'", "'GENERATE'", "'LOG'", "'OUTPUT'", 
                     "'ACTIVITIES'", "'TRACES'", "'CASES'", "'COLUMN'", 
                     "'TYPE'", "'String'", "'Number'", "'Int'", "'Timestamp'", 
                     "'MAX'", "'MIN'", "'DEC_CASES'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "GENERATE", 
                      "LOG", "OUTPUT", "ACTIVITIES", "TRACES", "CASES", 
                      "COLUMN", "TYPE", "STRING_TYPE", "NUMBER_TYPE", "INT_TYPE", 
                      "TIMESTAMP_TYPE", "MAX", "MIN", "DEC_CASES", "FILENAME", 
                      "ID", "DECIMAL", "INT", "TEXT", "IGNORE" ]

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
    RULE_int_option = 11
    RULE_dec_option = 12

    ruleNames =  [ "s", "g_type", "body", "activities", "a_mapping", "traces", 
                   "t_list", "count", "columns", "column", "c_type", "int_option", 
                   "dec_option" ]

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
    DEC_CASES=17
    FILENAME=18
    ID=19
    DECIMAL=20
    INT=21
    TEXT=22
    IGNORE=23

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
            self.state = 26
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
            self.state = 28
            self.match(elogGeneratorParser.GENERATE)
            self.state = 29
            self.match(elogGeneratorParser.LOG)
            self.state = 30
            self.match(elogGeneratorParser.OUTPUT)
            self.state = 31
            self.match(elogGeneratorParser.FILENAME)
            self.state = 32
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
            self.state = 34
            self.activities()
            self.state = 35
            self.traces()
            self.state = 36
            self.columns()
            self.state = 37
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
            self.state = 39
            self.match(elogGeneratorParser.ACTIVITIES)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.a_mapping()
                self.state = 43 
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
            self.state = 45
            self.match(elogGeneratorParser.TEXT)
            self.state = 46
            self.match(elogGeneratorParser.T__0)
            self.state = 47
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
            self.state = 49
            self.match(elogGeneratorParser.TRACES)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.t_list()
                self.state = 53 
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
            self.state = 55
            self.match(elogGeneratorParser.TEXT)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==elogGeneratorParser.T__1:
                self.state = 56
                self.match(elogGeneratorParser.T__1)
                self.state = 57
                self.match(elogGeneratorParser.TEXT)
                self.state = 62
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
            self.state = 63
            self.match(elogGeneratorParser.CASES)
            self.state = 64
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
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==elogGeneratorParser.COLUMN:
                self.state = 66
                self.column()
                self.state = 71
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
            self.state = 72
            self.match(elogGeneratorParser.COLUMN)
            self.state = 73
            self.match(elogGeneratorParser.TEXT)
            self.state = 74
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

        def INT_TYPE(self):
            return self.getToken(elogGeneratorParser.INT_TYPE, 0)

        def int_option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(elogGeneratorParser.Int_optionContext)
            else:
                return self.getTypedRuleContext(elogGeneratorParser.Int_optionContext,i)


        def NUMBER_TYPE(self):
            return self.getToken(elogGeneratorParser.NUMBER_TYPE, 0)

        def dec_option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(elogGeneratorParser.Dec_optionContext)
            else:
                return self.getTypedRuleContext(elogGeneratorParser.Dec_optionContext,i)


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
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(elogGeneratorParser.TYPE)
                self.state = 77
                localctx.t = self.match(elogGeneratorParser.STRING_TYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(elogGeneratorParser.TYPE)
                self.state = 79
                localctx.t = self.match(elogGeneratorParser.INT_TYPE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==elogGeneratorParser.MAX or _la==elogGeneratorParser.MIN:
                    self.state = 80
                    self.int_option()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(elogGeneratorParser.TYPE)
                self.state = 87
                localctx.t = self.match(elogGeneratorParser.NUMBER_TYPE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << elogGeneratorParser.MAX) | (1 << elogGeneratorParser.MIN) | (1 << elogGeneratorParser.DEC_CASES))) != 0):
                    self.state = 88
                    self.dec_option()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.match(elogGeneratorParser.TYPE)
                self.state = 95
                localctx.t = self.match(elogGeneratorParser.TIMESTAMP_TYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_optionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.opt_name = None # Token
            self.opt_value = None # Token

        def MIN(self):
            return self.getToken(elogGeneratorParser.MIN, 0)

        def INT(self):
            return self.getToken(elogGeneratorParser.INT, 0)

        def MAX(self):
            return self.getToken(elogGeneratorParser.MAX, 0)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_int_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_option" ):
                return visitor.visitInt_option(self)
            else:
                return visitor.visitChildren(self)




    def int_option(self):

        localctx = elogGeneratorParser.Int_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_int_option)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [elogGeneratorParser.MIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                localctx.opt_name = self.match(elogGeneratorParser.MIN)
                self.state = 99
                localctx.opt_value = self.match(elogGeneratorParser.INT)
                pass
            elif token in [elogGeneratorParser.MAX]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                localctx.opt_name = self.match(elogGeneratorParser.MAX)
                self.state = 101
                localctx.opt_value = self.match(elogGeneratorParser.INT)
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


    class Dec_optionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.opt_name = None # Token
            self.opt_value = None # Token

        def MIN(self):
            return self.getToken(elogGeneratorParser.MIN, 0)

        def DECIMAL(self):
            return self.getToken(elogGeneratorParser.DECIMAL, 0)

        def MAX(self):
            return self.getToken(elogGeneratorParser.MAX, 0)

        def DEC_CASES(self):
            return self.getToken(elogGeneratorParser.DEC_CASES, 0)

        def INT(self):
            return self.getToken(elogGeneratorParser.INT, 0)

        def getRuleIndex(self):
            return elogGeneratorParser.RULE_dec_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_option" ):
                return visitor.visitDec_option(self)
            else:
                return visitor.visitChildren(self)




    def dec_option(self):

        localctx = elogGeneratorParser.Dec_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dec_option)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [elogGeneratorParser.MIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                localctx.opt_name = self.match(elogGeneratorParser.MIN)
                self.state = 105
                localctx.opt_value = self.match(elogGeneratorParser.DECIMAL)
                pass
            elif token in [elogGeneratorParser.MAX]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                localctx.opt_name = self.match(elogGeneratorParser.MAX)
                self.state = 107
                localctx.opt_value = self.match(elogGeneratorParser.DECIMAL)
                pass
            elif token in [elogGeneratorParser.DEC_CASES]:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                localctx.opt_name = self.match(elogGeneratorParser.DEC_CASES)
                self.state = 109
                localctx.opt_value = self.match(elogGeneratorParser.INT)
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





