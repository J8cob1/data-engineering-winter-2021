# File: assertions.py
# Description: python file for the Data Validation Activity

import pandas
import math

# Read in data from a csv file and seperate it out into the corresponding tables
crash_data = pandas.read_csv("Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv")
crashes = crash_data[crash_data["Record Type"] == 1].dropna(axis=1, how='all')
vehicles = crash_data[crash_data["Record Type"] == 2].dropna(axis=1, how='all')
participants = crash_data[crash_data["Record Type"] == 3].dropna(axis=1, how='all')

# Validate the data. For this one, I will execute the assertions that seem to work for each table
for index, row in crashes.iterrows():
    # Existance Assertions, Limit Assertions, and Intra-record check assertions are here
    if (math.isnan(row["Serial #"])):
        print("Empty Serial Number")
    if (math.isnan(row["Crash Hour"])):
        print("Empty Crash Hour")
    if (row["County Code"] < 1 or row["County Code"] > 36):
        print("Country Code Not In Range")
    if (row["City Section ID"] < 1 or row["City Section ID"] > 250):
        print("City Section ID Not In Range")
    if (row["Crash Month"] == 2 and row["Crash Day"] > 29):
        print("There is an entry where February has a 29th day")
    if (row["Total Pedestrian Fatality Count"] > row["Total Fatality Count"]):
        print("The total pedestrian fatiality count is greater than the total fatality count")
        #crashes.drop([index], axis=0)
    
    # Summary Assertion 1: there can't be any duplicate serial number entries
    num_instances = len(crashes[crashes["Serial #"] == row["Serial #"]])
    if (num_instances > 1):
        print ("Duplicate Crash Serial Number Entry")

    # Summary Assertion 2: All crashes probably shouldn’t have more than 100 fatalities each
    max_fatalities = 100
    if row["Total Fatality Count"] > max_fatalities:
        print("Crash has more than " + str(max_fatalities) + " fatalities. This is likely a mistake")

# Referential Integrity Check 1: Every crash id in the vehicles table should refer to a crash id in the crashes table
for index, row in vehicles.iterrows():
    num_results = len(crashes.query('`Crash ID` == ' + str(row["Crash ID"])).index)
    if num_results == 0:
        print("Vehicle crash id does not match one from the crash_id table")

# Referential Integrity Check 2: Every crash id in the participants table should refer to a crash id in the crashes table (once the data is split up into the corresponding tables)
for index, row in participants.iterrows():
    num_results = len(crashes.query('`Crash ID` == ' + str(row["Crash ID"])).index)
    if num_results == 0:
        print("Participant crash id does not match one in the crash_id table")

# https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# https://medium.com/@bogdan.cojocar/how-to-do-column-validation-with-pandas-bbeb38f88990
# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
# https://www.kite.com/python/docs/pandas.DataFrame.groupby
# https://medium.com/@bogdan.cojocar/how-to-do-column-validation-with-pandas-bbeb38f88990
# https://stackoverflow.com/questions/50242968/check-for-duplicate-values-in-pandas-dataframe-column
# https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe