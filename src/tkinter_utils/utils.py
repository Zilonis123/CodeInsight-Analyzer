from tkinter import ttk
import tkinter as tk

from src.tkinter_utils.funcs import search

class App(tk.Tk):
    def __init__(self, title: str, size: tuple[int,int]):
        # setup the app
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)
        
        self.output = Output(self)
        self.input = Input(self)
        
        # run the app
        self.mainloop()
        
        
class Input(ttk.Frame):
    def __init__(self, master: App):
        super().__init__(master)
        
        self.master = master
        
        
        self.create_widgets()
        self.place(x=0, y=0, relwidth=1, relheight=.2)
    
    def create_widgets(self):

        self.entry_string = tk.StringVar()
        entry = ttk.Entry(master=self, textvariable=self.entry_string)
        button = ttk.Button(master=self, text="Search", command=lambda: search(self.master))

        entry.pack(pady=5)
        button.pack()
        
        
class Output(ttk.Frame):
    def __init__(self, master: App):
        super().__init__(master)
        
        self.create_widgets()
        self.place(x=0,rely=.2,relheight=.8, relwidth=1)
        
    def create_widgets(self):
        self.file_output_string = tk.StringVar()
        file_output_label = ttk.Label(master=self, textvariable=self.file_output_string)
        
        self.folder_output_string = tk.StringVar()
        folder_output_label = ttk.Label(master=self, textvariable=self.folder_output_string)
        
        file_output_label.pack(side="left", expand=True, padx=20)
        folder_output_label.pack(side="right", expand=True, padx=20)
    