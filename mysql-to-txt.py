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
			line = line.replace(r"\n","")
			line = line.replace(r"\r","")
			line = line.replace(r'\"','"')
			line = line.replace(r"\'","'")
			line = line.replace("&nbsp", "")
			line = line.replace(";", "")
			text.append(line.split("VALUES")[1].strip())

# Function that finds a title from a line
def find_title(line):
	if r"title=" in line:
		ind = line.find(r"title=")
		line_including_title = line[ind:ind+100]
		for i in range(len(line_including_title)):
			if line_including_title[i] == ">":
				start = i+1
			elif line_including_title[i] == "<":
				# print line
				return line_including_title[start:i]
	titles = re.findall(r'the \w+', line)

	for title in titles:
		if len(title)>6:
			return title
	return None

# Create a list for titles to avoid duplicates
title_list = []

# Find INSERT INTO comamnd from the text
count = 0
for text1 in text:
	for line in re.split(r'(\(\d+\,\d+\,\')', text1):
		if line:
			if re.search(r'\(\d+\,', line[:6]):
				a= 0
			else:
				a = 1

			if a == 0:
				if count > 0:
					title = find_title(content)
					if title:
						if title in title_list:
							title += item_index
						else:
							title_list.append(title)
					else:
						title = item_index

					# Save as a txt file
					with open(u"{}/{}.txt".format(output_path, title), "w") as F:
						print "\nSaving {}".format(title)
						print "Content:", content[:50]
						F.write(content)
				item_index = re.findall(r'\d+', line)[0]
				content = None
				count += 1
			else:
				if content:
					content += line.strip()
				else:
					content = line.strip()

print "Number of txt files created:", count

