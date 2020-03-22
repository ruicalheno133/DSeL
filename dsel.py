import sys
from antlr4 import *
from grammar.elogGeneratorLexer import elogGeneratorLexer
from grammar.elogGeneratorParser import elogGeneratorParser
from grammar.elogGeneratorVisitor import elogGeneratorVisitor

# Generate from file
def parseFile (file):
  
    input = FileStream(file)

    lexer = elogGeneratorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = elogGeneratorParser(stream)
    tree = parser.s()

    visitor = elogGeneratorVisitor()
    elogGeneratorVisitor().visit(tree) 

# Generate from string
def parseString (str):
  
    input = inputStream(str)

    lexer = elogGeneratorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = elogGeneratorParser(stream)
    tree = parser.s()

    visitor = elogGeneratorVisitor()
    elogGeneratorVisitor().visit(tree) 

filepath = sys.argv[1]
parseFile(filepath)