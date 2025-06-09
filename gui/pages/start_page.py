import tkinter as tk
from tkinter import ttk
from PIL import ImageTk as itk
from PIL import Image

from utils.constants import LARGE_FONT

class StartPage(tk.Frame):
    """Start page of the application"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Add background image
        self.background_image = itk.PhotoImage(Image.open("airplane1.png"))
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Add widgets
        label = tk.Label(self, text="Select plot type", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Line Plot",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = ttk.Button(self, text="Box Plot",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        button3 = ttk.Button(self, text="Histogram",
                            command=lambda: controller.show_frame("PageThree"))
        button3.pack()

        button4 = ttk.Button(self, text="Correlation Matrix",
                            command=lambda: controller.show_frame("PageFour"))
        button4.pack()

        button5 = ttk.Button(self, text="Scatter Plot",
                            command=lambda: controller.show_frame("PageFive"))
        button5.pack() 