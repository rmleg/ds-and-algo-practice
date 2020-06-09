""" Given a string, write a function to check if it is a permutation of a palin- 
drome. A palindrome is a word or phrase that is the same forwards and backwards.
 A permutation is a rearrangement of letters. The palindrome does not need to be 
 limited to just dictionary words. """


def palinperm(string):
    # brute force: check every permutation to see if it is a palindrome
    # better: try to build a palindrome from the string
    # do we ignore whitespace?

    # need to store whether I have already visited a letter?
    # need to store a copy of the string with visited letters removed?

    # sort string
    sortedString = sorted(string.lower())

    # ignore whitespace
    # count how many unpaired chars there are
    countUnpaired = 0
    # if more than 1 unpaired char, return false

    # initialize iterator variable
    i = 0

    while i < len(sortedString):
        if sortedString[i] == " ":
            # ignore whitespace, increment i
            i += 1
        elif i + 1 < len(sortedString) and sortedString[i] != sortedString[i + 1]:
            # if char is not the same as next char, increment countUnpaired
            countUnpaired += 1
            if countUnpaired > 1:
                # if more than one unpaired char, is not a perm of a palindrome
                return False
            else:
                # otherwise, increment i and continue to next char
                i += 1
        elif i + 1 < len(sortedString) and sortedString[i] == sortedString[i + 1]:
            # if char is same as next char, increment i twice to skip the next char (I hope)
            i += 2

    return True


print(palinperm("taco cat"))

print(palinperm("rachel leggett"))

print(palinperm("Tact Coa"))

print(palinperm("race car cra care"))
