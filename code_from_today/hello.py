import sys


def hello(name):
  if name == 'Alice':
    name = name + '???????'
  else:
    call_a_function_that_does_not_exist()

  name = name + "!!!'!!'!"
  print('hello', name)



# Define a main() function that prints a little greeting.
def main():
  hello(sys.argv[1])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
