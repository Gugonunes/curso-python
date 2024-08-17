def multiply(*args):
  total = 1
  for arg in args:
    total *= arg
  
  return total

print(multiply(1,2,3,4,5))

def odd_even(numero):
  return "even" if numero % 2 == 0 else "odd"

print(odd_even(6))