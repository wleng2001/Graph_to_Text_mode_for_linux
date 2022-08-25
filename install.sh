#!/bin/bash
#Program, which installs GtT in your computer

echo "Welcome in Graphic to Terminal program installator"
echo "Copying grub file and rename to grub.backup"
sudo cp /etc/default/grub ./grub.backup

python3 ./edit_grub.py

sudo cp ./grub.backuptext /etc/default/grub.backuptext
sudo cp ./grub.backupgraph /etc/default/grub.backupgraph
