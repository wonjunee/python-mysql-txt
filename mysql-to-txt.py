from pprint import pprint
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

