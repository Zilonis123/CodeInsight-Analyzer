import tkinter as tk
from tkinter import ttk

import os, json
from src.analysis.code_analyzer import *


def search() -> None:
    target_directory: str = entry_string.get()
    
    # reset input and output
    entry_string.set("")
    output_string.set("")
    
    if not os.path.exists(target_directory):
        # path provided doesn't exist
        output_string.set(f"Error: Provided path ({target_directory}) is incorrect!")
        return
    
    file_count: dict = process_directory(target_directory)
    
    output = ""
    for file_ext, count in file_count.items():
        output += f"{file_ext} found {count} times\n"
        
    output_string.set(output)


# get excluded 
file = open("exclude.json")
excluded: dict = json.load(file)
file.close()


window = tk.Tk()
window.title("Code Analyzer")
window.geometry("300x150")


# input
input_frame = ttk.Frame(master=window)
entry_string = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_string)
button = ttk.Button(master=input_frame, text="Search", command=search)

entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack()

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_string)
output_label.pack()

window.mainloop()