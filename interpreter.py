from nodes import *
from values import Number
import tokens


class Interpreter:
    def __init__(self):
        pass

    def visit(self, node) -> Number:
        if isinstance(node, BinaryNode):
            return self.visit_binary_node(node)
        elif isinstance(node, UnaryNode):
            return self.visit_unary_node(node)
        elif isinstance(node, NumberNode):
            return Number(node.value)
        else:
            raise RuntimeError("Unknown node")

    def visit_binary_node(self, node: BinaryNode) -> Number:
        if node.type == tokens.TT_PLUS:
            return Number(
                self.visit(node.left_node).value + self.visit(node.right_node).value
            )
        elif node.type == tokens.TT_MINUS:
            return Number(
                self.visit(node.left_node).value - self.visit(node.right_node).value
            )
        elif node.type == tokens.TT_MULTIPLY:
            return Number(
                self.visit(node.left_node).value * self.visit(node.right_node).value
            )
        elif node.type == tokens.TT_DIVIDE:
            try:
                return Number(
                    self.visit(node.left_node).value / self.visit(node.right_node).value
                )
            except ZeroDivisionError:
                raise RuntimeError("Dividing by zero")
        elif node.type == tokens.TT_MODULO:
            try:
                return Number(
                    self.visit(node.left_node).value % self.visit(node.right_node).value
                )
            except ZeroDivisionError:
                raise RuntimeError("Modulo operation dividing by zero")
        else:
            raise RuntimeError("Unknown token type for BinaryNode")

    def visit_unary_node(self, node: UnaryNode) -> Number:
        if node.type == tokens.TT_PLUS:
            return Number(+self.visit(node.node).value)
        elif node.type == tokens.TT_MINUS:
            return Number(-self.visit(node.node).value)
        else:
            raise RuntimeError("Unknown token type for UnaryNode")
