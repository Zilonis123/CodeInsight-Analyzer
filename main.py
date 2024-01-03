import os, sys, magic, json

def is_text_file(file_path):
    # check if a file is a text file
    mime = magic.Magic()
    file_type = mime.from_file(file_path)

    return "text" in file_type.lower()

def process_directory(directory: str) -> dict:
    file_extension_count = {}

    # get excluded folders
    file = open("exclude.json")
    excluded = json.load(file)
    excluded_folders: list[str] = excluded.get("folders", [])

    file.close()

    for root, dirs, files in os.walk(directory):

        if any(folder in root for folder in excluded_folders):
            continue  # Skip the entire subdirectory


        for file in files:
            file_path = os.path.join(root, file)
            
            # Get the file extension
            _, file_extension = os.path.splitext(file)

            if not file_extension.isspace() and is_text_file(file_path):
                file_extension_count[file_extension] = file_extension_count.get(file_extension, 0) + 1

    return file_extension_count

    # Display the results
    for extension, count in file_extension_count.items():
        print(f"{extension}: {count} file(s)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        target_directory: str = sys.argv[1]
        
        file_count: dict = process_directory(target_directory)

        for file_ext, count in file_count.items():
            print(f"{file_ext} found {count} times")
