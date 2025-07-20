import os

def create_directory_structure(base_path):
    """
    Creates the specified directory structure.

    Args:
        base_path (str): The root directory where the structure will be created.
    """
    
    # Define the main directory structure
    dirs = {
        "DeezContentEngine": {
            "campaigns": {
                "teamrocket": ["overlays", "scripts", "promos", "json"],
                "beachday": ["overlays", "scripts", "promos", "json"],
                "campfire": ["overlays", "scripts", "promos", "json"],
                "professorbinder": ["overlays", "scripts", "promos", "json"],
                "darklab": ["overlays", "scripts", "promos", "json"],
            },
            "characters": ["raw", "processed", "poses"],
            "cards": ["raw_scans", "cropped", "processed", "overlays"],
            "environments": ["backgrounds", "midgrounds", "foregrounds", "slots", "scenes"],
            "overlays": ["json", "templates", "preview_renders"],
            "voiceovers": ["raw", "processed"],
            "soundfx": ["ambient", "effects", "licensed"],
            "scripts": ["vo", "captions", "prompts"],
            "generated": ["images", "videos", "cards", "overlays", "thumbnails"],
            "final_outputs": ["ready_to_publish", "archive"],
            "naming": [],  # Files will be created separately
            "docs": []     # Files will be created separately
        }
    }

    # Define files to be created
    files = {
        "DeezContentEngine/naming": ["NamingConventions.md", "NamingConventions.json"],
        "DeezContentEngine/docs": ["ContentMap.md"]
    }

    def create_dirs(current_path, structure):
        for key, value in structure.items():
            path = os.path.join(current_path, key)
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")

            if isinstance(value, dict):
                create_dirs(path, value)
            elif isinstance(value, list):
                for sub_dir in value:
                    os.makedirs(os.path.join(path, sub_dir), exist_ok=True)
                    print(f"Created directory: {os.path.join(path, sub_dir)}")

    # Start creating directories
    create_dirs(base_path, dirs)

    # Create specified files
    for dir_path, file_list in files.items():
        for file_name in file_list:
            file_path = os.path.join(base_path, dir_path, file_name)
            with open(file_path, 'w') as f:
                pass # Create an empty file
            print(f"Created file: {file_path}")

# Set the base path for your project.
# It's recommended to set this to your desktop for easy access,
# but you can change it to any desired location.
# Example for macOS desktop: os.path.expanduser("~/Desktop")
# Example for current directory: os.getcwd()
base_directory_path = os.path.expanduser("~/Desktop")

if __name__ == "__main__":
    print(f"Starting to create directory structure under: {base_directory_path}")
    create_directory_structure(base_directory_path)
    print("\nDirectory structure creation complete!")
    print(f"You can find your new 'DeezContentEngine' folder at: {os.path.join(base_directory_path, 'DeezContentEngine')}")
