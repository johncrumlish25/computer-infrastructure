#! /usr/bin/env python

# Import libraries.
import yfinance as yf
import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Download five days of hourly stock market data
def get_data():
    df = yf.download(
        ["NVDA", "AVGO", "ARM", "AMD", "IBM"],
        period="5d",
        interval="1h"
    )

    # Generate a timestamp for the filename
    now = dt.datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M%S")

    # Save the downloaded data as a CSV file
    filename = f"data/{timestamp}.csv"
    df.to_csv(filename)

    return df


# Function to plot the percentage change in stock prices
def plot_data():

    # Find all CSV files in the data folder
    files = [file for file in os.listdir("data") if file.endswith(".csv")]

    # Find the most recent CSV file
    latest_file = max(files)

    # Read the latest CSV file using the first two rows as column headings
    stock_data = pd.read_csv("data/" + latest_file, header=[0, 1], index_col=0)

    # Calculate the percentage change in closing prices
    percentage_change = (stock_data["Close"] - stock_data["Close"].iloc[0]) / stock_data["Close"].iloc[0] * 100

    # Plot the percentage change
    percentage_change.plot()

    # Add title and labels 
    plt.title("Percentage Change in Closing Prices - " + latest_file[:8])
    plt.xlabel("Date")
    plt.ylabel("Percentage Change (%)")

    # Rotate the date labels for better readability
    plt.xticks(rotation=45)

    # Change the legend heading
    plt.legend(title="Company")

    # Adjust the layout to prevent overlapping
    plt.tight_layout()

    # Generate a timestamp for the filename
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

    # Save the graph as a PNG file
    plt.savefig("plots/" + timestamp + ".png")

    # Display the graph
    plt.show()


# Call both functions
get_data()
plot_data()