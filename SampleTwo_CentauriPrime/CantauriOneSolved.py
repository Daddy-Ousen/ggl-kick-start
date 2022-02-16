# TODO: Complete the get_ruler function
def get_ruler(kingdom):
  ruler = ''
  # TODO: Add logic to determine the ruler of the kingdom
  alice = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
  nobody = ['Y', 'y']
  alice_tuple = tuple(alice)
  nobody_tuple = tuple(nobody)
  if kingdom.endswith(alice_tuple):
    ruler = 'Alice'
  elif kingdom.endswith(nobody_tuple):
    ruler = 'nobody'
  else:
    ruler = 'Bob'
  
  # It should be either 'Alice', 'Bob' or 'nobody'.
  return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()