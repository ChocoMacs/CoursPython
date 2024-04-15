# Variables 
voyelles = "aeiouAEIOU"

########################

Phrase = input("Donne moi une phrase : ")
n = 0
for lettre in Phrase:
    if lettre in voyelles:
        n += 1
print("il y a ",n," voyelles dans la phrase.")