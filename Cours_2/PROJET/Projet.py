import psutil

disk = str(psutil.disk_usage("/System/Volumes/Data"))
disk = disk.replace(",","=")
disk = disk.replace(")","")
disk = disk.split("=")
print(disk)

total_disk = disk[1].split("=")
total_disk = total_disk[0]
total_disk = round(int(total_disk)/1024**3, ndigits=1)
print(total_disk,"Go au total")

used_disk = disk[3].split("=")
used_disk = used_disk[0]
used_disk = round(int(used_disk)/1024**3, ndigits=1)
print(used_disk,"Go Used")

free_disk = disk[5].split("=")
free_disk = free_disk[0]
free_disk = round(int(free_disk)/1024**3, ndigits=1)
print(free_disk, "Go free")

percent_disk = disk[7].split("=")
percent_disk = percent_disk[0]
print(percent_disk,"%")