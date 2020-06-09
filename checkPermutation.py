""" Given two strings, write a method to decide if one is a permutation of the other. """


def checkPermutation(stringA, stringB):
    if len(stringA) != len(stringB):
        # Not a permutation if they are different lengths
        return False
    elif stringA == stringB:
        # If they are the same string, they are permutations
        return True
    else:
        # loop through stringA, return false when a char is not found in stringB
        for char in stringA:
            if char not in stringB:
                return False

    return True


print("hello and llohe")
print(checkPermutation("hello", "llohe"))

print("world and world")
print(checkPermutation("world", "world"))

print("hello and world")
print(checkPermutation("hello", "world"))

print("hello and empty string")
print(checkPermutation("hello", ""))
