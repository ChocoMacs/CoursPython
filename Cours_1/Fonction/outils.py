"""Module outil contenant les fonctions suivantes :
- table

"""

def table(nb, max=10):
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
    

def nbvoyelle(chaine): 
    voyelles = "aeiouAEIOU"
    n = 0

    for lettre in chaine:
        if lettre in voyelles:
            n += 1
    print("il y a ",n," voyelles dans la phrase.")



def purge(phrase,exclu):
    newphrase = ""
    for lettre in phrase:
        if lettre != exclu:
            newphrase = newphrase + lettre
    print(newphrase)
