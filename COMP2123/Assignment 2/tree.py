"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""

import node
from node import Node

class Tree:
    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    - swap(subtree_a, subtree_b): Swap the position of the subtrees.
    """

    def __init__(self, root):
        """
        Initialises the tree with a root node.
        :param root: the root node.
        """
        self.root = root

    def put(self, node, child):
        """
        Inserts a node into the tree. Adds `child` to `node`.
        :param node: The node currently in the tree.
        :param child: The child to add to the tree.
        """
        node.add_child(child)

    def sum_of_children(self, node, total):
        total += node.key
        for c in node.children:
            total = self.sum_of_children(c, total)
        
        node.subtree_value = total
        return total

    def propogate_subtree(self, node):
        if node == None:
            return
        else:
            node.subtree_value = node.key
            for c in node.children:
                if c.subtree_value > node.subtree_value:
                    node.subtree_value = c.subtree_value
            self.propogate_subtree(node.parent)



    def flatten(self, node):
        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes.

        :param node: The root of the subtree to flatten.

        Example

           A(5)
           / \
         B(3) C(6)
         /    |  \
        D(2) E(3) F(6)

        flatten(C)

           A(5)
           / \
         B(3) C(15)
         /
        D(2)

        """

        if node.is_external() == True:
            return "Node is a leaf node"
        
        node.key = self.sum_of_children(node, 0)
        cursor = node.parent
        while cursor != None:
            cursor.subtree_value = cursor.key
            for c in cursor.children:
                if c.subtree_value > cursor.subtree_value:
                    cursor.subtree_value = c.subtree_value
            cursor = cursor.parent
       
        node.children.clear()


    def swap(self, subtree_a, subtree_b):
        """
        Swap subtree A with subtree B
        :param subtree_a: The root node of subtree_a.
        :param subtree_b: The root node of subtree_b.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """

        temp1 = subtree_a.parent
        temp2 = subtree_b.parent

        temp1.children[temp1.children.index(subtree_a)] = subtree_b
        temp2.children[temp2.children.index(subtree_b)] = subtree_a
        
        subtree_a.parent = temp2
        subtree_b.parent = temp1

        self.propogate_subtree(subtree_a)
        self.propogate_subtree(subtree_b)