#!/bin/bash
#Program, which installs GtT in your computer

echo "Welcome in GtT (Graphic to Terminal for linux) program installator"
echo "Copying grub file and raname to grub.backup"
sudo cp /etc/default/grub ./grub.backup

python3 ./edit_grub.py

echo 'Enable default mode' > mode.txt

sudo chmod 755 GtT
sudo cp ./GtT /bin/GtT
sudo cp ./grub.backuptext /etc/default/grub.backuptext
sudo cp ./grub.backupgraph /etc/default/grub.backupgraph
sudo cp ./grub.backup /etc/default/grub.backup
