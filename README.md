# Data Visualization Application

Simple Python application for visualizing time series data with multiple plot types and interactive features. 

![](data_visualizer.gif)

## Features

- Line plots with time range selection
- Box plots with parameter selection
- Histograms with customizable bin width
- Correlation matrix heatmap
- Scatter plots with multiple parameter selection

## Data

The data included in this project is NOT the original data from any specific aircraft.  This data was modified based on the data from the flight data recorder in a way that conserves all flight characteristics. 

## Installation

### Using Conda (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/edytaolow01/data_visualizer
cd data_visualizer
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate data-visualization
```

### Using pip

1. Clone the repository:
```bash
git clone https://github.com/edytaolow01/data_visualizer
cd data_visualizer
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

1. Place your data file (Modified_data.txt) in the project root directory
2. Run the application:
```bash
python main.py
```

## Project Structure

```
.
├── main.py                 # Application entry point
├── data_processor.py       # Data loading and processing
├── gui/                    # GUI components
│   ├── app.py             # Main application window
│   └── pages/             # Individual page implementations
│       ├── start_page.py
│       ├── line_plot_page.py
│       ├── box_plot_page.py
│       ├── histogram_page.py
│       ├── correlation_page.py
│       └── scatter_plot_page.py
└── utils/                  # Utility functions and constants
    ├── constants.py
    └── helpers.py
```

## Requirements

- Python 3.12 or higher (other may cause application errors)
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Pillow

## Limitations

- Since the data covers only one flight, a broader analysis using machine learning and deep learning techniques would likely not be effective. This will be addressed in future work.
- The application should be optimized both in terms of the GUI and the time required to generate plots.
