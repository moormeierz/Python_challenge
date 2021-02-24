# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:37:34 2021

@author: Zach
"""

import os
import pandas as pd
import csv


# Read csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')
          
# Create dataframe
budget_csv_df = pd.read_csv(budget_csv)   
                          
df = pd.DataFrame(budget_csv_df)


# Total months
mcount = len(budget_csv_df)

# Total Profit/Loss
total_profit = budget_csv_df["Profit/Losses"].sum()


# Create another column in dataframe
# Difference month to month  (this makes the print function more appealing)

mdiff = budget_csv_df["Profit/Losses"].diff()

df['Difference'] = mdiff


# Calculate Average, Min, Max of Difference column
avg = mdiff.mean()

increase = mdiff.max()

decrease = mdiff.min()


# Create a new dataframe that only includes Date and Difference for the summary table
summary_df = budget_csv_df[["Date", "Difference"]]


# Print Summary Table
print("Financial Analysis")
print("-------------------------")
print("Total Months: " ,mcount)
print("Total:  $",total_profit)
print(f"Average Change: ${avg:.2f}")
print("-------------------------")
print("Greatest Increase")
print(summary_df[mdiff==mdiff.max()])
print("-------------------------")
print("Greatest Decrease")
print(summary_df[mdiff==mdiff.min()])


# create dictionary, turn into dataframe
summary_dict = [{"Total Months": mcount, "Total Profit": total_profit, "Average Change": avg, 
                 "Greatest Increase": increase, "Greatest Decrease": decrease}]

summary_dict_df = pd.DataFrame(summary_dict)


# Output text file
tfile = open('Analysis.txt', 'a')
tfile.write(summary_dict_df.to_string())
tfile.close()


















