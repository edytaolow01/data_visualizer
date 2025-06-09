# Data Visualization Application

A Python application for visualizing time series data with multiple plot types and interactive features.

## Features

- Line plots with time range selection
- Box plots with parameter selection
- Histograms with customizable bin width
- Correlation matrix heatmap
- Scatter plots with multiple parameter selection

## Installation

### Using Conda (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate data-visualization
```

### Using pip

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

1. Place your data file (Dane.txt) in the project root directory
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

- Python 3.11 or higher
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Pillow

## License

This project is licensed under the MIT License - see the LICENSE file for details. 