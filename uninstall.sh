#loc=

sudo rm /etc/default/grub.backuptext
sudo rm /etc/default/grub.backupgraph

echo "Enable default mode"
sudo cp /etc/default/grub.backup /etc/default/grub
sudo update-grub

sudo rm /etc/default/grub.backup
sudo rm /bin/GtT
sudo rm $loc

echo -n "You must restart computer to aplly changes. Do you want do it now?(Y/n): "
read answer
if test $answer == "Y"
	then shutdown -r now
fi
