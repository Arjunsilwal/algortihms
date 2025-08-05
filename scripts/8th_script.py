import os

folder = "automation_test"

for idx, filename in enumerate(os.listdir(folder)):
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, f"data_{idx}.txt")
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → data_{idx}.txt")