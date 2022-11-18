from typing import List, Any, Callable, Union
from graphviz import *

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value) -> None:
        self.value=value
        self.children=[]


    def is_leaf(self) -> bool:
        if self.children:
            return False
        return True


    def add(self,child:'TreeNode') -> None:
        self.children.append(child)


    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        x = [self]
        while x:
            visit(x[0])
            for i in x[0].children:
                x.append(i)
            x.pop(0)

    def search(self,value: Any) -> Union["TreeNode", None]:
        if self.value==value:
            return self
        for x in self.children:
            wynik=x.search(value)
            if wynik:
                return wynik

    def show(self, x=Graph('NTGAWTP')):
        x.node(str(self), str(self.value), shape='egg',color="blue")
        for i in self.children:
            x.edge(str(self), str(i),color="red")
            i.show(x)
        return x


class Tree:
    root: TreeNode

    def __init__(self, root) -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        self.root.show().render(filename='Obraz', format='jpg')


def rysuj(x: 'TreeNode') -> None:
    if isinstance(x, TreeNode):
        print(x.value)
    else:
        print(x)




a = TreeNode("F")
a.add(TreeNode("B"))
a.add(TreeNode("G"))
a.children[0].add(TreeNode("A"))
a.children[0].add(TreeNode("D"))
a.children[1].add(TreeNode("I"))
a.children[0].children[1].add(TreeNode("C"))
a.children[0].children[1].add(TreeNode("E"))
a.children[1].children[0].add(TreeNode("H"))

# tree.add(123,tree.root.search(1))
#a.for_each_deep_first(rysuj)
#a.for_each_level_order(rysuj)
#print(a.is_leaf())
#print(a.search(10))
#b = Tree(a)
#b.show()



