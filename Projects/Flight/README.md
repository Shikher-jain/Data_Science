# ⚠️ Note: The MySQL database used in this project runs only on your local machine (localhost) and is not hosted on the cloud. You must have MySQL installed and running locally to use all features of this application.

# 🚀 [Live Streamlit App](https://shikherjain09-flights-app.streamlit.app/)

# Flight Data Science Project

This project is designed to analyze and manage flight data using Python. It provides tools for cleaning, storing, and interacting with flight datasets, leveraging a local database and a simple application interface.

## Project Structure

- **app.py**: Main application file. Likely contains the entry point for running the app (e.g., a Streamlit or Flask interface).
- **crud.py**: Contains Create, Read, Update, Delete operations for managing flight data in the database.
- **csv_to_sql.py**: Script to import and convert flight data from CSV format into a SQL database.
- **db_helper.py**: Database helper functions for connecting to and interacting with the database.
- **flights_cleaned.csv**: The cleaned flight dataset used for analysis and database import.
- **requirements.txt**: Lists all Python dependencies required to run the project.

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Data_Science/Projects/Flight
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Import Data**: Run the CSV to SQL script to load data into the database:
   ```bash
   python csv_to_sql.py
   ```
2. **Run the Application**: Start the main app (e.g., Streamlit or Flask):
   ```bash
   python app.py
   ```
   or, if using Streamlit:
   ```bash
   streamlit run app.py
   ```

## File Descriptions
- **app.py**: Launches the user interface for interacting with flight data.
- **crud.py**: Functions for database operations (add, view, update, delete records).
- **csv_to_sql.py**: Loads and processes the CSV data into the SQL database.
- **db_helper.py**: Utility functions for database connectivity and queries.
- **flights_cleaned.csv**: Source data file for flights (cleaned and ready for import).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open source and available under the [MIT License](LICENSE).
