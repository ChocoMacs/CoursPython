###### Variables ####### 

########################

temps = input("Donne moi l'heure en 'HH:MM:SS' : ").split(':')

if int(temps[0]) < 0 or int(temps[1]) < 0:
    print("Mauvaise heure")
elif int(temps[0]) > 24 or int(temps[1]) or int(temps[2]) > 59:
    print("Mauvaise heure")

temps[2] = str(int(temps[2])+ 1)
if  int(temps[2]) == 60:
    temps[2] = '00'
    temps[1] = str(int(temps[1])+ 1)
    if int(temps[1]) == 60:
        temps[1] = '00'
        temps[0] = str(int(temps[0])+ 1)
        if int(temps[0]) == 24:
            temps[0] = '00'
print("Il sera ",temps[0],':',temps[1],':',temps[2],"dans 1 seconde")