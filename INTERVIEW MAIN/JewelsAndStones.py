"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
    so "a" is considered a different type of stone from "A".

Example 1:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3
"""
# Create Dict       { a:1, A:2, ...... }
# Cycle Through J, and then add value for each in S

def numJewelsInStones(jewels, stones):
    dictjs = {} # Create a dictionary to hold search-keys and values
    for i in range(len(jewels)):    # Place all jewels as keys.
        dictjs[jewels[i]] = stones.count(jewels[i])  # Place key-->value based its own count in the stones list.
    print(dictjs)
    # -----------------------------------


numJewelsInStones("aA", "aAAbbbb")
numJewelsInStones("Nathan", "bnsleoithskdlowkfNNEJOXNCWOTHkjscnwotyqhqdn")
