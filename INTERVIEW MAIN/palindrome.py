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
        return True


isPalindrome("redrum sdfdssmurder")