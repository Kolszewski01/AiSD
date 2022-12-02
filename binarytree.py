from typing import Any, Callable
from graphviz import *

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value) -> None:
        self.value=value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if self.left_child or self.right_child:
            return False
        return True


    def add_left(self, value: Any) -> None:
        self.left_child=BinaryNode(value)

    def add_right(self, value: Any) -> None:
        self.right_child=BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)


    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root=root

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)


tree = BinaryNode(10)
tree.add_left(9)
tree.left_child.add_left(1)
tree.left_child.add_right(3)
tree.add_right(2)
tree.right_child.add_left(4)
tree.right_child.add_right(6)

treen=BinaryTree(tree)

treen.traverse_in_order(print)
print('----------------')
treen.traverse_post_order(print)
print('----------------')
treen.traverse_pre_order(print)

assert treen.root.value == 10
assert treen.root.right_child.value == 2
assert treen.root.right_child.is_leaf() is False
assert treen.root.left_child.left_child.value == 1
assert treen.root.left_child.left_child.is_leaf() is True

