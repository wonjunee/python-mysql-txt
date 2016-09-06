from tools import find_the_something, find_title, save_txt, find_a, remove_bad_chars
from pprint import pprint
<<<<<<< HEAD
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
||||||| merged common ancestors
from tools import parsing_document_contents

# Open the file and load it into a string
text = ""
with open(u"c:/users/wlee/downloads/example.txt","r") as F:
	for line in F:
		line = unicode(line, encoding='utf-8', errors='ignore')
		text+=line.strip()

# Find INSERT INTO comamnd from the text
text = text.split(u"INSERT INTO")

# Parsing document_contents
parsed_document_contents = {}
for i in range(len(text)):
	if i > 0 and i < len(text) - 1:
		parsed_document_contents = parsing_document_contents(text[i], parsed_document_contents)

for key in parsed_text.keys():
	print key
	print "Number of items:", len(parsed_text[key])

# for key, values in parsed_text.iteritems():
# 	value_ind = 0
# 	for value in values:
# 		try:
# 			a = int(value[0].split(",")[0])
# 		except:
# 			print key
# 			print value
# 			print value_ind
# 		value_ind += 1

# Save articles to txt files
import re
for key, value in parsed_text.iteritems():
	folder = "documents"
	for article in value:
		with open(u"c:/users/wlee/downloads/{}/{}.txt".format(folder, article[0]), "w") as F:
			F.write(article[1])
=======
import sys
import re
import os

# Setting default Encoding
reload(sys)
sys.setdefaultencoding("utf8")

##########################################
#				INPUT
##########################################

sql_file_path = u"D:\content\Dump.sql"
output_path = u"./udacity/parsed_documents"
splitted_files = u"splitted_files"

##########################################

dump_files = os.listdir(splitted_files)

# split the large file into smaller files
if len(dump_files) == 0 :
	# Open the file and load it into a string
	i = 0
	with open(sql_file_path,"r") as F:
		for line in F:
			if "INSERT INTO" in line[:50]:
				line = unicode(line, encoding='utf-8', errors='ignore')
				line = line.replace(r"\n","")
				line = line.replace(r"\r","")
				line = line.replace(r'\"','"')
				line = line.replace(r"\'","'")
				line = line.replace("&nbsp", "")
				line = line.replace(";", "")
				with open(u"{}\dump{}.sql".format(splitted_files, i), "w") as F:
					F.write(line.split("VALUES")[1].strip())
				i += 1
	print "Number of splitted files created:", i
	print

# Find "the blah blah" from the line
def find_the_something(num, line):
	pattern = r"the \w+"
	for i in range(num-1):
		pattern += r" \w+"
		max_length = min(1000, len(line))
	titles = re.findall(pattern, line[:max_length])
	if titles:
		return titles[0]
	else:
		return None

# Function that finds a title from a line
def find_title(line):
	# If the content is html tag then find the title
	if r"title=" in line:
		ind = line.find(r"title=")
		line_including_title = line[ind:ind+100]
		for i in range(len(line_including_title)):
			if line_including_title[i] == ">":
				start = i+1
			elif line_including_title[i] == "<":
				# print line
				return line_including_title[start:i]

	# else find the blah blah blah
	for i in range(5,0,-1):
		title = find_the_something(i, line)
		if title:
			return title

	# if none exists from the above
	# then return the first three words
	return " ".join(line[:100].split(" ")[:3])

# Save as txt file
def save_txt(output_path, title, content):
	with open(u"{}/{}.txt".format(output_path, title), "w") as F:
		print "Saving: {}.txt".format(title)
		print "Content:", content[:50]
		F.write(content)

# Decide a value
def find_a(line):
	if re.search(r'\(\d+\,', line[:10]):
		if re.search(r'\(\d+\,', line[:10]).start() == 0:
			return 0
	return 1

# Create a list for titles to avoid duplicates
title_list = []

# iterate over dump_files and parse each of them
count = 0
for file in dump_files:
	with open(r"{}/{}".format(splitted_files,file)) as dump_file:
		for i in dump_file:
			text = i
			break

	parsed_list = re.split(r'(\(\d+\,\d+\,\')', text)
	del text

	sub_count = 0
	for line in parsed_list:
		if line:
			a = find_a(line)

			if a == 0:
				if sub_count > 0:
					title = find_title(content)
					save_txt(output_path, title, content)

				item_index = re.findall(r'\d+', line)[0]
				print item_index
				content = None
				count += 1
				sub_count += 1
			else:
				if content:
					content += line
				else:
					content = line

	title = find_title(content)
	save_txt(output_path, title, content)

print "Number of txt files created:", count
>>>>>>> 85727724b99031f985dec48b97a5a07ab415650f

os.chdir(original_path)