import matplotlib
matplotlib.use('TkAgg')
from matplotlib import style
style.use("ggplot")

from gui.app import App
from data_processor import DataProcessor

def main():
    # Initialize data processor
    data_processor = DataProcessor("Modified_data.txt")
    
    # Create and run the application
    app = App()
    app.geometry("1280x720")
    app.mainloop()

if __name__ == "__main__":
    main() 