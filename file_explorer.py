import glob
import os
os.chdir(".")
for file in glob.glob("*.jpg"):
    print(file)
