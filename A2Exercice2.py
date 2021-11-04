


list= [11, 45, 8, 11, 23, 45, 23, 45, 8]  #create list

print(list)

for a in range(2,len(list),3): #Deviser la liste en 3 morceaux,on commence du dernier au premier
 
  print([list[a],list[a-1],list[a-2]],end=' ') #affiche les trois 3 morceaux égaux