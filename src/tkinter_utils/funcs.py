import os, json

from src.analysis.code_analyzer import process_directory
from src.analysis.folder_hierarchy import build_folder_hierarchy

def display_folder_hiearchy(target_directory: str, folder_output):
    # get excluded 
    file = open("exclude.json")
    excluded: dict = json.load(file)
    
    hiearchy = build_folder_hierarchy(target_directory, excluded.get("folders", []))
    
    folder_output.set(json.dumps(hiearchy, indent=2))


def count_file_types(target_directory: str, file_output_string):
    def draw_output(file_count: dict) -> None:
        output = ""
        for file_ext, count in file_count.items():
            output += f"{file_ext} found {count} times\n"
        file_output_string.set(output)
        
        
    file = open("exclude.json")
    excluded: dict = json.load(file)
   
    file_count: dict = process_directory(target_directory, excluded, draw_output)


def search(master) -> None:
    target_directory: str = master.input.entry_string.get()
    
    if target_directory == "":
        # nothing provided
        return
    
    # reset input and output
    master.input.entry_string.set("")
    
    output = master.output
    
    folder_output = output.folder_output_string
    file_output = output.file_output_string
    
    output.file_output_string.set("")
    folder_output.set("")
    
    
    if not os.path.exists(target_directory):
        # path provided doesn't exist
        output.file_output_string.set(f"Error: Provided path ({target_directory}) is incorrect!")
        return

    count_file_types(target_directory, file_output)
    display_folder_hiearchy(target_directory, folder_output)