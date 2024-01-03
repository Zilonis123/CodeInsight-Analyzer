import os


def count_files(directory: str, excluded_folders=[]) -> int:
    total_files: int = sum(
        [len(files) for root, dirs, files in os.walk(directory) if not any(folder in root for folder in excluded_folders)]
    )
    return total_files