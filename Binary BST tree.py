from typing import Any, List
from graphviz import Digraph


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



    def min(self):
        if self.left_child:
            return self.left_child.min()
        return self







    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root=root

    def __insert(self, node: 'BinaryNode', val: Any):
        if node:
            if node.value > val:
                node.left_child = self.__insert(node.left_child, val)
            else:
                node.right_child = self.__insert(node.right_child, val)
        else:
            node = BinaryNode(val)
        return node


    def insert(self, value: Any) -> None:
        self.root = self.__insert(self.root, value)

    def insert_list(self, list_:List[Any]):
        for x in list_:
            self.insert(x)


    def contains(self, value: Any) -> bool:
        temp = self.root
        while temp:
            if value > temp.value:
                temp = temp.right_child
            elif value < temp.value:
                temp = temp.left_child
            else:
                return True
        return False

    def __remove(self, node: 'BinaryNode', val: Any):
        if node.value != val:
            if node.value > val:
                node.left_child = self.__remove(node.left_child, val)
            else:
                node.right_child = self.__removee(node.right_child, val)
        else:
            if node.is_leaf():
                node = None
            elif node.left_child and node.right_child:
                node.value = node.right_child.min().value
                node.right_child = self.__remove(node.right_child, node.right_child.min().value)
            elif node.left_child:
                node = node.left_child
            else:
                node = node.right_child
        return node

    def remove(self, value: Any):
        self.root = self.__remove(self.root, value)

    





















    def show(self, g=Digraph('g')):
        q = [self.root]
        while q:
            g.node(str(q[0]), str(q[0]), shape='circle')
            if q[0].left_child:
                g.edge(str(q[0]), str(q[0].left_child))
                q.append(q[0].left_child)
            if q[0].right_child:
                g.edge(str(q[0]), str(q[0].right_child))
                q.append(q[0].right_child)
            q.pop(0)
        g.render(filename='bst', format='png', cleanup=True, view=True)




a=BinaryNode(8)
# a.insert(a,10)
# a.insert(a,3)
# a.insert(a,1)
# a.insert(a,6)
# a.insert(a,4)
# a.insert(a,7)
# a.insert(a,14)
# a.insert(a,13)

b=BinaryTree(a)

b.insert_list([10, 3, 1, 6, 4, 7, 14, 13])

b.show()

print(b.contains(20))







































