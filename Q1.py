# to sum all numbers in a list

lst = []
len = int(input("enter size of the list : "))

for i in range(len):
    elem = int(input("Enter the elements : "))
    lst.append(elem)

print("Your List is :",lst)

def sum():
    add = 0
    for i in lst:
        add += i
    return add

add = sum()
print("Expected Output is :",add)
