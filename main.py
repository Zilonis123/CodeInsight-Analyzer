import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import os, json
from src.analysis.code_analyzer import *
from src.analysis.folder_hierarchy import build_folder_hierarchy


def count_file_types(target_directory: str):
    def draw_output(file_count: dict) -> None:
        output = ""
        for file_ext, count in file_count.items():
            output += f"{file_ext} found {count} times\n"
        file_output_string.set(output)
   
    file_count: dict = process_directory(target_directory, excluded, draw_output)


def display_folder_hiearchy(target_directory: str):
    hiearchy = build_folder_hierarchy(target_directory, excluded.get("folders", []))
    
    folder_output_string.set(json.dumps(hiearchy, indent=2))

def search() -> None:
    target_directory: str = entry_string.get()
    
    if target_directory == "":
        # nothing provided
        return
    
    # reset input and output
    entry_string.set("")
    file_output_string.set("")
    folder_output_string.set("")
    
    
    if not os.path.exists(target_directory):
        # path provided doesn't exist
        file_output_string.set(f"Error: Provided path ({target_directory}) is incorrect!")
        return

    count_file_types(target_directory)
    display_folder_hiearchy(target_directory)

if __name__ == "__main__":
    # get excluded 
    file = open("exclude.json")
    excluded: dict = json.load(file)
    file.close()


    window = ThemedTk(theme="black")
    window.title("Code Analyzer")
    window.geometry("750x550")
    window.resizable(False, False)
    


    # input
    input_frame = ttk.Frame(master=window)
    entry_string = tk.StringVar()
    entry = ttk.Entry(master=input_frame, textvariable=entry_string)
    button = ttk.Button(master=input_frame, text="Search", command=search)

    entry.pack(side="left", padx=10)
    button.pack(side="left")

    # output
    output_frame = ttk.Frame(master=window)
    file_output_string = tk.StringVar()
    file_output_label = ttk.Label(master=output_frame, textvariable=file_output_string)
    
    folder_output_string = tk.StringVar()
    folder_output_label = ttk.Label(master=output_frame, textvariable=folder_output_string)
    
    file_output_label.pack(side="left")
    folder_output_label.pack(side="right")
    
    
    # layout (grid)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=2)
    window.rowconfigure(0, weight=1)

    input_frame.grid(row=0, column=0, sticky="nesw")
    output_frame.grid(row=0, column=1, sticky="nesw")

    window.mainloop()