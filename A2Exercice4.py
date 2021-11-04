my_set1={23, 42, 65, 57, 78, 83, 29}  # create set

my_set2={57, 83, 29, 67, 73, 43, 48}  # create set


print(my_set1.intersection(my_set2)) #affiche l'intersection entre my_set1 et my_set2


  
my_set1=my_set1-my_set1.intersection(my_set2) # Supprimez(l'intersection entre my_set1 et my_set2) de my_set1 

print("my_set 1 après suppression :",my_set1) # afficher la nouvelle my_set1