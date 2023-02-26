import re
filename = 'folder1/folder2/file.ext'
print (re.search(r'[.][a-zA-Z]{1,}$', filename))