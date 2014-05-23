import os

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".htm") :
    	os.rename(os.path.join(os.getcwd(),filename), os.path.join(os.getcwd(),filename+"l"))
