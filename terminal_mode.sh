#!/bin/bash

echo 'Enabling text mode'
sudo cp /etc/default/grub.backuptext /etc/default/grub
sudo update-grub
sudo systemctl set-default multi-user.target
echo -n "You must restart computer to aplly changes. Do you want do it now?(Y/n): "
read answer
if test $answer == "Y"
then shutdown -r now
fi
