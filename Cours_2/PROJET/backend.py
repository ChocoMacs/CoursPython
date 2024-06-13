import sqlite3
import time
import psutil
import os

#import keyboard

# Archives Old DB
PATH_DB = "Cours_2/PROJET/metrics.db"
ARCHIVES_DB = "Cours_2/PROJET/metrics.old_db"
if os.path.isfile(PATH_DB):
    n = input("Nouvelle DB : Y/N")
    if (n == "Y"):
        os.rename(PATH_DB,ARCHIVES_DB)
    

try:
    while True:
        # DBsql :
        con = sqlite3.connect(PATH_DB)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS stats (time, cpu, ram_used, ram_free, batt, used_disk, free_disk )")

        # Metriques a disposition:
        ## temps
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")

        ## CPU
        cpu_usage = psutil.cpu_percent(interval=1)

        ##RAM 
        mem = str(psutil.virtual_memory())
        mem = mem.replace(',','')
        mem = mem.split()

        mem_total = mem[0].split("=")
        mem_total = mem_total[1]
        mem_total = round(int(mem_total)/1024**3, ndigits=1)

        mem_used = mem[3].split("=")
        mem_used = mem_used[1]
        mem_used = round(int(mem_used)/1024**3, ndigits=1)

        mem_free = mem[4].split("=")
        mem_free = mem_free[1]
        mem_free = round(int(mem_free)/1024**3, ndigits=1)

        ## Battery
        batt = str(psutil.sensors_battery())
        batt = batt.replace('=',',')
        batt = batt.split()
        batt = batt[0].split(',')
        batt = batt[1]

        ## Disk 
        disk = str(psutil.disk_usage("/System/Volumes/Data"))
        disk = disk.replace(",","=")
        disk = disk.replace(")","")
        disk = disk.split("=")
     
        total_disk = disk[1].split("=")
        total_disk = total_disk[0]
        total_disk = round(int(total_disk)/1024**3, ndigits=1)
     
        used_disk = disk[3].split("=")
        used_disk = used_disk[0]
        used_disk = round(int(used_disk)/1024**3, ndigits=1)
     
        free_disk = disk[5].split("=")
        free_disk = free_disk[0]
        free_disk = round(int(free_disk)/1024**3, ndigits=1)
    
        percent_disk = disk[7].split("=")
        percent_disk = percent_disk[0]
        

        # Alimentation de la DB
        cur.execute("INSERT INTO stats VALUES (?,?,?,?,?,?,?)",(time_stamp,cpu_usage,mem_used,mem_free,batt,used_disk,free_disk))
        con.commit()

        # Temporisation
        time.sleep(5)

        #Print de la DB pour vérifications
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in cur.execute("SELECT time, cpu, ram_used, ram_free, batt ,used_disk, free_disk FROM stats "):
            print ("A",row[0],"votre cpu est à",row[1],"%" ,row[2],"ram free" ,row[3],"ram used" ,row[4],"de batterie",row[5], "Go utilisé",row[6], "Go de free")
    
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
