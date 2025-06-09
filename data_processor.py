import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = None
        self.time = None
        self.load_data()
        
    def load_data(self):
        """Load and preprocess the data"""
        # Read data from file
        self.df = pd.read_table(self.data_file)
        
        # Normalize time
        num_points = len(self.df)
        normalized_time = np.linspace(0, self.df['czas'].max(), num_points)
        self.df['czas'] = normalized_time
        
        # Format time
        self.df['czas'] = pd.to_datetime(self.df["czas"], unit='s').dt.strftime("%H:%M:%S")
        self.time = self.df['czas']
        
    def get_data(self):
        """Return the processed dataframe"""
        return self.df
        
    def get_time(self):
        """Return the time series"""
        return self.time 