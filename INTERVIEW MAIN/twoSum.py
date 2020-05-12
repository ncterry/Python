"""Search through a list for 2 numbers, that will have a sum of a target.
###     num_list = [-234, 43545, 2, 5, 345, 7]
###     target = 12

two_sum(num_list, target) ---> True

### 0(n^2),   0(n  ln  n),  0(n)
We have 3 functions below, same result but with different complexities.
"""
# --------------------------------------------------------
# --------------------------------------------------------
# Simple double for-loop, but is the most time consuming.
def two_sum_n_squared(num_list, target):    # ----------- This is more of a brute force function
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            value = num_list[i] + num_list[j]        # i1+(j1, j2, j3...) cycle through each j for each i
            if (target == value) and (i != j):       # Don't add number in the list to itself.
                return True, num_list[i], num_list[j]   # To also return the values that == True
    return False


# --------------------------------------------------------
# --------------------------------------------------------
def two_sum_n_ln_n(num_list, target):
    # num_list = [34, 234, 54, -10]
    # target = 30
    # sorted_num_list = [-10, 34, 54, 234]
    """ Work from outside -> in     (L -->          <-- R)
        Start with   -10 + 234
        This is larger than target=30, so we to stay with L, and move in from the R.
                    -10 + 54    Larger than target=30, move in another on R
                    -10 + 34    Smaller that target=30, move in from L
                    But this means our position of L==R so we can return false."""
    num_list.sort()         # Sort the list that was sent in.
    left_index = 0              # L
    right_index = len(num_list) - 1    # R

    while left_index < right_index:
        value = num_list[left_index] + num_list[right_index]
        if target == value:
            return True, num_list[left_index], num_list[right_index]
        elif target < value:
            right_index -= 1    # Move in from R
        elif target > value:
            left_index += 1     # Move in from L
    return False    # Fallback on False


# --------------------------------------------------------
# --------------------------------------------------------
""" # num_list = 34, 43, 1, 2[
    # target = 3
    # already_seen =  34, 43, 1 ......
    Create empty set, then go through list.
    At 34, first value, just add to set. 
        Then list=43, we need -40 to get target=3
            Check set, only have 34 in there, (not -40), so add 43 to set.
        Then list=1, we need 2.
            Check set, (34, 43), doesn't work, so add 1 to set.
        Then list=2, we need 1.
            Check set, (34, 43, 1) DOES work. Return True and values."""
def two_sum_n(num_list, target):
    already_seen = set()        # Empty set to hold viewed list values.
    for number in num_list:
        difference = target - number
        if difference in already_seen:
            return True, number, difference
        else:
            already_seen.add(number)
    return False    # Fallback on False


# --------------------------------------------------------
# --------------------------------------------------------
print(two_sum_n_squared([-234, 43545, 2, 5, 345, 7], 12))
print((two_sum_n_ln_n([-234, 43545, 2, 5, 345, 7], 12)))
print(two_sum_n([-234, 43545, 2, 5, 345, 7], 12))