# Label; MountPoint; TotalSize (MB); Used (%)
partitions = [
"System;/;50000;85",
"Data;/home;150000;40",
"Cache;/tmp;5000;10",
"Backup;/mnt/backup;500000;92",
"USB-Drive;/media/usb;16000;0",
"Logs;/var/log;10000;95",
"Database;/var/lib/mysql;80000;70",
"Shared;/mnt/shared;200000;15",
"Win-System;/mnt/win;100000;90",
"Recovery;/recovery;2000;98"
]

mount_input = input("Ievadi montējuma punktu: ")

found = False

for p in partitions:
    label, mount, total_size, used = p.split(";")
    
    if mount == mount_input:
        print("Atrasts Label:", label)
        found = True
        break
    
    if not found:
        print("Nav atrasts")