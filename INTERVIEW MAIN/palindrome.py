"""
Write a function to check if a string is a palindrome or not.
"""
# ------------------------------------------------------------------------------
def isPalindrome(string):
    left, right = 0, len(string)-1
    while right >= left:
        if not string[left] == string[right]:
            print(f'{string} is not a palindrome.')
            return False
        left += 1
        right -= 1
        #print(string)           # print string
        #print(string[::-1])     # print string in reverse
    return True


print(isPalindrome("redrums dfd smurder"))      