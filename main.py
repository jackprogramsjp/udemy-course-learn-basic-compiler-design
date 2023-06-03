from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
import sys

while True:
    text = input("calc > ")

    if text.strip() == "":
        continue

    try:
        lexer = Lexer(text)
        tokens = lexer.get_tokens()
        parser = Parser(tokens)
        tree = parser.parse()

        if tree is None:
            continue

        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value) # or print(value.value)
    except RuntimeError as e:
        print("error:", e.args[0], file=sys.stderr)
