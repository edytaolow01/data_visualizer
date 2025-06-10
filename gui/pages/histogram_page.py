import tkinter as tk
from tkinter import ttk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from utils.constants import LARGE_FONT, AVAILABLE_PARAMETERS, HISTOGRAMBINSWIDTH, OVERRUNVALUE
from utils.helpers import popup_msg, validate_numeric_input
from data_processor import DataProcessor

class PageThree(tk.Frame):
    """Histogram page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Initialize data processor
        self.data_processor = DataProcessor("Modified_data.txt")
        self.df = self.data_processor.get_data()
        
        # Create widgets
        label = tk.Label(self, text="Histogram", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Start Page",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        # Create combobox for parameter selection
        n = tk.StringVar()
        self.C0 = ttk.Combobox(self, width=10, textvariable=n)
        self.C0['values'] = AVAILABLE_PARAMETERS
        self.C0.pack()
        self.C0.bind("<<ComboboxSelected>>", self.selection)
        
        # Create canvas for controls
        mycanvas = tk.Canvas(self, width=100, height=100)
        mycanvas.pack(side='right')
        
        # Create bin width controls
        self.entry1 = tk.Entry(mycanvas, width=6)
        self.entry1.pack()

        button2 = ttk.Button(mycanvas, text="Set Bin Width",
                            command=self.select_bins_width)
        button2.pack()

        button3 = ttk.Button(mycanvas, text="Reset to Automatic",
                            command=self.automatic_bins_width)
        button3.pack()
        
        # Create overrun controls
        self.entry2 = tk.Entry(mycanvas, width=6)
        self.entry2.pack()
        
        button4 = ttk.Button(mycanvas, text="Set Threshold",
                            command=self.handle_overrun)
        button4.pack()
        
        button5 = ttk.Button(mycanvas, text="Clear Threshold",
                            command=self.delete_overrun)
        button5.pack()

        # Initialize plot attributes
        self.wykres_canvas = None
        self.toolbar = None
        self.selected_param = None

    def select_bins_width(self):
        """Handle bin width input"""
        global HISTOGRAMBINSWIDTH
        val = self.entry1.get()
        if validate_numeric_input(val):
            HISTOGRAMBINSWIDTH = float(val)
            self.create_graph()
        else:
            popup_msg("Podaj cyfrę większą od 0")

    def automatic_bins_width(self):
        """Reset bin width to automatic"""
        global HISTOGRAMBINSWIDTH
        HISTOGRAMBINSWIDTH = None
        self.create_graph()

    def handle_overrun(self):
        """Handle overrun value input"""
        global OVERRUNVALUE
        val = self.entry2.get()
        if validate_numeric_input(val):
            OVERRUNVALUE = float(val)
            self.create_graph()
        else:
            popup_msg("Podaj cyfrę")

    def delete_overrun(self):
        """Reset overrun value"""
        global OVERRUNVALUE
        OVERRUNVALUE = None
        self.create_graph()

    def selection(self, event=None):
        """Handle parameter selection"""
        self.selected_param = self.C0.get()
        self.create_graph()

    def create_graph(self):
        """Create histogram"""
        if not self.selected_param:
            return
            
        # Create figure
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        
        # Create histogram
        if HISTOGRAMBINSWIDTH is not None:
            h = sns.histplot(ax=a, x=self.df[self.selected_param],
                           binwidth=HISTOGRAMBINSWIDTH, stat='percent')
        else:
            h = sns.histplot(ax=a, x=self.df[self.selected_param], stat='percent')
        
        # Add overrun line if specified
        if OVERRUNVALUE is not None:
            a.axvline(x=OVERRUNVALUE, color="r", linestyle="--")
        
        # Set labels
        h.set_ylabel("Percentage [%]", labelpad=20)
        a.set_title(f"Histogram of {self.selected_param}")
        a.set(xlim=(0))
        
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