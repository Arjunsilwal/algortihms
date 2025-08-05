import os

files = os.listdir(".")  # "." means current folder
print("Files in current folder:", files)

files2 = os.listdir("..")
print("Files in main folder:", files2)