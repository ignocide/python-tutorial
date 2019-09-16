# integer

myint = 7
print(myint)

# float

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

# string

mystring = "string"
print(mystring)

mystring = 'string'
print(mystring) 

mystring = "Don't worry about apostrophes"
print(mystring)


# multi define

a,b = 3,4

print(a,b);


one = 1
two = 2
hello = "hello"
try :
  print(one + two + hello)
except TypeError: 
  print('integer and string can not be plused')




# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)