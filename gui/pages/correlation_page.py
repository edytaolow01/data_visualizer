import tkinter as tk
from tkinter import ttk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

from utils.constants import LARGE_FONT
from data_processor import DataProcessor

class PageFour(tk.Frame):
    """Correlation matrix page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Initialize data processor
        self.data_processor = DataProcessor("Modified_data.txt")
        self.df = self.data_processor.get_data()
        
        # Create widgets
        label = tk.Label(self, text="Correlation Matrix", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Start Page",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        # Initialize plot attributes
        self.wykres_canvas = None
        self.toolbar = None

    def RysujHeatMap(self):
        """Create correlation matrix heatmap"""
        # Create figure
        f = Figure(figsize=(10, 8), dpi=100)
        a = f.add_subplot(111)
        
        # Calculate correlation matrix (excluding time column)
        numeric_df = self.df.select_dtypes(include=[np.number])
        dane_hx = numeric_df.corr()
        
        # Create heatmap
        heatmap = sns.heatmap(dane_hx, 
                            annot=True, 
                            cmap='coolwarm',
                            center=0,
                            fmt='.2f',
                            square=True,
                            linewidths=0.5,
                            cbar_kws={'shrink': .8},
                            ax=a)
        
        # Rotate labels for better readability
        heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, ha='right')
        heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0)
        
        # Adjust layout
        f.tight_layout()
        
        # Set title
        a.set_title("Parameter Correlation Matrix", pad=20)
        
        # Update canvas
        if self.wykres_canvas:
            self.wykres_canvas.get_tk_widget().destroy()
        if self.toolbar:
            self.toolbar.pack_forget()
            
        self.wykres_canvas = FigureCanvasTkAgg(f, self)
        self.wykres_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.toolbar = NavigationToolbar2Tk(self.wykres_canvas, self)
        self.toolbar.update()
        self.wykres_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True) 