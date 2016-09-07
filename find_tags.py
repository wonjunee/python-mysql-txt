from tools import find_the_something, find_title, save_txt, remove_bad_chars, find_tags_text
from pprint import pprint
import sys
import re
import os
import codecs

# add the following line in c:/users/user/AppData/Roaming/Sublime Text 2/Packages/Python/Python.sublime_build
# "encoding": "cp852"

# Setting default Encoding
reload(sys)
sys.setdefaultencoding("utf8")

##########################################
#				INPUT
##########################################

# output_path = r"E:\sql"
output_path = r"sql"

##########################################

#------------------------ Find tags for each text file -----------------------------
# Set a directory
original_path = os.getcwd()

os.chdir(output_path)

# Create a folder for wrong sql lines
error_files = u"wrong_sql_tags"
if not os.path.exists(error_files):
    os.makedirs(error_files)

# iterate over dump_files and parse each of them
count = 0
subfolder = -1
for path in os.walk("."):
	if len(path[2]) > 0 and re.search("wrong", path[0]) == None:
		for filename in path[2]:
			if filename[-8:] != "_tag.txt":
				filepath = r"{}\{}".format(path[0], filename)
				with open(filepath) as F:
					text = F.read()
				try:
					tags = find_tags_text(text)
					with open(r"{}\{}_tag.txt".format(path[0], filename.split(".")[0]), "w") as F:
						F.write(tags)
					sys.stdout.write("{} saved successfully.\n".format(filepath))
				except:
					sys.stdout.write("ERROR OCCURS!!!! {}\n".format(filepath))
					os.rename(filepath, r"{}\{}".format(error_files, filename))

os.chdir(original_path)