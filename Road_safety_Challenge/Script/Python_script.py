#step 1: Import the required libraries needed for this script
# using pandas
# using beautifulsoup would have been a good option also but its a framework
# so for this task , we are using only pandas library
import pandas as pd


# step 2: Create a function that runs the necessary scripts  and return the final output

def Data_wrangling():
    
    # step 3: Read the website with its url into the script
    #         Method - pd.read_html (This would read all the tables in the website and puts them in a single list)
    #         Use List indexing to get the required table
    
    df = pd.read_html('https://en.wikipedia.org/wiki/Road_safety_in_Europe')
    df_output = df[2]

    #step 4: Select the required columns from the table, filtering out the ones that won't be used 
    df_output = df_output[['Country', 'Area (thousands of km2)[24]', 'Population in 2018[25]', 'GDP per capita in 2018[26]', 'Population density (inhabitants per km2) in 2017[27]', 
             'Vehicle ownership (per thousand inhabitants) in 2016[28]', 'Total Road Deaths in 2018[30]', 'Road deaths per Million Inhabitants in 2018[30]']]

    #step 5: Rename the columns above to the desired names as required.
    df_output = df_output.rename(  columns={
        'Area (thousands of km2)[24]':'Area',
        'Population in 2018[25]':'Population',
        'GDP per capita in 2018[26]':'GDP per Capita',
        'Population density (inhabitants per km2) in 2017[27]':'Population Density',
        'Vehicle ownership (per thousand inhabitants) in 2016[28]':'Vehicle Ownership',
        'Total Road Deaths in 2018[30]':'Total Road Deaths',
        'Road deaths per Million Inhabitants in 2018[30]':'Road deaths per Million Inhabitants'}) 
    
    #step 6: Insert a Year column in the data and populate with a constant value of 2018
    df_output.insert(1, 'Year', 2018)

    #step 7: Sort data using the Road deaths per million inhabitants column, excluding the last row
    #The last row contains EU total for all countries, and should remain at the bottom of the table
    Data_sorted = df_output[0:28].sort_values('Road deaths per Million Inhabitants')

    #step 8: Add the EU total row back to the bottom of the sorted data.
    output = Data_sorted.append(df_output.loc[28])

    #step 9: store the resulting dataset in a csv file, and filter out the index and allowing "Country" as first column in resulting csv file.
    output.to_csv('Wrangled_data.csv', index = False)

    return output

#final step: call the function here
Data_wrangling()
