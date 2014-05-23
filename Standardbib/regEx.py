import re

f = open("htmlFile" ,"r+")
a = re.sub("<[^>]*>", "", f.read())
f.seek(0)
f.write(a)
f.truncate()
