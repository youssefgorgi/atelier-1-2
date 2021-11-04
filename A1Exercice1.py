#defining the function calcule la somme des séries

def factorial(x):
                  if x == 1:
                                    return 1
                  else:
                                    return (x * factorial(x-1))
 #taking values from the user
a=int(input("entre un nombre:"))
b=int(input("entre un nombre:"))
c=int(input("entre un nombre:"))
d=int(input("entre un nombre:"))
e=int(input("entre un nombre:"))
print("The factorial de la premier: " , factorial(a))
print("The factorial de la la dexieme:", factorial(b))
print("The factorial de troixiem:", factorial(c))
print("The factorial de la quatriem:", factorial(d))
print("The factorial de la quatriem:", factorial(e))

som=1+factorial(a)+factorial(b)+factorial(c)+factorial(d)+factorial(e)

print("la some de est:",som)
