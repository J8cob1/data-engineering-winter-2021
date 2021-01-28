# File: assertions.py
# Description: python file for the Data Validation Activity

import pandas
import math

# Read in data from a csv file and seperate it out into the corresponding tables
crash_data = pandas.read_csv("Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv")
crash_data = crash_data.groupby(crash_data["Record Type"])
crash_data_tables = [
    crash_data.get_group(1).dropna(axis=1, how='all'),
    crash_data.get_group(2).dropna(axis=1, how='all'),
    crash_data.get_group(3).dropna(axis=1, how='all')
]


# Validate the data. For this one, I will execute the assertions that seem to work for each table
# Intra record checks have to be done another way
for index, row in crash_data_tables[1-1].iterrows():
    if (math.isnan(row["Serial #"]) or 
        math.isnan(row["Crash Hour"]) or 
        (row["County Code"] < 1 or row["County Code"] > 36) or 
        (row["City Section ID"] < 1 or row["City Section ID"] > 250) or
        row["Crash Month"] == 2 and row["Crash Day"] > 29 or 
        row["Total Pedestrian Fatality Count"] > row["Total Fatality Count"] or 
        ):
        print(row)
# Validation
# Consider splitting the table based on record types

# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# https://medium.com/@bogdan.cojocar/how-to-do-column-validation-with-pandas-bbeb38f88990
# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
"""error_rows = []
for row in crash_data:
    print (row)
for index, row in crash_data.iterrows():
    if (math.isnan(row["Serial #"]) or
        math.isnan(row["Crash Hour"]) or 
        (row["Crash Hour"] < 0.0 or row["Crash Hour"] > 23.0) or
        (row["County Code"] < 1 or row["County Code"] > 36) or 
        (row["City Section ID"] < 1 or row["City Section ID"] > 250) or
        ):
        #error_rows.append(index)
        print(row["Crash Hour"])"""

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
# https://www.kite.com/python/docs/pandas.DataFrame.groupby