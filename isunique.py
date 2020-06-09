def isUnique(string):
    """ Determine if a string has all unique characters """
    # hold visited charts
    chars = dict()
    for char in string:
        # for each character in the string
        if char in chars:
            # if the char already exists in chars, it is not unique.
            return False
        else:
            # if the char hasn't been seen yet, add it to chars
            chars[char] = True
    
    # if reach end of loop without returning False, return True
    return True

def isUniqueNoDict(string):
    """ Determine if a string has all unique characters
    WITHOUT using additional data structures """
    # hold visited chars in a string
    seenChars = ''
    for char in string:
        # for each char in string
        if char in seenChars:
            return False
        else:
            seenChars += char
    
    return True

print("hello: ")
print(isUnique('hello'))

print("goodbye: ")
print(isUnique('goodbye'))

print("rachel: ")
print(isUnique('rachel'))

print("hello: ")
print(isUniqueNoDict('hello'))

print("goodbye: ")
print(isUniqueNoDict('goodbye'))

print("rachel: ")
print(isUniqueNoDict('rachel'))

