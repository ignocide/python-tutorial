import random 

def lattery():
  for i in range(6):
    yield random.randint(1,40)


  yield random.randint(1,15)

for random_number in lattery():
  print("and the next number is ... %d" % (random_number))


a = 1
b = 2
a,b = b,a
print(a,b)


# fill in this function
def fib():
    pass #this is a null statement which does nothing when executed, useful as a placeholder.
