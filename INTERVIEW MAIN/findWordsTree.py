"""
We have a list:
['dog', 'dark', 'cat', 'door', 'dodge', 'do']

If we want to sort, search, etc. As a list it will just be a slow  0(n)
We want it in a TRIE tree.
                                 ()
                                /  \
                              d      c       EX.  d=node   o,a = children
                             /\       \
                            o  a        a
                          //\   \        \
                        d g  o   r         t
                       /      \   \
                      g        r   k
                     /
                    e

Now we will create class/functions, so that if we send in  'do'  as a prefix
  The program will return all words starting with that prefix.
  ['dog', 'door', 'dodge']

Video's code, with NCT's notes.
"""

# Autocompletion
# Video explanation at https://www.youtube.com/watch?v=QGVCnjXmrNg

class Node:

    def __init__(self, children, isWord):
        self.children = children  # the char below it
        self.isWord = isWord

class Solution:
    def __init__(self):
      self.trie = None

    def build(self, words):
        self.trie = Node({}, False)     # Create base trie structure.
        for word in words:              # Iterate through list
            current = self.trie         # Start at head of trie
            for char in word:
                if not char in current.children:              # If char is not in current children....
                    current.children[char] = Node({}, False)  # ... then create it.
                current = current.children[char]              # Then move to the new child.
            current.isWord = True       # Mark node as a word. 2nd for loop so must be end of a word.

    def autocomplete(self, prefix):           # Given prefix, it will return a set of words
        current = self.trie                   # Start by pointing to head of trie
        for char in prefix:                   # [d] [o]
            if char not in current.children:  # If we cannot find that char in node's children, then break.
                return []
            current = current.children[char]      # If we CAN find that char, move to that node.
        return self._findWordsFromNode(current, prefix)     # Sent in 'do', and found down to 'do' on tree  head->d->o.
                                                            # Now we will go find all words from this point.
    def _findWordsFromNode(self, node, prefix):   # From current node, return all of words: ['dog', 'door', 'dodge']
        words = []                  # list to append words we find, and return list.
        if node.isWord:             # If node is marked as word,  ex. d->o->g..... g=isWord since it does complete (dog)....
            words += [prefix]       # ..... then add word to list.
        for char in node.children:  # Go through each next node-children (chars) then call function to repeat if words.
            words += self._findWordsFromNode(node.children[char], prefix + char)
        return words


s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))     # Expected Answer:  ['dog', 'door', 'dodge']
print(s.trie)
