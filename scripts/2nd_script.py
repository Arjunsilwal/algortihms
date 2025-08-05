import os

# Create a folder
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("folder created")

# Remove a folder (must be empty)
os.rmdir("new_folder")
print("folder deleted")