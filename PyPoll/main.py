# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:41:04 2021

@author: Zach
"""

import os
import pandas as pd
import csv

#Read csv file and setup dataframe
election_csv = os.path.join('Resources', 'election_data.csv')

election_csv_df = pd.read_csv(election_csv)
                            
df = pd.DataFrame(election_csv_df)

#Total Votes Overall
vcount = len(election_csv_df)

#Individual candidate votes
ccount = election_csv_df['Candidate'].value_counts()

# create a new dataframe that includes percentage and total votes for each candidate
updated_df = pd.DataFrame({'Percentage':ccount/vcount, 'Votes': ccount,})

#Convert decimal to percent
updated_df['Percentage'] = updated_df['Percentage'].astype(float).map("{:.2%}".format)


# Determine the winner
winner = updated_df[updated_df['Votes']==updated_df['Votes'].max()]

# print summary table
print("Election Results")
print("-------------------------------")
print("Total Votes: ", vcount)
print("-------------------------------")
print(updated_df)
print("-------------------------------")
print('Winner:')
print(winner)

#Create Dictionary and turn into dataframe

summary_dict = [{'Total Votes': vcount}]

summary_dict_df = pd.DataFrame(summary_dict)


# output text file
tfile = open('Analysis.txt', 'a')
tfile.write(summary_dict_df.to_string())
tfile.write(updated_df.to_string())
tfile.close()
