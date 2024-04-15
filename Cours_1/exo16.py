# -*- coding utf-8 -*-

c = 0
higher = 0

while c != 20:
    c += 1 
    print("Donner le nombre n°",c," : ")
    nb = int(input())
    if int(nb) > higher:
        higher = nb

print(" Le nombre le plus grand est : ",higher)

