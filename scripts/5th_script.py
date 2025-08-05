import os

if not os.path.exists("automation_test"):
    os.mkdir("automation_test")

# directory = "automated"
# Define the file path
# file_path = os.path.join(directory, "hello.txt")
# Create the directory if it doesn't exist
# exist_ok=True prevents an error if the folder is already there
# os.makedirs(directory, exist_ok=True)


with open("automation_test/hello.txt", "w") as file:
    file.write("Automation is fun!")

files = os.listdir("./automation_test")
print("Files in automation_test folder:", files)
