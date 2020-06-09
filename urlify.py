""" Write a method to replace all spaces in a string with '%20'. """


def urlify(string):
    if " " not in string:
        # if there are no spaces in the string, just return it
        return string

    else:
        # copy char by char, replace spaces with '%20'
        url = ""
        for char in string:
            if char == " ":
                url += "%20"
            else:
                url += char
        return url


print(urlify("hello world"))

print(urlify(" hello world"))

print(urlify("hello world "))

print(urlify(" hello world "))

print(urlify(""))
