# Zakomentowanie tego tekstu: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" wyłącza ekran startowy i końcowy
# Zamiana GRUB_CMDLINE_LINUX="" na GRUB_CMDLINE_LINUX="text" uruchomi linux w trybie tekstowym
#  Odkomentowanie: GRUB_TERMINAL=console wyłączy graficzny terminal przez co stanie się on czarno-biały

import os

text_to_change=['GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"','GRUB_CMDLINE_LINUX=""','#GRUB_TERMINAL="console"','GRUB_CMDLINE_LINUX_DEFAULT="quiet"']
changed_text=['#GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"','GRUB_CMDLINE_LINUX="text"','GRUB_TERMINAL="console"','#GRUB_CMDLINE_LINUX_DEFAULT="quiet"']
file_name="grub.backup"
text_file_name="grub.backuptext"
graph_file_name="grub.backupgraph"
program_file_name="GtT"
text_mode=True
text_for_user="#The file was edited by GtT\n#You can read more on my github: https://github.com/wleng2001/Graph_to_Text_mode_for_linux\n"

def read_file(file_name):
	file=open(file_name)
	try:
		text=file.readlines()
	finally:
		file.close()
		return text

def find_text_in_list(search_text, analyze_text):
	for i in analyze_text:
		if search_text in i:
			return True
	return False

def replace_text(text, search_text, new_text):
	if search_text in text:
		text=text.replace(search_text, new_text)
		return text
	else: return text

def edit_file(table, search_text, replaced_text):
	new_table=[]
	for i in table:
		new_table.append(replace_text(i,search_text,replaced_text))
	return new_table

def edit_more(table, new_file_name, table_to_change, table_changed,):
	new_file=open(new_file_name,'w')
	new_file.write(text_for_user)
	new_table=table
	for i in range(len(table_to_change)):
		new_table=edit_file(new_table,table_to_change[i],table_changed[i])

	for i in new_table:
		new_file.write(i)
	new_file.close()

def copy_file(table,file_name, head=""):
        file=open(file_name,'w')
        file.write(head)
        for i in table:
                file.write(i)
        file.close()
#-----------------------------------------------------------------------------------------------------
print("Checking actually mode")
grub_text=read_file(file_name)
if find_text_in_list(text_to_change[1], grub_text):
	print("You're in graphical mode.")
	text_mode=False
else:
	print("You're in text mode.")
	text_mode=True

print(f"Start editing {file_name} file")
if text_mode==False:
	print("Creating text file.")
	edit_more(grub_text, text_file_name, text_to_change, changed_text)
	print("Creating graph file.")
	copy_file(grub_text,graph_file_name, text_for_user)

if text_mode==True:
	print("Creating graph file.")
	edit_more(grub_text, graph_file_name, changed_text, text_to_change)
	print("Creating text file.")
	copy_file(grub_text,text_file_name, text_for_user)

GtT_text=edit_file(read_file(program_file_name),"#loc=",'loc="'+os.getcwd()+'/"') #add iformation of help.txt  localization
copy_file(GtT_text,program_file_name)

uninstall_text=edit_file(read_file("uninstall.sh"),"#loc=",'loc="'+os.getcwd()+'/"')
copy_file(uninstall_text,"uninstall.sh")

print(f"End editing {file_name} file")
