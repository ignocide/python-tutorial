# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(my_pets)
print(uppered_pets)



# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = list(zip(my_strings, my_numbers))

print(results)
print(type(results[0]))