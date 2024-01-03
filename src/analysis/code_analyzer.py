
from tqdm import tqdm
import json, os

from src.utils.code_analysis_helpers import *


def process_directory(directory: str, excluded={}) -> dict:
    file_extension_count = {}

    excluded_folders: list[str] = excluded.get("folders", [])
    excluded_files: list[str] = excluded.get("files", [])

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