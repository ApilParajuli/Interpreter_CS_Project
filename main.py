import os
import sys
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

def main(input_file):
    # Step 1: Read the input file
    with open(input_file, 'r') as file:
        source_code = file.read()
    
    # Step 2: Tokenize the input
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)  # Optional: Debugging to see tokens
    
    # Step 3: Parse the tokens into an AST
    parser = Parser(tokens)
    ast = []
    while parser.current_pos < len(tokens):  # Parse multiple statements
        ast.append(parser.parse())
    
    # Step 4: Interpret the AST
    interpreter = Interpreter()
    for node in ast:
        interpreter.visit(node)

if __name__ == "__main__":
    if  os.path.exists(sys.argv[1]) is False:
        print("File or folder maynot exist!!")
        
    else:
         main(sys.argv[1])
