""" Parse sql script into dictionary """

# Parsing document_contents database
def parsing_document_contents(text, parsed_document_contents):
	if u'document_contents' not in text[:50]:
		return parsed_document_contents

	text = text.split(u"\'")
	for i in text:
		if u'VALUES' in i:
			table = i.split(u'VALUES')[0]
			table = table[2:len(table)-2]
			ID = i.split(u'(')[-1][:-1]
			content = ""
			if table not in parsed_document_contents.keys():
				parsed_document_contents[table] = []
		elif u"),(" in i:
			if i.split(u'),(')[-1][0].isdigit():
				parsed_document_contents[table].append([ID, content])
				ID = i.split(u'),(')[-1][:-1]
				content = ""
		else:
			content += i
	return parsed_document_contents