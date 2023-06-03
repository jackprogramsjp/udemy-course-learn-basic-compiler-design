from tokens import Token
import tokens
from nodes import *
from typing import Optional


class Parser:
    def __init__(self, tokens: "list[Token]"):
        self.tokens = tokens
        self.index = 0
        self.current_token: Optional[Token] = None
        self.advance()

    def advance(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
        else:
            self.current_token = None

    def parse(self) -> Optional[any]:
        if self.current_token is None:
            return None

        result = self.expression()

        if self.current_token is not None:
            raise RuntimeError("Invalid syntax")

        return result

    def expression(self):
        result = self.term()

        while self.current_token is not None and self.current_token.type in (
            tokens.TT_PLUS,
            tokens.TT_MINUS,
        ):
            if self.current_token.type == tokens.TT_PLUS:
                self.advance()
                result = BinaryNode(tokens.TT_PLUS, result, self.term())
            elif self.current_token.type == tokens.TT_MINUS:
                self.advance()
                result = BinaryNode(tokens.TT_MINUS, result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type in (
            tokens.TT_MULTIPLY,
            tokens.TT_DIVIDE,
            tokens.TT_MODULO,
        ):
            if self.current_token.type == tokens.TT_MULTIPLY:
                self.advance()
                result = BinaryNode(tokens.TT_MULTIPLY, result, self.factor())
            elif self.current_token.type == tokens.TT_DIVIDE:
                self.advance()
                result = BinaryNode(tokens.TT_DIVIDE, result, self.factor())
            elif self.current_token.type == tokens.TT_MODULO:
                self.advance()
                result = BinaryNode(tokens.TT_MODULO, result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == tokens.TT_LPAREN:
            self.advance()

            result = self.expression()

            if self.current_token.type != tokens.TT_RPAREN:
                raise RuntimeError(
                    "There must be a right parenthesis ')' to end the expression/factor"
                )

            self.advance()

            return result
        elif token.type == tokens.TT_NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == tokens.TT_PLUS:
            self.advance()
            return UnaryNode(tokens.TT_PLUS, self.factor())
        elif token.type == tokens.TT_MINUS:
            self.advance()
            return UnaryNode(tokens.TT_MINUS, self.factor())

        raise RuntimeError("Illegal token in factoring")
