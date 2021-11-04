
#defining the function 

def cnv(n):
    if n > 1:
        cnv(n // 2) # floor division: nous permet de prendre juste la resultat sans vergule
    print(n % 2, end='  ')

nbr = int(input("Veuillez entrez un nombre decimal: ")) #calling the function
cnv(nbr )