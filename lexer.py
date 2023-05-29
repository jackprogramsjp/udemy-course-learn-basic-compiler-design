from typing import Optional
import tokens
from tokens import Token

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.current_char: Optional[str] = None
        self.advance()
    
    def advance(self):
        if self.index < len(self.text):
            self.current_char = self.text[self.index]
            self.index += 1
        else:
            self.current_char = None

    def get_tokens(self):
        tokens_list: list[Token] = []
        
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char == '.' or self.current_char.isdigit():
                tokens_list.append(self.get_number())
            elif self.current_char == '+':
                self.advance()
                tokens_list.append(Token(tokens.TT_PLUS))
            elif self.current_char == '-':
                self.advance()
                tokens_list.append(Token(tokens.TT_MINUS))
            elif self.current_char == '*':
                self.advance()
                tokens_list.append(Token(tokens.TT_MULTIPLY))
            elif self.current_char == '/':
                self.advance()
                tokens_list.append(Token(tokens.TT_DIVIDE))
            elif self.current_char == '%':
                self.advance()
                tokens_list.append(Token(tokens.TT_MODULO))
            elif self.current_char == '(':
                self.advance()
                tokens_list.append(Token(tokens.TT_LPAREN))
            elif self.current_char == ')':
                self.advance()
                tokens_list.append(Token(tokens.TT_RPAREN))
            else:
                raise RuntimeError("Illegal character -> " + self.current_char)
        
        return tokens_list
    
    def get_number(self):
        number: str = self.current_char
        dot_count = 0
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char.isdigit()):
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    break

            number += self.current_char
            self.advance()

        if number[0] == '.':
            number = '0' + number
        
        if number[-1] == '.':
            number += '0'
        
        return Token(tokens.TT_NUMBER, float(number))
