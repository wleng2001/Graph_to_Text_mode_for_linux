#!/bin/bash

echo 'Enable graphic mode'
sudo cp /etc/default/grub.backupgraph /etc/default/grub
sudo update-grub
sudo systemctl set-default graphical.target
echo -n "You must restart computer to aplly changes. Do you want do it now?(Y/n): "
read answer
if test $answer == "Y"
then shutdown -r now
fi
