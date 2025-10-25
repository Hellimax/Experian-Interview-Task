# Experian-Interview-Task

A Python application for processing and analyzing listing data with automation capabilities.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Environment Setup

### 1. Install Dependencies

Install all required packages using the provided requirements file:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory of the project:

```bash
cp sample.env .env
```

Edit the `.env` file and configure the required environment variables according to your setup. Refer to `sample.env` for the correct format and required variables.

## Running the Application

### Main Application

To run the main application:

```bash
python app.py
```

### Automation Script

The `testing_automation.py` script automates the processing of multiple listing files. It takes a folder path as input that contains different listings in `.txt` format.

The folder should contain listing files in `.txt` format, each representing a different listing to be processed.

## Output Files

The application generates the following output files:

- **`listing_results.json`** - Contains the results of all processed listings
- **`listing_results_latest.json`** - Contains the most recent results of all listings

These files are automatically generated after running the application or automation script.

## Project Structure

```
Experian-Interview-Task/
├── app.py                          # Main application file
├── testing_automation.py           # Automation script for batch processing
├── requirements.txt                # Python dependencies
├── sample.env                      # Sample environment configuration
├── .env                           # Your environment configuration (create this)
├── listing_results.json           # Output: All listing results
└── listing_results_latest.json    # Output: Latest listing results
```


## Contact

[Add your contact information here]
