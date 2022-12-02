from typing import List, Any, Callable, Union
# from graphviz import *

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value) -> None:
        self.value=value
        self.left_child=None
        self.right_child=None


    def is_leaf(self) -> bool:
        if self.left_child or self.right_child:
            return False
        return True


    def add_left(self, value: Any) -> None:

        self.left_child = BinaryNode(value)

    def add_right(self, value: Any) -> None:

        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        if self.right_child:
            self.right_child.traverse_in_order(visit)
        visit(self)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        if self.right_child:
            self.right_chil.traverse_in_order(visit)




    # def search(self,value: Any) -> Union["TreeNode", None]:
    #     if self.value==value:
    #         return self
    #     for x in self.children:
    #         wynik=x.search(value)
    #         if wynik:
    #             return wynik

    # def show(self, x=Graph('NTGAWTP')):
    #     x.node(str(self), str(self.value), shape='egg',color="blue")
    #     for i in self.children:
    #         x.edge(str(self), str(i),color="red")
    #         i.show(x)
    #     return x
    #
#
class BinaryTree:
    root: BinaryNode

    def __init__(self, root) -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(BinaryNode(value))

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self) -> None:
        self.root.show().render(filename='Obraz', format='jpg')



def rysuj(x: 'BinaryNode') -> None:
    if isinstance(x, BinaryNode):
        print(x.value)
    else:
        print(x)



b=BinaryNode(10)
b.add_left(9)
b.add_right(2)
b.left_child.add_left(1)
b.left_child.add_right(3)
b.right_child.add_right(6)
b.right_child.add_left(4)

tree = BinaryTree(b)

tree.traverse_in_order(print)

