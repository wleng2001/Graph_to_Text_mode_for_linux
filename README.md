# Graph_to_Text_mode_for_linux
<!-- markdownlint-configure-file { "MD004": { "style": "consistent" } } -->
<!-- markdownlint-disable MD033 -->

## Description

The program automatically change your linux mode from graphical to text (tty) and vice versa.
It's simply program, which is written in bash and python. It copies your grub file and edit it by python. You can use it by command in terminal.

-----

## Instalation

If you want use the program you must check that you have python in version 3. You can do it by write the command in terminal:
### `python3 --version` 
If you get infomration similary to this you can install GtT
### `Python 3.10.4`
Next paste the command to the terminal: 
### `git clone https://github.com/wleng2001/Graph_to_Text_mode_for_linux.git ./GtT`
Write the text in the terminal:
### `cd GtT`
Run installer:
### `sudo bash install.sh`
Installer ask you for password to your linux account, because it edit system file.
Congratulation! You have installed GtT!

-----

## Usage

If you forget how to use program you can write the command in terminal to read about it.
### `GtT -h`
After typing the command you should see the information: 
<a href="help.txt"> help</a>
If you want to change mode to text you should write the text in terminal.
### `sudo GtT -t`
The program ask you for password to your linux account, because it edit system file. After the operating is completed program ask you for restart computer.
If you want to change mode to graphic you should write the text in terminal.
### `sudo GtT -g`
The program ask you for password to your linux account, because it edit system file. After the operating is completed program ask you for restart computer.
If you want to change mode to default you should write the text in terminal. It command show always, because program doesn't advanced yet.
### `sudo GtT -d`
The program ask you for password to your linux account, because it edit system file. After the operating is completed program ask you for restart computer.
If you want to uninstall program you should write the text in terminal.
### `sudo GtT -u`
The program ask you for password to your linux account, because it edit system file. After the operating is completed program ask you for restart computer.

-----
It's my first repository on github and I learn about it.
