from typing import Optional

TT_NUMBER = "TT_NUMBER"
TT_PLUS = "TT_PLUS"
TT_MINUS = "TT_MINUS"
TT_MULTIPLY = "TT_MULTIPLY"
TT_DIVIDE = "TT_DIVIDE"
TT_MODULO = "TT_MODULO"
TT_LPAREN = "TT_LPAREN"
TT_RPAREN = "TT_RPAREN"

def operator_to_character(token_type: str) -> str:
    if token_type == TT_PLUS:
        return '+'
    elif token_type == TT_MINUS:
        return '-'
    elif token_type == TT_MULTIPLY:
        return '*'
    elif token_type == TT_DIVIDE:
        return '/'
    elif token_type == TT_MODULO:
        return '%'
    elif token_type == TT_LPAREN:
        return '('
    elif token_type == TT_RPAREN:
        return ')'

class Token:
    def __init__(self, type: str, value: Optional[float] = None):
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        token_repr = self.type.replace("TT_", "") # This will remove the 'TT_' string part

        if self.value is not None:
            token_repr += ":" + str(self.value)
        
        return token_repr
