import tkinter as tk
from tkinter import ttk
from PIL import ImageTk as itk
from PIL import Image

from .pages.start_page import StartPage
from .pages.line_plot_page import PageOne
from .pages.box_plot_page import PageTwo
from .pages.histogram_page import PageThree
from .pages.correlation_page import PageFour
from .pages.scatter_plot_page import PageFive

from utils.constants import LARGE_FONT

class App(tk.Tk):
    """Main application class"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Create container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Initialize all pages
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("StartPage")
        
    def show_frame(self, cont):
        """Show the selected frame"""
        frame = self.frames[cont]
        frame.tkraise()
        
        # Initialize specific page data if needed
        if cont == "PageThree":
            frame.C0.set("Psi[°]")
            frame.selection()
        if cont == "PageFour":
            frame.RysujHeatMap() 