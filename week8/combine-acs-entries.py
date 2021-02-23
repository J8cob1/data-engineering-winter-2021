# File: combine-acs-entries.py
# Purpose: combine all the entires in the census data table into county-level (i.e: one row per county) entries
# Date: 2/23/2021

import pandas
import numpy

# Read in data
censusTractData = pandas.read_csv("data/acs2017_census_tract_data.csv")

# Get the individual counties, then combine all the data for the state/county combinations
counties = censusTractData["County"].unique()
entries = []
for county in counties:
    # Find all the entries for the county
    county_data = censusTractData[censusTractData['County'] == county]

    # Get the states for the given county name, and calculate the data for the state/county combinations
    states = county_data['State'].unique()
    for state in states:
        # Find all the entries for this state and county
        state_county_data = county_data[county_data['State'] == state]
        
        # Calculate the field we want
        total_population = state_county_data['TotalPop'].sum()
        
        population_in_poverty = numpy.array(state_county_data['TotalPop']) * (numpy.array(state_county_data['Poverty'])/100)
        population_in_poverty = population_in_poverty[~numpy.isnan(population_in_poverty)]
        overall_poverty_percentage = numpy.sum(population_in_poverty) / total_population

        total_incomes_per_population = numpy.array(state_county_data['TotalPop']) * numpy.array(state_county_data['IncomePerCap'])
        total_incomes_per_population = total_incomes_per_population[~numpy.isnan(total_incomes_per_population)]
        total_income_per_capita = numpy.sum(total_incomes_per_population) / total_population

        # Save all the values (along with the state and county names)
        entries.append([state, county, total_population, total_income_per_capita])

# Write all the values we've saved to a new csv
parsed_census_data = pandas.DataFrame(entries, columns=["State", "County", "Population", "IncomePerCapita"])
parsed_census_data.to_csv("data/parsed_cencus_data.csv", index=False)