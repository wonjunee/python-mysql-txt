from pprint import pprint
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

