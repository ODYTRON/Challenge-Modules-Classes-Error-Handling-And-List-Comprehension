
# A full example showing how to import a csv file
# Objectives :
# Make a basic class with a parameter to import 
# make a basic method which counts how many times a name occurs (name is a parameter taken from the instance)
# make a method which counts how many times the import parameter exists under certain contitions 
# Make an instance of the class
# call its two methods


# Step by step explanation 

# import the csv module
import csv

# create the class with the init method (dont forget the key word self)
# As you can see the method takes a parameter which we have to provide in the instance later
class Team():
    def __init__(self, name):
        # We declare the parameter like this
        self.name = name
        # here is the csv handler, open, read, declare it as a list to process it later
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)
    # here is our first method with a counter. It examines the possibility if the import parameter is the same
    # with a text from index[2] and it adds 1 if so
    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
    # Here is something more interesting. It takes one parameter and compares if
    # this parameter exists in index[0] in combination with the name parameter
    # dont forget to declare the counter inside the method haha
    def count_wins_in_year(self, year):
        self.year = year
        metritis = 0
        for recurse in self.nfl:
            if recurse[2] == self.name and recurse[0] == self.year:
                metritis = metritis + 1
        return metritis
        
# Make the instance
niners = Team("San Francisco 49ers")
# call method 1
niners_wins_2013 = niners.count_wins_in_year("2013")
# call method 2
niners_total_wins = niners.count_total_wins()




