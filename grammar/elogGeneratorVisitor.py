# Generated from elogGenerator.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .elogGeneratorParser import elogGeneratorParser
else:
    from elogGeneratorParser import elogGeneratorParser

import random
import pandas as pd

# This class defines a complete generic visitor for a parse tree produced by elogGeneratorParser.

class elogGeneratorVisitor(ParseTreeVisitor):
    def __init__(self): 
        self.rows = 0 
        self.traces = []
        self.activities = {}
        self.columns = {}
        self.last_timestamp = 0

    def get_int_value(self, c_obj):
        minv = float(c_obj.get('MIN', 0))
        maxv = float(c_obj.get('MAX', 100))
        cases = int(c_obj.get('DEC_CASES', 2))
        value = round(random.uniform(minv, maxv), cases)

        return value

    def get_dec_value(self, c_obj):
        minv = int(c_obj.get('MIN', 0))
        maxv = int(c_obj.get('MAX', 100))
        value = random.randint(minv,maxv)

        return value

    def get_random_value(self, c_obj): 
        value = ""

        if c_obj['type'] == "Number": 
            value = self.get_int_value(c_obj)

        elif c_obj['type'] == "Int":
            value = self.get_dec_value(c_obj)

        elif c_obj['type'] == "Timestamp":
            value = int(random.random() * 1000) + self.last_timestamp
            self.last_timestamp = value

        elif c_obj['type'] == "String": 

            value = "randomString"

        return value

    def build_row(self, case_id, activity):
        row = ""
        row += f"{case_id},"
        row += f"{self.activities[activity]}" 

        for c_obj in self.columns.values(): 
            row += f",{self.get_random_value(c_obj)}"

        row += '\n'
        return row 

    def build_df_row(self, case_id, activity) :
        row = [case_id, activity] 

        for c_obj in self.columns.values(): 
            row.append(self.get_random_value(c_obj)) 

        return row

    def build_header(self):
        header = "CaseID,ActivityID"

        for c_name in self.columns.keys():
            header += f",{c_name}"

        header += '\n'
        return header

    def build_df_header(self):
        header = ['CasedID', 'ActivityID']

        for c_name in self.columns.keys():
            header.append(c_name) 

        return header

    def create_df(self): 
        header = self.build_df_header()
        rows = []

        for i in range(1, self.rows + 1): 
            # pick a random trace
            trace = random.randrange(0, len(self.traces))

            self.last_timestamp = 0
            # create a row based on that trace
            for a in self.traces[trace]: 
                row = self.build_df_row(i, a)
                rows.append(row)

        return pd.DataFrame(rows, columns=header)

    def create_csv(self, filename): 
        # Open file
        f = open(filename, 'w+')

        # Build header string
        header = self.build_header()
        
        # write header 
        f.write(header)

        # For each case 
        for i in range(1, self.rows + 1): 
            # pick a random trace
            trace = random.randrange(0, len(self.traces))
            self.last_timestamp = 0
            # create a row based on that trace
            for a in self.traces[trace]: 
                row = self.build_row(i, a)
                f.write(row)

        # Close file
        f.close()

        return None

    # Visit a parse tree produced by elogGeneratorParser#s.
    def visitS(self, ctx:elogGeneratorParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#g_type.
    def visitG_type(self, ctx:elogGeneratorParser.G_typeContext):

        # Visit children and gather log info
        self.visitChildren(ctx)

        if ctx.output.text == "LOG": 
            filename = str(ctx.FILENAME())
            return self.create_csv(filename)
            
        elif ctx.output.text == "DF":
            return self.create_df()

    # Visit a parse tree produced by elogGeneratorParser#body.
    def visitBody(self, ctx:elogGeneratorParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#activities.
    def visitActivities(self, ctx:elogGeneratorParser.ActivitiesContext):
        for a in ctx.a_mapping():
            self.activities[str(a.TEXT())] = str(a.ID())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#a_mapping.
    def visitA_mapping(self, ctx:elogGeneratorParser.A_mappingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#traces.
    def visitTraces(self, ctx:elogGeneratorParser.TracesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#t_list.
    def visitT_list(self, ctx:elogGeneratorParser.T_listContext):
        trace = [] 
        for a in ctx.TEXT():
            trace.append(str(a))
        self.traces.append(trace)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#count.
    def visitCount(self, ctx:elogGeneratorParser.CountContext):
        self.rows = int(str(ctx.INT()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#columns.
    def visitColumns(self, ctx:elogGeneratorParser.ColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#column.
    def visitColumn(self, ctx:elogGeneratorParser.ColumnContext):
        c_name = str(ctx.TEXT())
        c_type = ctx.c_type().t.text
        c_obj = {}

        c_obj['type'] = c_type

        if c_type == "Int":

            for option in ctx.c_type().int_option():
                opt_name, opt_val = self.visitInt_option(option)
                c_obj[opt_name] = opt_val

        elif c_type == "Number":

            for option in ctx.c_type().dec_option():
                opt_name, opt_val = self.visitDec_option(option)
                c_obj[opt_name] = opt_val
        
        self.columns[c_name] = c_obj

        return self.visitChildren(ctx)


    # Visit a parse tree produced by elogGeneratorParser#c_type.
    def visitC_type(self, ctx:elogGeneratorParser.C_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by elogGeneratorParser#int_option.
    def visitInt_option(self, ctx:elogGeneratorParser.Int_optionContext):
        return ctx.opt_name.text, ctx.opt_value.text

    # Visit a parse tree produced by elogGeneratorParser#dec_option.
    def visitDec_option(self, ctx:elogGeneratorParser.Dec_optionContext):
        return ctx.opt_name.text, ctx.opt_value.text



del elogGeneratorParser