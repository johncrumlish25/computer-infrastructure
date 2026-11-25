# Computer Infrastructure - Assessment

This repository contains my assessment work for the 'Computer Infrastructure' module delievered by [ATU](https://atu.ie).

## Assessment Overview

The assessment explores various topics relating to computer infrastructure, using Python and Jupyter Notebook.

The problems cover areas including:

- Retrieving and working with financial data using the `yfinance` library.
- Downloading and saving stock market data as CSV files.
- Reading and processing data using Pandas.
- Calculating percentage changes in stock prices.
- Creating plots to visualise and compare stock market performance.

## Contents

- `data/` - Folder containing datasets generated and used throughout the assessment.
- `plots/` - Folder containing plots and visualisations generated throughout the assessment.
- `problems.ipynb` - Jupyter notebook containing the assessment problems and solutions.
- `AGENTS.md` - Instructions and guidelines for using AI as a learning and programming aid.
- `.gitignore` - Files and folders that should not be included in the Git repository.
- `requirements.txt` - Python packages required for the project.

## Requirements

The project uses Python and the following main libraries and modules:

- Jupyter Notebook
- NumPy
- yfinance
- Matplotlib
- datetime
- Pandas
- os

All packages are listed in `requirements.txt`.

## How to Clone and Run This Repository

Clone the repository and install the required packages:

```bash
git clone https://github.com/johncrumlish25/computer-infrastructure.git
pip install -r requirements.txt
jupyter notebook problems.ipynb