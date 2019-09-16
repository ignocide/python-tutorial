# list

mylist = []

mylist.append(1)

mylist.append(2)

mylist.append(3)

print(mylist[0])
print(mylist[1])
print(mylist[2])

# prints out 1,2,3
for x in mylist:
    print(x)


# mylist = [1,2,3]
# print(mylist[10])

# IndexError: list index out of range

numbers = [0,1,2,3,4]
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)