"""
Given a string s of unbalanced '(' and ')' parentheses, we add the minimum
number of parentheses  ((()))  and in any positions so that the resulting
parentheses string is equal and valid.

Acceptable:     ()  (())....(A) (AB)

Input 1 = "()))"
Input 2 = "((("

Given a parentheses string, return the minimum number of parentheses
we must add to make the resulting string valid.
"""

class Solution:
    def minAddToMakeValid(self, S):
        """
        :param S:   str
        :rtype:     int
        We can't do a double for loop as that would take too much time/space
            Instead
        """
        count = 0
        stack = []
        """
        Cycle through the string
        If there is a    )
            Then If the length of new stack > 0
            AND if the end of the new stack  == ( 
                That means there are corresponding () so delete end of new stack
                    Don't add to new stack unless there is not a (
        Else if we are missing a ( in the string, add one to the stack to keep track.
        """
        for c in S:
            if c == ')':
                if len(stack) > 0 and stack[len(stack) - 1] == '(':
                    del stack[len(stack) - 1]
            else:
                stack.append('(')
        #
        for c in stack:
            count = count + 1
        return count



addParen = Solution()
print(f'Parenthesis needed:  {addParen.minAddToMakeValid("((())((()")}')
