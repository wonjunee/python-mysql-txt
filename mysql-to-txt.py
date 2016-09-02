from pprint import pprint
import sys
import re

# Setting default Encoding
reload(sys)
sys.setdefaultencoding("utf8")

##########################################
#				INPUT
##########################################

sql_file_path = u"../Untitled-6.sql"
output_path = u"../parsed_documents"

##########################################

# Open the file and load it into a string
text = []
with open(sql_file_path,"r") as F:
	for line in F:
		if "INSERT INTO" in line[:50]:
			line = unicode(line, encoding='utf-8', errors='ignore')
			text.append(line.split("VALUES")[1].strip())

# Create an empty dictionary
txt_dict = {}

# Find INSERT INTO comamnd from the text
for text1 in text:
	for line in re.split(r'(\(\d+\,\d+\,\')', text1):
		if line:
			if line[:1] == "(":
				item_index = re.findall(r'\d+', line)[0]
			else:
				txt_dict[item_index] = line.strip()

# Deleting text
del text

# Print the number of Items
print "Number of Items:", len(txt_dict.keys())

# Function that finds a title from a line
def find_title(line):
	for i in range(len(line)):
		if line[i] == ">":
			start = i+1
		elif line[i] == "<":
			# print line
			return line[start:i]
	return None

parsed_document_dict = {}

# Parsing document_contents
for k, v in txt_dict.iteritems():
	if r"title=" in v:
		ind = v.find(r"title=")
		title = find_title(v[ind:ind+100])
		if title:
			if title in parsed_document_dict.keys():
				parsed_document_dict["{}-{}".format(title,k)] = v
			else:
				parsed_document_dict[title] = v
			# print title
		else:
			parsed_document_dict[k] = v
	else:
		parsed_document_dict[k] = v

# Deleting txt_dict
del txt_dict

# Save articles to txt files
count = 0
for key, value in parsed_document_dict.iteritems():
	with open(u"{}/{}.txt".format(output_path, key), "w") as F:
		F.write(value)
		count += 1

print "Number of txt files created:", count

