# Date Created

Updated on the 20th of February 2025.

## Project Title

Data Wrangling Challenge, Software Engineer - for Datopian

## Project Description

This project aims at scraping a table data from given website. The table from the site gives details on the rate at which road accident deaths occur in European Union Countries. The next task is to then clean the data and add visuals to give more insights on the data.


## How to Set up the project

For preference, two scripts were created: a `.py` and  `.ipynb` script. With this, user as a choice at which to lauch the codes.

To use this project locally,

Get [anaconda ](https://www.anaconda.com/products/individual) for `.ipynb` 
Get a code editor like [Vscode](https://code.visualstudio.com/download) or Atom. 
Get power Bi desktop [Power bi desktop](https://powerbi.microsoft.com/en-us/downloads/). This will be neeeded to  view the visualized file (Europian Union Road Deaths Visualization).

### step 1
### Clone the repository

    `git clone https://github.com/delelawson/Data-Wrangling-Challenge`
 
### step 2
### Start the virtual environment and Run the commands below in the project root folder

    `virtualenv env
     source env/Scripts/activate # for windows
     source env/bin/activate # for MacOs`

### step 3
### Install pandas Extensions

    `pip install pandas`

# step 4
### Running the script: In the project root directory, run any of
    
    `python Road_safety_Challenge\Script\Python_script.py
     conda Road_safety_Challenge\Script\Jupiter_Script.ipynb`

## Script Functionalities
The `Data_wrangling` function is used for solving this challenge.It takes the url and scrapes it for the desired data by indexing the list of tables gotten for the specific table. The data is then filtered according to the requiremets of the task.
The resulting data is then converted to a CSV file located in the [Wrangled_Data folder](Road_safety_Challenge/Wrangle_data)

### Visualisation:
This was seperated into 3 pages:

- **1. Summary**: A summary of the data 
<img width="744" alt="Image" src="https://github.com/user-attachments/assets/c1372757-0fbd-4d9a-a41b-55ceba5cddfc" />

- **2. Statistical analysis**: This shows the correlation of road death with other factors 
<img width="743" alt="Image" src="https://github.com/user-attachments/assets/4e0e45b1-2755-4844-826c-225f9e0399d1" />

- **3. Insights and recommendation**: Shows detailed insights and profers recommendations

### Some DAX (correlation furmula)
```bash

Population_correlation = 
VAR Mean_X = AVERAGE(Wrangled_data[Population])
VAR Mean_Y = AVERAGE(Wrangled_data[Road deaths per million inhabitants])

VAR Numerator = 
    SUMX(
        Wrangled_data, 
        (Wrangled_data[Population] - Mean_X) * 
        (Wrangled_data[Road deaths per million inhabitants] - Mean_Y)
    )

VAR Denom_X = 
    SQRT(
        SUMX(
            Wrangled_data, 
            POWER(Wrangled_data[Population] - Mean_X, 2)
        )
    )

VAR Denom_Y = 
    SQRT(
        SUMX(
            Wrangled_data, 
            POWER(Wrangled_data[Road deaths per million inhabitants] - Mean_Y, 2)
        )
    )

RETURN DIVIDE(Numerator, Denom_X * Denom_Y, BLANK())
```
### Python script (for creating a correlation table; relating road death to all factors )
```bash
import pandas as pd


numeric_cols = dataset.select_dtypes(include=['number'])


target_col = "Road deaths per Million Inhabitants"

# To check if the target column exists in the dataset
if target_col in numeric_cols.columns:
    # Compute correlation of each numeric column with the target column
    correlation_df = numeric_cols.corr()[[target_col]].reset_index()
    correlation_df.columns = ["Feature", "Correlation with Road Deaths"]
else:
    correlation_df = pd.DataFrame(columns=["Feature", "Correlation with Road Deaths"])


dataset = correlation_df
```
