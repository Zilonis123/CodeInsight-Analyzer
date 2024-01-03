import os, sys, json
from tqdm import tqdm
from colorama import Fore, Style

from src.analysis.code_analyzer import *
from src.utils.file_operations import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
    else:
        target_directory: str = sys.argv[1]

        # get excluded folders
        file = open("exclude.json")
        excluded: dict = json.load(file)
        file.close()

        files: int = count_files(target_directory, excluded.get("folders", []))

        print(f"Searching {Fore.GREEN}{files}{Style.RESET_ALL} files")
        file_count: dict = process_directory(target_directory)

        for file_ext, count in file_count.items():
            print(f"{file_ext} found {Fore.GREEN}{count}{Style.RESET_ALL} times")
