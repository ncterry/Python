"""
Binary tree
             2
            / \
           1   3
               /\
              4  5
                  \
                   6

We are given a pointer to the root of the tree, and 2 values v1, v2
You need to return the lowest common ancestor of v1, v2
v1=4, v2=6
The lowest common ancestor in this tree would be 3
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
