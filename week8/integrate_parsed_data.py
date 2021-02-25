# File: integrate_parsed_data.py
# Purpose: to combine the county level data produced by the other two python scripts, adn potentially do some analysis
# Date: 2/23/2021

import pandas
import itertools

# Calculate the pearson correlation coefficient, and draw a graph if the coefficient value is less than -0.5 or greater than 0.5
# - column1: the name of the first column we will use to calculate the pearson correlation coefficient 
# - column2: the name of the second column we will use to calculate the pearson correlation coefficient 
# - data: the dataframe you are calculating the coefficient and drawing the graph from
# - isOregon: a boolean indicating if the data is Oregon data (as opposed to national USA data)
def calculateR(column1, column2, data, isOregon):
    R = data[column1].corr(data[column2])
    if (R > 0.5 or R < -0.5):
        plotName = column1 + "-" + column2 + ".png"
        if (isOregon == True):
            plotName = "Oregon-" + plotName
        data.plot.scatter(column1, column2).get_figure().savefig("graphs/" + plotName)

# Read in CSVs
censusData = pandas.read_csv("data/parsed_census_data.csv")
covidData = pandas.read_csv("data/parsed_covid_data.csv")

# Combine data
combined_data = censusData.merge(covidData, how='inner')
#combined_data.to_csv("data/combined_data.csv", index=False)

# Calculate the correlation between columns for all counties in the state of Oregon
oregon_data = combined_data[combined_data['State'] == "Oregon"]
calculateR("TotalCases", "Poverty", oregon_data, True)
calculateR("TotalDeaths", "Poverty", oregon_data, True)
calculateR("TotalCases", "IncomePerCapita", oregon_data, True)
calculateR("TotalDeaths", "IncomePerCapita", oregon_data, True)
calculateR("Dec2020Cases", "Poverty", oregon_data, True)
calculateR("Dec2020Deaths", "Poverty", oregon_data, True)
calculateR("Dec2020Cases", "IncomePerCapita", oregon_data, True)
calculateR("Dec2020Deaths", "IncomePerCapita", oregon_data, True)

# Calculate the correlation between columns for all counties
calculateR("TotalCases", "Poverty", combined_data, False)
calculateR("TotalDeaths", "Poverty", combined_data, False)
calculateR("TotalCases", "IncomePerCapita", combined_data, False)
calculateR("TotalDeaths", "IncomePerCapita", combined_data, False)
calculateR("Dec2020Cases", "Poverty", combined_data, False)
calculateR("Dec2020Deaths", "Poverty", combined_data, False)
calculateR("Dec2020Cases", "IncomePerCapita", combined_data, False)
calculateR("Dec2020Deaths", "IncomePerCapita", combined_data, False)