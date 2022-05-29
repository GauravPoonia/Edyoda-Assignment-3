# Calculate the uppercase and lowercase cha

s = input("Enter a string : ")
print("Original string is : ",s)

def calc():
    count = {"UPPER_CASE":0, "LOWER_CASE":0}
    for i in s:
        if i.isupper():
            count["UPPER_CASE"] += 1
        elif i.islower():
            count["LOWER_CASE"] += 1
        else:
            pass

    print("No. of Upper case characters :",count["UPPER_CASE"])
    print("No. of Lower case characters :",count["LOWER_CASE"])

calc()