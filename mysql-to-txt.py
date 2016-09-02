from pprint import pprint
from tools import parsing_document_contents
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

txt_dict = {}
asdf = []

# Find INSERT INTO comamnd from the text
for text1 in text:
	for line in re.split(r'(\(\d+\,\d+\,\')', text1):
		if line:
			if line[:1] == "(":
				item_index = re.findall(r'\d+', line[:10])[0]
			else:
				txt_dict[item_index] = line.strip()

# Print the number of Items
print "Number of Items:", len(txt_dict.keys())

# Parsing document_contents
for k, v in txt_dict.iteritems():
	if "<p>" in v:
		print k
		print v[:50]
		print v[-50:]

# Save articles to txt files
for key, value in parsed_document_contents.iteritems():
	for article in value:
		with open(u"{}/{}.txt".format(output_path, article[0]), "w") as F:
			F.write(article[1])

