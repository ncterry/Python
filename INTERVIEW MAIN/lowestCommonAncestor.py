"""
Binary tree
                   6
                /     \
               2       8
              / \     / \
             0   4   7   9
                / \
               3   5

We are given a pointer to the root of the tree, and 2 values v1, v2
You need to return the lowest common ancestor of v1, v2
v1=2, v2=8
The lowest common ancestor in this tree would be 6
"""
# VVV VVV VVV      Base Binary Tree      VVV VVV VVV
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:                       # if data exists on node
            if data < self.data:            # if new data is less than data on node
                if self.left is None:       # if there is nothing less\left of this node
                    self.left = Node(data)  # new data is less, no current left, so create node to the left
                else:
                    self.left.insert(data)  # else, move to left of node, and insert a new node with new data
            elif data > self.data:          # if new data is greater than current node data
                if self.right is None:      # if no node to the right, create new right-node
                    self.right = Node(data)
                else:
                    self.right.insert(data)  # there is another right-node, run insert check on next
        else:
            self.data = data        # If no data on current node, then we can place data on node.

    def printtree(self):            # We want to print from least to most in tree.
        if self.left:               # if left exists, then there must be a node to the left.
            self.left.printtree()   # run print tree again on the left. Want to move to the least node first
        print(self.data)
        if self.right:              # if there is a node to the right (not None)
            self.right.printtree()

    # ^^^ Base Binary Tree ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # VVV VVV VVV      Attached Ancestor Function      VVV VVV VVV
    def lowestCommonAncestor(self, p, q):           # local function to run on the local binary tree w/2 ancestor values
        while self:                                 # while the tree exists
            if p > self.data and q > self.data:     # if both values are greater, then go to the right and check again
                self = self.right
            elif p < self.data and q < self.data:   # if both values are less, then go to the left and check again.
                self = self.left
            else:
                return self.data    # reached the node where v1, v2 are on either side, this must be the right ancestor
# ----------------------------------------------------------------
# Input Tree: [6,2,8,0,4,7,9,3,5]
# Create head node
root = Node(6)
#
root.insert(2)
root.insert(8)
root.insert(0)
root.insert(4)
root.insert(7)
root.insert(9)
root.insert(3)
root.insert(5)
#
root.printtree()
#
print(f'\n\nHead(data) = {root.data}')  # head node, so it will be 6 since that is the first we put in
#
print(f'Lowest Common Ancestor of 2, 8 = {root.lowestCommonAncestor(2, 8)}')
print(f'Lowest Common Ancestor of 2, 4 = {root.lowestCommonAncestor(2, 4)}')
print(f'Lowest Common Ancestor of 7, 9 = {root.lowestCommonAncestor(7, 9)}')
print(f'Lowest Common Ancestor of 5, 0 = {root.lowestCommonAncestor(5, 0)}')


"""
We created a basic binary tree above.
Now input 2 descendants, now find lowest common ancestor from them, with 'them' included as a potential - See ex2.
#
Input: [6,2,8,0,4,7,9,3,5]
ex1. Descendants: p=2, q=8
Output = 6
---
ex2. Descendants: p=2, q=4
Output = 2
                   6
                /     \
               2       8   
              / \     / \
             0   4   7   9
                / \
               3   5
"""