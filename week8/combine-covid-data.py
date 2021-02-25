# File: combine-covid-data.py
# Purpose: simplify the covid data entries
# Date: 2/23/2021

import pandas
import numpy
import datetime

# Read in data
covidData = pandas.read_csv("data/COVID_county_data.csv")

# Get the individual counties, then combine all the data for the state/county combinations
counties = covidData["county"].unique()
entries = []
for county in counties:
    # Find all the entries for the county
    county_data = covidData[covidData['county'] == county]

    # Get the states for the given county name, and calculate the data for the state/county combinations
    states = county_data['state'].unique()
    for state in states:
        # Find all the entries for this state and county
        state_county_data = county_data[county_data['state'] == state]
        #print(state_county_data)

        # Calculate the fields we want
        total_cases = state_county_data['cases'].sum()
        total_deaths = state_county_data['deaths'].sum()

        dec_2020_start = datetime.datetime(2020, 12, 1)
        dec_2020_end = datetime.datetime(2020, 12, 31)
        dec_2020_rows = pandas.to_datetime(state_county_data['date']).between(dec_2020_start, dec_2020_end, inclusive=True)
        dec_2020_data = state_county_data[dec_2020_rows]
        
        cases_reported_dec_2020 = dec_2020_data['cases'].sum()
        deaths_reported_dec_2020 = dec_2020_data['deaths'].sum()
        
        # Save the fields (along with the state and county names)
        entries.append([state, county, total_cases, total_deaths, cases_reported_dec_2020, deaths_reported_dec_2020])

# Write all the values we've saved to a new csv
parsed_covid_data = pandas.DataFrame(entries, columns=["State", "County", "TotalCases", "TotalDeaths", "Dec2020Cases", "Dec2020Deaths"])
parsed_covid_data.to_csv("data/parsed_covid_data.csv", index=False)