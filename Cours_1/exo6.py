Phrase = input("Donne moi une phrase : ")
n = 1
for mot in Phrase:
    if mot == ' ':
        n += 1
print("il y a ",n," mot dans la phrase.")