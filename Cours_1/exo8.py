###### Variables ####### 

########################

temps = input("Donne moi l'heure en 'HH:MM' : ").split(':')

if int(temps[0]) < 0 or int(temps[1]) < 0:
    print("Mauvaise heure")
elif int(temps[0]) > 24 or int(temps[1]) > 59:
    print("Mauvaise heure")

temps[1] = str(int(temps[1])+ 1) 
if int(temps[1]) == 60:
    temps[1] = '00'
    temps[0] = str(int(temps[0])+ 1)
    if int(temps[0]) == 24:
        temps[0] = '00'
print("Il sera ",temps[0],':',temps[1],"dans 1 minute")