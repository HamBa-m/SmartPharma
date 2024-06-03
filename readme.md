# Medicaments Delivery Schedule App

This Streamlit application helps managers in the pharmaceutical industry to efficiently manage the delivery of medicaments. The system predicts and schedules which drugs need to be sent to specific cities and at what time, optimizing the supply chain and ensuring timely deliveries.

## Features

- Filter predictions by product class and city.
- Display interactive line charts for the predicted medicament needs over time.
- Automatically shows 5 random results if no filters are selected.

## Installation

To run this application, you need to have Python installed on your system. Follow the steps below to set up and run the app.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Install Streamlit

Open your terminal and run the following command to install Streamlit:

```bash
pip install streamlit
```

### Install Other Dependencies

Ensure you have `pandas` installed. If not, you can install it using pip:

```bash
pip install pandas
```

## Running the App

1. Clone this repository or download the code files.

2. Ensure your project directory has the following structure:

```
PHARMA
├── app
│   ├── app.py
│   └── predictions.json
├── data
│   ├── data.xlsx
│   ├── dataframe_dict.pkl
│   ├── eda.ipynb
│   └── model.pth
└── README.md
```

3. Place your `predictions.json` file in the `app` directory.

4. Open a terminal in the `SmartPharma` directory and run the following command:

```bash
streamlit run app/app.py
```

5. The application will start, and you can access it in your web browser at `http://localhost:8501`.

## File Structure

```
PHARMA
├── app
│   ├── app.py
│   └── predictions.json
├── data
│   ├── data.xlsx
│   ├── dataframe_dict.pkl
│   ├── eda.ipynb
│   └── model.pth
└── README.md
```

- `app/app.py`: The main Streamlit app script.
- `app/predictions.json`: The JSON file containing the predictions data.
- `data/data.xlsx`: The Excel file containing training data.
- `data/dataframe_dict.pkl`: A pickle file with a dictionary of dataframes.
- `data/eda.ipynb`: A Jupyter notebook for exploratory data analysis.
- `data/model.pth`: The trained model file.
- `README.md`: This file, containing instructions for running the app.

## Usage

- Use the filters on the left sidebar to select the product classes and cities you want to visualize.
- The filtered data will be displayed in a table.
- Interactive line charts will show the predicted medicament needs over time, with each tick on the x-axis representing a month starting from the current month.
- If no filters are selected, 5 random results will be displayed by default.

## License

This project is licensed under the MIT License.