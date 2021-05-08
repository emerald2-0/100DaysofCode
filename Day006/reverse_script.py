#function to reverse via loop
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

#prompt
mystring = input("Enter a string to reverse: ")

#call
print(reverse(mystring))