import os

"""Root directory where all coding folders are stored"""
ROOT = 'Coding'

""" Target category folders """
folders = ["projects", "unfinished", "learning"]

def ensure_folders_exist(root, folders):
    """Create category folders if they do not exist."""
    for folder in folders:
        path = os.path.join(root, folder)
        os.makedirs(path, exist_ok=True)


def get_projects(root, folders):
    """Return a list of project folders to classify."""
    items = os.listdir(root)
    projects = []

    for item in items:
        path = os.path.join(root, item)

        if (
            os.path.isdir(path)
            and item not in folders
            and item != 'proj'
            and not item.startswith(".")
        ):
            projects.append(item)

    return projects

def classify_project(project):
    """Ask user to classify a project and return category."""
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

    return mapping.get(choice)


def move_project(root, project, category):
    """Move project folder into selected category."""
    source = os.path.join(root, project)
    destination = os.path.join(root, category, project)

    if os.path.exists(source):
        os.rename(source, destination)
        print(f"Moved {project} → {category}")
    else:
        print(f"{project} already moved or missing")


# --- Main Execution ---

ensure_folders_exist(ROOT, folders)

projects = get_projects(ROOT, folders)

for project in projects:
    category = classify_project(project)

    if category:
        move_project(ROOT, project, category)
    else:
        print("Invalid choice, skipping...")
