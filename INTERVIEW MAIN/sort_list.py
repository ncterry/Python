
# Create a simple sorting function.
'''
We send the original array, and a new empty array to the function.
When we find a lower value in the old array,
    We copy that low value to the new array.
    Then we also delete it from the old array.
    We keep this up until the old array doesn't exist anymore.
'''
def sorter(array_old=[], array_new=[]):
    while array_old:            # While unsorted array still exists.
        min = array_old[0]      # Lowest current value
        for n in array_old:     # Cycle through old array until you find one less than min
            if n < min:         # If less than min
                min = n         # Set min to that new lowest value
        array_new.append(min)   # Append new low value to new array
        array_old.remove(min)   # Remove that value from old. Old will eventually not exist.
    return array_new
# --------------------------------------------------
print(sorter([2, 5, 9, 3, 8, 1, 10, 6, 4, 7], []))
# --------------------------------------------------

