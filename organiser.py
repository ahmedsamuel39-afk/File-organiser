import os

ROOT = 'Coding'


folders = ["projects", "unfinished", "learning"]

SCRIPT_DIR = os.path.basename(os.path.dirname(__file__))

for folder in folders:
    path = os.path.join(ROOT, folder)
    os.makedirs(path, exist_ok=True)

items = os.listdir(ROOT)
projects = []

for item in items:
    path = os.path.join(ROOT, item)
    
    if (
        os.path.isdir(path)
        and item not in folders
        and item != 'proj'
        and not item.startswith(".")
    ):
        projects.append(item)

for project in projects:

    print(f"\nProject found: {project}")

    print("Choose category:")
    print("1 - projects")
    print("2 - unfinished")
    print("3 - learning")

    choice = input("Enter number: ")

    mapping = {
        "1": "projects",
        "2": "unfinished",
        "3": "learning"
    }

    category = mapping.get(choice)

    if category:
        source = os.path.join(ROOT, project)
        destination = os.path.join(ROOT, category, project)

        if os.path.exists(source):
            os.rename(source, destination)
            print(f"Moved {project} → {category}")
        else:
            print(f"{project} already moved or missing")
    else:
        print("Invalid choice, skipping...")

