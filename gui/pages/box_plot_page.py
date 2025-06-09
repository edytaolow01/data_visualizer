import tkinter as tk
from tkinter import ttk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from utils.constants import LARGE_FONT, AVAILABLE_PARAMETERS, OVERRUNVALUE
from utils.helpers import popup_msg, validate_numeric_input
from data_processor import DataProcessor

class PageTwo(tk.Frame):
    """Box plot page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Initialize data processor
        self.data_processor = DataProcessor("Dane.txt")
        self.df = self.data_processor.get_data()
        
        # Create widgets
        label = tk.Label(self, text="Box Plot", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Start Page",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        self.entry1 = tk.Entry(self, width=6)
        self.entry1.pack()

        button2 = ttk.Button(self, text="Set Threshold",
                            command=self.handle_overrun)
        button2.pack()

        button3 = ttk.Button(self, text="Clear Threshold",
                            command=self.delete_overrun)
        button3.pack()

        # Create canvas for checkboxes
        mycanvas = tk.Canvas(self, width=100, height=100)
        mycanvas.pack(side='right')

        # Create checkboxes for parameters
        self.all_int_vars = {item: tk.IntVar() for item in AVAILABLE_PARAMETERS}
        for item in AVAILABLE_PARAMETERS:
            self.c1 = tk.Checkbutton(mycanvas, text=item, variable=self.all_int_vars[item],
                                   onvalue=1, offvalue=0, command=self.create_graph)
            self.c1.pack(side=tk.TOP)

        # Initialize plot attributes
        self.wykres_canvas = None
        self.toolbar = None

    def handle_overrun(self):
        """Handle overrun value input"""
        global OVERRUNVALUE
        val = self.entry1.get()
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

    def create_graph(self):
        """Create box plot"""
        # Get selected parameters
        selected_params = [key for key, item in self.all_int_vars.items() if item.get() == 1]
        
        # Create figure
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        
        # Create box plot data dictionary
        box_dictionary = {param: self.df[param] for param in selected_params}
        
        # Plot box plot
        p = 'purple'
        o = 'orange'
        a.boxplot(box_dictionary.values(), patch_artist=True,
                 boxprops=dict(facecolor=o, color=o, alpha=0.75),
                 capprops=dict(color=p, alpha=0.75),
                 whiskerprops=dict(color=p, alpha=0.75),
                 flierprops=dict(color=p, markeredgecolor=p, alpha=0.25),
                 medianprops=dict(color=p, alpha=0.75))
        
        # Set labels
        a.set_xticklabels(box_dictionary.keys())
        a.set_title("Box Plot")
        
        # Add overrun line if specified
        if OVERRUNVALUE is not None:
            a.axhline(y=OVERRUNVALUE, color="r", linestyle="--")
        
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