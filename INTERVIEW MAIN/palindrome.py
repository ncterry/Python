"""
Write a function to check if a string is a palindrome or not.
"""
# ------------------------------------------------------------------------------
def isPalindrome(string):
    left = 0
    right = len(string)-1
    while right >= left:
        if not string[left] == string[right]:       # If left[char] != right[char]
            print(f'{string} is not a palindrome.')
            return False
        left += 1       # move 1 from left to the right     -->
        right -= 1      # move 1 from right to the left         <--
        #print(string)           # print string
        #print(string[::-1])     # print string in reverse
    return True


print(f'Palindrome: True or False:')
print("\nredrums dfd smurder   = ")
print(isPalindrome("redrums dfd smurder"))
#
print("\nterryCyrret   = ")
print(isPalindrome("terryCyrret"))
#
print("\nxxtttnxxx   = ")
print(isPalindrome("xxtttnxxx"))