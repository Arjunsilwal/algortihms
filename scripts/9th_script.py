import os

for root, dirs, files in os.walk("automation_test"):
    for file in files:
        if file.endswith(".txt"):
            print("Found TXT file:", os.path.join(root, file))





# using glob for patter matching
import glob

# Find all .txt files in folder
txt_files = glob.glob("automation_test/*.txt")
print("TXT files:", txt_files)

