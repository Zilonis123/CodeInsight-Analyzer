import os


def count_files(directory: str) -> int:
    total_files: int = sum([len(files) for _, _, files in os.walk(directory)])
    return total_files