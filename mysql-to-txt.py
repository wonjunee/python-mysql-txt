from pprint import pprint
from tools import parsing_document_contents

##########################################
#				INPUT
##########################################

sql_file_path = u"../example.txt"
output_path = u"../parsed_documents"

##########################################
# Open the file and load it into a string
text = ""
with open(sql_file_path,"r") as F:
	for line in F:
		line = unicode(line, encoding='utf-8', errors='ignore')
		text+=line.strip()

# Find INSERT INTO comamnd from the text
text = text.split(u"INSERT INTO")

# Parsing document_contents
parsed_document_contents = {}
for i in range(len(text)):
	parsed_document_contents = parsing_document_contents(text[i], parsed_document_contents)

# Print the number of Items
for key in parsed_document_contents.keys():
	print key
	print "Number of items:", len(parsed_document_contents[key])

# Save articles to txt files
import re
for key, value in parsed_document_contents.iteritems():
	for article in value:
		with open(u"{}/{}.txt".format(output_path, article[0]), "w") as F:
			F.write(article[1])

