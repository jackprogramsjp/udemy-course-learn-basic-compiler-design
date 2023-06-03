import tokens


class NumberNode:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


class BinaryNode:
    def __init__(self, type: str, left_node, right_node):
        self.type = type
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self) -> str:
        return (
            "("
            + str(self.left_node)
            + tokens.operator_to_character(self.type)
            + str(self.right_node)
            + ")"
        )


class UnaryNode:
    def __init__(self, type: str, node):
        self.type = type
        self.node = node

    def __repr__(self) -> str:
        return "(" + tokens.operator_to_character(self.type) + str(self.node) + ")"
