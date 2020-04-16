import sys

def greet(name):
  print(f'Hello world {name}')

if (len(sys.argv)) > 1:
  name = sys.argv[1]
  greet(name)
else:
  greet('world')