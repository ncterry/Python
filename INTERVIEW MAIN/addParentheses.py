"""
Given a string s of '(' and ')' parentheses, we add the minimum
number of parentheses  ((()))  and in any positions so that the resulting
parentheses string is equal and valid.

Acceptable:     ()  (())....(A) (AB)

Input 1 = "()))"
Input 2 = "((("

Given a parentesis string, return the minimum number of parentheses
we must add to make the resulting string valid.
"""

class Solution:
    def minAddToMakeValid(self, S):
        """
        :param S:   str
        :rtype:     int
        """
        count = 0
        stack = []
        for c in S:
            if c == ')':
                if len(stack) > 0 and stack[len(stack) - 1] == '(':
                    del stack[len(stack) - 1]
                else:
                    count = count + 1
            else:
                stack.append('(')
        for c in stack:
            count = count + 1
        return count



addParen = Solution()
print(f'Parenthesis needed:  {addParen.minAddToMakeValid("((())(((")}')