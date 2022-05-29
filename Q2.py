# to reverse a given string

word = input("Enter the string to be reversed : ")

def rev():
    strng = ""

    for i in word:
        strng = i + strng
    return strng

strng = rev()
print("Reversed string is :",strng)
