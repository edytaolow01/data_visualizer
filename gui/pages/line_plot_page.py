import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import seaborn as sns

from utils.constants import LARGE_FONT, AVAILABLE_PARAMETERS, SLIDERX1, SLIDERX2, SLIDERY1, SLIDERY2
from utils.helpers import popup_msg, validate_numeric_input
from data_processor import DataProcessor

class PageOne(tk.Frame):
    """Line plot page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Initialize data processor
        self.data_processor = DataProcessor("Dane.txt")
        self.df = self.data_processor.get_data()
        self.time = self.data_processor.get_time()
        
        # Create widgets
        label = tk.Label(self, text="Line Plot", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Start Page",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = ttk.Button(self, text="Clear Ranges",
                            command=self.delete_overrun)
        button2.pack()

        # Create canvas for checkboxes
        mycanvas = tk.Canvas(self, width=100, height=100)
        mycanvas.pack(side='right')
        
        mycanvas2 = tk.Canvas(self, width=100, height=100)
        mycanvas2.pack(side='right')
        
        # Create checkboxes for parameters
        self.all_int_vars = {item: tk.IntVar() for item in AVAILABLE_PARAMETERS}
        for item in AVAILABLE_PARAMETERS:
            self.c1 = tk.Checkbutton(mycanvas, text=item, variable=self.all_int_vars[item],
                                   onvalue=1, offvalue=0, command=self.create_graph)
            self.c1.pack(side=tk.TOP)

        # Create time range inputs
        self.entry1 = tk.Entry(mycanvas2, width=6)
        self.entry1.pack()

        self.s_time = tk.Scale(mycanvas2, from_=0, to=110, orient='horizontal',
                              length=100, showvalue=1, label='Time Range [min]',
                              command=self.value_from_scalex1)
        self.s_time.pack()

        button3 = ttk.Button(mycanvas2, text="Set Time Range Start [min]",
                            command=self.handle_overrunx1)
        button3.pack()

        self.entry2 = tk.Entry(mycanvas2, width=6)
        self.entry2.pack()

        self.s_time2 = tk.Scale(mycanvas2, from_=0, to=110, orient='horizontal',
                               length=100, showvalue=1, label='Time Range [min]',
                               command=self.value_from_scalex2)
        self.s_time2.pack()

        button4 = ttk.Button(mycanvas2, text="Set Time Range End [min]",
                            command=self.handle_overrunx2)
        button4.pack()

        # Create y-axis range inputs
        self.entry3 = tk.Entry(mycanvas2, width=6)
        self.entry3.pack()

        self.s_time3 = tk.Scale(mycanvas2, from_=0, to=22000, orient='horizontal',
                               length=100, showvalue=1, label='Y-Axis Range Start',
                               command=self.value_from_scaley1)
        self.s_time3.pack()

        button5 = ttk.Button(mycanvas2, text="Set Y1",
                            command=self.handle_overruny1)
        button5.pack()

        self.entry4 = tk.Entry(mycanvas2, width=6)
        self.entry4.pack()

        self.s_time4 = tk.Scale(mycanvas2, from_=0, to=22000, orient='horizontal',
                               length=100, showvalue=1, label='Y-Axis Range End',
                               command=self.value_from_scaley2)
        self.s_time4.pack()

        button6 = ttk.Button(mycanvas2, text="Set Y2",
                            command=self.handle_overruny2)
        button6.pack()

        # Initialize plot attributes
        self.wykres_canvas = None
        self.toolbar = None

    def handle_overrunx1(self):
        """Handle time range start input"""
        val = self.entry1.get()
        if validate_numeric_input(val):
            self.s_time.set(float(val))
            self.entry1.delete(0, tk.END)
        else:
            popup_msg("Podaj cyfrę")

    def handle_overrunx2(self):
        """Handle time range end input"""
        val = self.entry2.get()
        if validate_numeric_input(val):
            self.s_time2.set(float(val))
            self.entry2.delete(0, tk.END)
        else:
            popup_msg("Podaj cyfrę")

    def handle_overruny1(self):
        """Handle y-axis range start input"""
        val = self.entry3.get()
        if validate_numeric_input(val):
            self.s_time3.set(float(val))
            self.entry3.delete(0, tk.END)
        else:
            popup_msg("Podaj cyfrę")

    def handle_overruny2(self):
        """Handle y-axis range end input"""
        val = self.entry4.get()
        if validate_numeric_input(val):
            self.s_time4.set(float(val))
            self.entry4.delete(0, tk.END)
        else:
            popup_msg("Podaj cyfrę")

    def value_from_scalex1(self, s1):
        """Update time range start value"""
        global SLIDERX1
        SLIDERX1 = float(s1)
        self.create_graph()

    def value_from_scalex2(self, s2):
        """Update time range end value"""
        global SLIDERX2
        SLIDERX2 = float(s2)
        self.create_graph()

    def value_from_scaley1(self, s3):
        """Update y-axis range start value"""
        global SLIDERY1
        SLIDERY1 = float(s3)
        self.create_graph()

    def value_from_scaley2(self, s4):
        """Update y-axis range end value"""
        global SLIDERY2
        SLIDERY2 = float(s4)
        self.create_graph()

    def create_graph(self):
        """Create line plot"""
        # Get selected parameters
        selected_params = [key for key, item in self.all_int_vars.items() if item.get() == 1]
        
        # Create figure
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        
        # Plot selected parameters
        for param in selected_params:
            a.plot(self.time, self.df[param], label=param)
        
        # Add legend
        if selected_params:
            a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
            title = f"Dependence of {', '.join(selected_params)} on time"
            a.set_title(title)
        
        # Set axis limits and ticks
        a.set(xlim=(0, 6050))
        a.set_xticks(a.get_xticks()[::900])
        
        # Add time range highlight
        if SLIDERX1 is not None and SLIDERX2 is not None:
            a.axvspan(SLIDERX1*60, SLIDERX2*60, alpha=0.50)
        
        # Add y-axis range highlight
        if SLIDERY1 is not None and SLIDERY2 is not None:
            a.fill_between(self.time, SLIDERY1, SLIDERY2, alpha=0.50)
        
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

    def delete_overrun(self):
        """Reset all range values"""
        global SLIDERX1, SLIDERX2, SLIDERY1, SLIDERY2
        SLIDERX1 = None
        SLIDERX2 = None
        SLIDERY1 = None
        SLIDERY2 = None
        self.create_graph() 