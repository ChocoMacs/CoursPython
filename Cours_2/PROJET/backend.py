import sqlite3
import time
import psutil
import os
import shutil
#import keyboard

# Archives Old DB
PATH_DB = "Cours_2/PROJET/metrics.db"
ARCHIVES_DB = "Cours_2/PROJET/metrics.old_db"
if os.path.isfile(PATH_DB):
    os.rename(PATH_DB,ARCHIVES_DB)


try:
    while True:
        # DBsql :
        con = sqlite3.connect(PATH_DB)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS stats (time, cpu, ram_total, ram_used, ram_free)")

        # Metriques :
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
        
        # Alimentation de la DB
        cur.execute("INSERT INTO stats VALUES (?,?,?,?,?)",(time_stamp,cpu_usage,mem_total,mem_used,mem_free))
        con.commit()

        # Tempoisation
        time.sleep(5)

        #Print de la DB pour vérifications
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in cur.execute("SELECT time, cpu, ram_total, ram_used, ram_free FROM stats "):
            print ("A",row[0],"votre cpu est à",row[1],"%" ,row[2] ,row[3] ,row[4]  )
    
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
