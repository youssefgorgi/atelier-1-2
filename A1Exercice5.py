


#defining the function

def compte (c):
                  nbr=0 # on initialise au dibut un variable
                  while c!=0: #condition
                                    c= int(c/10)
                                    nbr=nbr+1 # chaque fois en incrément
                  return nbr
c=int(input("veullez saisir un nombre:"))    #demende à l'utilisateur de saisir un nombre 
print("Nombre total de chiffres dans le nombre",c,"est",compte(c)) # l'affichage