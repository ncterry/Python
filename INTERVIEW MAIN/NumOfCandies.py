""" EASY
Given the array candies and the integer extraCandies, where candies[i]
represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the
kids such that he or she can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]             """

# candies1 = [2, 3, 5, 1, 3]; extraCandies1 = 3   # Output: [true,true,true,false,true]
# candies2 = [4, 2, 1, 1, 2]; extraCandies2 = 1   # Output: [true,false,false,false,false]
# candies3 = [12, 1, 12];     extraCandies3 = 10  # Output: [true,false,true]

def kidsWithCandies(input, extraCandies):           # Send List and extra value into function.
    output = [False, False, False, False, False]    # Output list for bool if kid can reach current max candies.
    #
    print(f'Can each child have the max candies:')
    for i in range(len(input)):                     # Cycle through the full input list.
        if input[i] + extraCandies >= max(input):   # Check if current[kid] + extra candies is more than current max
            output[i] = True    # If Kid plus extra candies is >= current max, then they turn True
        print(f'\tMax Candies:   Kid[{i+1}] --> {output[i]}')
    #
    print("\n", output[0:len(input)], "\n-----------\n")
# ---------------------------------------------------------------------


kidsWithCandies([2, 3, 5, 1, 3],  3)
kidsWithCandies([4, 2, 1, 1, 2],  1)
kidsWithCandies([12, 1, 12],  10)
