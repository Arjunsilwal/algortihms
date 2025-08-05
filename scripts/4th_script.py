import os

# Create/write to a file

with open("example.txt", "w") as file:
    file.write("Hello, scripting world!")


# Delete a file
os.remove("example.txt")
print("File deleted!")