class Myclass:
  x = "blah"

  def __init__(self):
    print("this is __init__")
    self.x = 'x' 


  def function(self):
    print("this is a message inside the class")
    print(self)

myobj = Myclass()

print(myobj.x)

print(myobj.function())