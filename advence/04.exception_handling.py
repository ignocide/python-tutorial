def do_stuff_with_number(n):
  print(n)

def catch_this():
    this_list = (1,2,3,4,5)

    for i in range(20):
      try:
        do_stuff_with_number(this_list[i])
      except IndexError:
        do_stuff_with_number(0)

catch_this()

