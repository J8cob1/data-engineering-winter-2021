# File: data-integration-script.py
# Purpose: to combine the countey level COVID-19 data and ACS Census Tract Data for 2017 (for the class Data Integration Activity)
# Date: 2/23/2021

import pandas

# Read in CSVs
censusTractData = pandas.read_csv("data/acs2017_census_tract_data.csv")
covid19Data = pandas.read_csv("data/COVID_county_data.csv")
#print(censusTractData)
#print(covid19Data)

# Combine the data
