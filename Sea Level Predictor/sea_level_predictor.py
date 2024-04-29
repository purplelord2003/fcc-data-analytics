import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12,7))
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df, marker='x')

    # Create first line of best fit
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    slope = res.slope
    intercept = res.intercept
    
    x = pd.Series(range(1880, 2051))
    y = x * slope + intercept

    plt.plot(x, y, "r-")

    # Create second line of best fit
    df_2 = df[df["Year"] >= 2000]
    res_2 = linregress(x=df_2["Year"], y=df_2["CSIRO Adjusted Sea Level"])
    slope_2 = res_2.slope
    intercept_2 = res_2.intercept
    
    x_2 = pd.Series(range(2000, 2051))
    y_2 = x_2 * slope_2 + intercept_2

    plt.plot(x_2, y_2, "b-")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()