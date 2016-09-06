""" Tools to Parse sql script into dictionary """
import re
import os
import random

def remove_bad_chars(line):
	line = line.replace(r'\r','').replace(r'\n',' ').replace(r'&nbsp',' ').replace(r';','').replace("&quot", "")
	line = re.sub(r'\\', '', line)
	line = re.sub(r'\s+', ' ', line)
	line = line.strip()
	return line

def remove_white_from_title(title):
	title = re.sub(r'[\n\r]', '', title)
	title = re.sub(r'&nbsp', '', title)
	title = re.sub(r'\s+', ' ', title)
	title = title.strip()
	return title

# Find "the blah blah" from the line
def find_the_something(num, line):
	# make pattern "the something something"
	pattern = r"the \w+"
	for i in range(num-1):
		pattern += r" \w+"

	max_length = min(1000, len(line))

	if max_length == 1000:
		line = " ".join(line[:1000].split(" ")[:-1])
		titles = re.findall(pattern, line)
	else:
		titles = re.findall(pattern, line[:max_length])

	if titles:
		return remove_white_from_title(titles[0])
	else:
		return None

def find_title_html(line):
	line = re.sub(r"<([^<]*)>", '', line)
	line = " ".join(re.findall(r'[a-zA-Z]+', line)[:10])
	return line

def find_title(line):
	if line:
		if "<p>" in line:
			return find_title_html(line)
		line = " ".join(re.findall(r'[a-zA-Z]+', line)[:10])
		return line
	return "Title {}".format(random.random())

# Save as txt file
def save_txt(output_path, title, content, count, file, error_files):
	title = remove_bad_chars(title)
	if not os.path.exists(output_path):
		os.makedirs(output_path)

	try:
		with open(r"{}\{}.txt".format(output_path, title), "w") as F:
			print file
			print "{}\t- Saving: {}.txt".format(count, title)
			print "\t  Content:", content[:50]
			F.write(content)
	except:
		
		print "error occurs:", file
		print title
		title = random.random()
		print file
		print "\t  Content:", content[:50]
		with open(r"{}\{}.txt".format(output_path, title), "w") as F:
			print file
			print "{}\t- Saving: {}.txt".format(count, title)
			print "\t  Content:", content[:50]
			F.write(content)
# Decide a value
def find_a(line):
	if re.search(r'\(\d+\,', line[:10]):
		if re.search(r'\(\d+\,', line[:10]).start() < 5:
			return 0
	return 1