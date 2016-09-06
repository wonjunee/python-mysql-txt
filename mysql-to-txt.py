from tools import find_the_something, find_title, save_txt, find_a, remove_bad_chars
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

# sql_file_path = u"D:\content\Dump.sql"
sql_file_path = r"Untitled-6.sql"
# output_path = r"E:\sql"
output_path = r"sql"
# splitted_files = r"D:\content\splitted_files"
splitted_files = r"c:\users\wlee\downloads\splitted_files"

##########################################

# Create a folder for splitted_files
if not os.path.exists(splitted_files):
	os.makedirs(splitted_files)

# split the large file into smaller files
# Open the file and load it into a string
i = 0
subfolder = 0
with open(sql_file_path,"r") as F:
	for line in F:
		if "INSERT INTO" in line[:50]:
			# Create a subfolder if not exists
			if not os.path.exists(r'{}\{}'.format(splitted_files, subfolder)):
				os.makedirs(r'{}\{}'.format(splitted_files, subfolder))

			# Write sql into a subfolder
			with open(u"{}\{}\dump{}.sql".format(splitted_files, subfolder, i), "w") as F:
				F.write(line.split("VALUES")[1].strip())
			i += 1

			if i % 1000 == 0:
				subfolder += 1

print "Number of splitted files created:", i
print "Number of folders created:", subfolder

#------------------------ Writing to txt files -----------------------------
# Set a directory
original_path = os.getcwd()

# change path to folder where txt files will be saved
if not os.path.exists(output_path):
	os.makedirs(output_path)
os.chdir(output_path)

# Create a folder for wrong sql lines
error_files = u"wrong_sql_lines"
if not os.path.exists(error_files):
    os.makedirs(error_files)

# iterate over dump_files and parse each of them
count = 0
subfolder = -1
for path in os.walk(splitted_files):
	if len(path[2]) > 0:
		subfolder += 1
		for file in path[2]:
			with codecs.open(r"{}/{}".format(path[0], file), "r", "utf-8") as dump_file:
				text = dump_file.read()
				text = text.decode("ascii", "ignore")

			# find the end line and split items
			pre_parsed_list = re.split(r'(\(\d+\,\d+\,\')', text)

			del text

			parsed_list = {}

			for line in pre_parsed_list:
				if line:
					if re.search(r'\(\d+\,\d+', line.strip()[:20]):
						key = re.findall(r'\d+', line)[0]
						parsed_list[key] = ""
					else:
						parsed_list[key] += remove_bad_chars(line)

			del pre_parsed_list

			for k, v in parsed_list.iteritems():
				title = find_title(v)
				save_txt(str(subfolder), title, v, count, "{}\{}".format(path[0],file), error_files)
				count += 1

print "Number of txt files created:", count

os.chdir(original_path)