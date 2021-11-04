
#defining the function
def inver(a):
    new_a = []  #list vide
    index = len(a)
    while index:
        index -= 1       ## index=index-1                
        new_a.append(a[index]) #ajouter a[index] à new_a
    return ''.join(new_a)   #pour construire la liste de toute façon à être en mesure d'obtenir la taille.

a=input("veuillez tapez un mot:") #taking values from the user
print(inver(a))