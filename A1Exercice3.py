

#defining the function
def somme(n):
                 
                  if n <= 0:     
                                    return 0
                  else:
                                    return n + somme(n - 1) #On additionne décroissant de n à zéro
n=int (input("veuillez entre un nobre entier:"))  #demende à l'utilisateur de saisir un nombre 
print("la some de 1 jusqu'a n est;",somme(n))     #Afficher la resultat