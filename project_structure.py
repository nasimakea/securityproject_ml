import os

PROJECT_NAME = "networksecurity"

# List of directories to create
directories = [
    ".github/workflows",
    "network_data",
    "notebooks",
    f"{PROJECT_NAME}/components",
    f"{PROJECT_NAME}/constants",
    f"{PROJECT_NAME}/entity",
    f"{PROJECT_NAME}/exception",
    f"{PROJECT_NAME}/logging",
    f"{PROJECT_NAME}/pipeline",
    f"{PROJECT_NAME}/utils",
    f"{PROJECT_NAME}/cloud",
]

# List of files to create
files = [
    "requirements.txt",
    "README.md",
    ".gitignore",
    ".env",
    "Dockerfile",
    "setup.py",
    ".github/workflows/main.yml",
    f"{PROJECT_NAME}/__init__.py",
]

def create_structure():
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass
            print(f"Created file: {file}")

    # Write default .gitignore content
    with open(".gitignore", "w") as f:
        f.write(
            "venv/\n"
            "__pycache__/\n"
            "*.pyc\n"
            ".env\n"
            ".idea/\n"
            ".vscode/\n"
        )

    print("\n✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
