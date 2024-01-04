import os, sys, json
from tqdm import tqdm
from colorama import Fore, Style

from src.analysis.code_analyzer import *
from src.utils.file_operations import *
from src.analysis.folder_hierarchy import print_folder_hierarchy


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
    else:
        target_directory: str = sys.argv[1]
        
        if not os.path.exists(target_directory):
            print(f"{Fore.RED}Error: Path '{target_directory}' does not exist.{Style.RESET_ALL}")
            
        else:
            # get excluded folders
            file = open("exclude.json")
            excluded: dict = json.load(file)
            excluded_folders: dict = excluded.get("folders", [])
            file.close()

            files: int = count_files(target_directory, )

            print(f"Searching {Fore.GREEN}{files}{Style.RESET_ALL} files")
            file_count: dict = process_directory(target_directory)

            for file_ext, count in file_count.items():
                print(f"{file_ext} found {Fore.GREEN}{count}{Style.RESET_ALL} times")

            print_folder_hierarchy(target_directory, excluded_folders)
