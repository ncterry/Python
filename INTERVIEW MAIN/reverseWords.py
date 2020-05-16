"""
Given an input string, reverse the string word by word.

Input:  the sky is blue
Output: blue is sky the
"""
# {start} will begin at the end of the string and work back.

class Solution(object):
    def reverseString(self, inputstring):
        inputstring = inputstring.strip()   # Strip front/trailing whitespace
        print(f'Input String = {inputstring}')
        words = []                          # Stack to hold reverse string.
        start, end = 0, len(inputstring)    # Locations to indicate individual words in string
        # [blue]<-start|end
        # start[blue]end
        for i in range(0, len(inputstring)):
            start = len(inputstring) - 1 - i    # Reverse-traverse over string.
            if inputstring[start] == " " and start != len(inputstring) - 1:  # Stop extra space on end if not trimmed.
                words.append(inputstring[(start + 1):end] + " ")  # Find space, then place word prior on stack
                end = start  # Word is placed, now start after the related space       sky' 'blue
            elif start == 0:
                words.append(inputstring[start:end])  # Spaces trimmed at top, so this is the first char
                end = start

        print(words)
        return ''.join(words)


try1 = Solution()
print(f'\n{try1.reverseString("  the sky is blue    ")}')    # start/end white space trimmed in function.
