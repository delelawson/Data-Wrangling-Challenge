# Date Created

Created on the 18th of August 2021.

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
