"""
Create sql lines from txt files
"""
import re
import os
import sys

# Setting default Encoding
reload(sys)
sys.setdefaultencoding("utf8")

# Path
file_path = r"files"
# Number of files in one insert line
group_num = 100

saved_path = os.getcwd()

# change path
os.chdir(file_path)

# Getting files
files = os.listdir(".")

error_files = u"..\check_files"
if not os.path.exists(error_files):
    os.makedirs(error_files)

def parse_content(content):
	content = content.strip()
	for i in range(1,min(5,len(content))):
		if content[-i] == u',' or content[-1] == u";":
			if content[-i-2:-i] == u"')":
				content = content[:len(content)-i-2]
				return content.strip()
	return content

# create a sql format
def create_sql_insert_line(ind, content):
	content = parse_content(content)
	insert_line = u"({},{},'{}')".format(ind, ind, content)
	return insert_line

# sys.stdout.write(u"INSERT INTO document_contents VALUES ")

# write a sql line for a single txt
def write_sql_from_txt(file, ind):
	try:
		with open(u"{}".format(file_path,file)) as F:
			text = F.read()
			sys.stdout.write(create_sql_insert_line(ind, text))
			ind += 1
	except:
		os.rename("{}\{}".format(error_files, ))
	return ind

# write a entire sql line from a group of txt files
def write_sql_from_files(file_path, files, ind):
	# write the first line of sql
	sys.stdout.write(u"INSERT INTO document_contents VALUES ")

	# write insert lines
	for file_index in range(len(files)):
		ind = write_sql_from_txt(file_path, files[file_index], ind)
		if file_index < len(files) - 1:
			sys.stdout.write(u',')
		else:
			sys.stdout.write(u';')
	# write a linebreak
	sys.stdout.write(u'\n')

	return ind

# grouping files
ind = 0
for file_index in range(len(files)):
	group_count = file_index % group_num
	if group_count == 0:
		sub_files = []

	sub_files.append(files[file_index])

	if file_index % group_num == group_num - 1:
		ind = write_sql_from_files(file_path, sub_files, ind)

	# At the end of the file write down the last sql lines
	if file_index == len(files) - 1:
		ind = write_sql_from_files(file_path, sub_files, ind)		