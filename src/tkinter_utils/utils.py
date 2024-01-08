from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk

from src.tkinter_utils.funcs import search

class App(ThemedTk):
    def __init__(self, title: str, size: tuple[int,int]):
        # setup the app
        super().__init__(theme="black")
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)
    
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)
        
        self.output = Output(self)
        self.input = Input(self)
        
        # run the app
        self.mainloop()
        
        
class Input(ttk.Frame):
    def __init__(self, master: App):
        super().__init__(master)
        
        self.master = master
        
        
        self.create_widgets()
        self.grid(row=0, column=0, sticky="nesw")
    
    def create_widgets(self):
        
        

        self.entry_string = tk.StringVar()
        entry = ttk.Entry(master=self, textvariable=self.entry_string)
        button = ttk.Button(master=self, text="Search", command=lambda: search(self.master))

        entry.pack(side="left", padx=10)
        button.pack(side="left")
        
        
class Output(ttk.Frame):
    def __init__(self, master: App):
        super().__init__(master)
        
        self.create_widgets()
        self.grid(row=0, column=1, sticky="nesw")
        
    def create_widgets(self):
        self.file_output_string = tk.StringVar()
        file_output_label = ttk.Label(master=self, textvariable=self.file_output_string, font="Anton")
        
        self.folder_output_string = tk.StringVar()
        folder_output_label = ttk.Label(master=self, textvariable=self.folder_output_string)
        
        file_output_label.pack(side="left")
        folder_output_label.pack(side="right")
    