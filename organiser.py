import os
# Root directory where all coding folders are stored
ROOT = 'Coding'

# Target category folders
folders = ["projects", "unfinished", "learning"]

# Name of this script's directory (not currently used, but useful for future improvements)
SCRIPT_DIR = os.path.basename(os.path.dirname(__file__))
# Ensure all category folders exist (create them if missing)
for folder in folders:
    path = os.path.join(ROOT, folder)
    os.makedirs(path, exist_ok=True)

# Get all items inside the root directory
items = os.listdir(ROOT)
projects = []

# Filter only relevant project folders
for item in items:
    path = os.path.join(ROOT, item)
    
    if (
        os.path.isdir(path) # only include folders (not files)
        and item not in folders  # exclude category folders
        and item != 'proj'  # exclude specific folder (custom rule)
        and not item.startswith(".") # ignore hidden/system folders
    ):
        projects.append(item)

for project in projects:

    print(f"\nProject found: {project}")

    print("Choose category:")
    print("1 - projects")
    print("2 - unfinished")
    print("3 - learning")

    choice = input("Enter number: ")

     # Map user input to folder names
    mapping = {
        "1": "projects",
        "2": "unfinished",
        "3": "learning"
    }

    category = mapping.get(choice)

    if category:
        source = os.path.join(ROOT, project)
        destination = os.path.join(ROOT, category, project)
          
        # Move the folder if it still exists
        if os.path.exists(source):
            os.rename(source, destination)
            print(f"Moved {project} → {category}")
        else:
            print(f"{project} already moved or missing")
    else:
        print("Invalid choice, skipping...")

