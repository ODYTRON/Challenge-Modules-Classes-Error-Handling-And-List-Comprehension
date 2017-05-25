# import modules
import csv

# csv file handler
#here we use the csv module
csvopener = open('nfl_suspensions_data.csv')
csvreader = csv.reader(csvopener)
nfl_suspensions = list(csvreader)

# header extractor 
# wanna cut rows just slice , wanna cat columns just iterate
nfl_suspensions = nfl_suspensions[1:]

# Count up the frequency for each value in the year column.
# we use the method if empty else fill with key, value = 1 till the if detects to add more integers.  
years = {}
for rows in nfl_suspensions:
    row_year = rows[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
            years[row_year] = 1
            
            
print(years)
