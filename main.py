import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import os, json

from src.tkinter_utils.utils import App

if __name__ == "__main__":
    # get excluded 
    file = open("exclude.json")
    excluded: dict = json.load(file)
    file.close()

    App("Analyzer", (650, 550))