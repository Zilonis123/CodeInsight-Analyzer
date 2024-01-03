import os, sys, magic, json
from tqdm import tqdm
from colorama import Fore, Style

def is_text_file(file_path):
    # check if a file is a text file
    mime = magic.Magic()
    file_type = mime.from_file(file_path)

    return "text" in file_type.lower()

def count_files(directory):
    total_files = sum([len(files) for _, _, files in os.walk(directory)])
    return total_files


def process_directory(directory: str) -> dict:
    file_extension_count = {}

    # get excluded folders
    file = open("exclude.json")
    excluded = json.load(file)
    excluded_folders: list[str] = excluded.get("folders", [])
    excluded_files: list[str] = excluded.get("files", [])

    file.close()

    for root, dirs, files in tqdm(os.walk(directory), desc="Processing", unit="files", leave=True):

        if any(folder in root for folder in excluded_folders):
            continue  # Skip the entire subdirectory


        for file in files:
            file_path = os.path.join(root, file)
            
            # Get the file extension
            file_name, file_extension = os.path.splitext(file)

            if f"{file_name}{file_extension}" in excluded_files:
                continue

            if file_extension != "" and is_text_file(file_path):
                file_extension_count[file_extension] = file_extension_count.get(file_extension, 0) + 1

    return file_extension_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
    else:
        target_directory: str = sys.argv[1]

        files = count_files(target_directory)
        print(f"Searching {Fore.GREEN}{files}{Style.RESET_ALL} files")
        file_count: dict = process_directory(target_directory)

        for file_ext, count in file_count.items():
            print(f"{file_ext} found {Fore.GREEN}{count}{Style.RESET_ALL} times")
