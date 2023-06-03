from lexer import Lexer
import sys

while True:
    text = input("calc > ")

    if text.strip() == "":
        continue

    try:
        lexer = Lexer(text)
        tokens = lexer.get_tokens()
        print(tokens)
    except RuntimeError as e:
        print("error:", e.args[0], file=sys.stderr)
