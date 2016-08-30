# Parse sql script into dictionary

# Parsing document_contents database
def parsing_document_contents(text, parsed_document_contents):
	text = text.split(u"\'")
	for i in text:
		if u'VALUES' in i:
			table = i.split(u'VALUES')[0]
			table = table[2:len(table)-2]
			ID = i.split(u'(')[-1][:-1]
			content = ""
			if table not in parsed_text.keys():
				parsed_document_contents[table] = []
		elif u"),(" in i:
			if i.split(u'),(')[-1][0].isdigit():
				parsed_document_contents[table].append([ID, content])
				ID = i.split(u'),(')[-1][:-1]
				content = ""
		else:
			content += i
	return parsed_document_contents

"""
	(586611,
		'Voodoo in Haitian Society',
		'voodoo-haitian-society',
		336,1,1,1,
		'Haiti,United States,
		West Africa,
		2010 Haiti earthquake,Dominican Republic',
		0,
		'active',
		'WW',
		209158,
		'Unpublished',
		0
		),
	(586612,
		'kazakh',
		'kazakh',
		1828,7,1,4,
		'United States,China,
		Christian values,
		Working class,
		Asia-Pacific Economic Cooperation',
		0,
		'active',
		'WW',
		209159,
		'Unpublished',
		0)
"""