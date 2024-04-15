i = 0
while True:
    i += 1
    if i == 3:
        continue
    #ici le i == 3 permet de filtrer l'affichage de la valeur 3
    if i > 5:
        break
    print(i)