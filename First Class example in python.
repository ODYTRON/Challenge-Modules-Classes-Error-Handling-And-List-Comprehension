# First Class example in python. the example is a dataset which has to do
# with NFL suspensions

# Class name
class Suspension():
# Initial function , initiated with self and a key word to archive columns # note that you set columns
# you call positions of a single arbitrary row for the moment , then it will be specific , which row
    def __init__(self,column):
# we set all the properties to the coresponding columns        
        self.name = column[0]
        self.team = column[1]
        self.games = column[2]
        self.suspensions = column[3]
# now let's play with the exceptions here we need to convert the year to integer
# if this fails we set the particular value of the year to 0 (for example if the line dont exist)
        try:
# here is the conversion         
            self.year = int(column[5])
# if there is fail the exception sets year property to 0             
        except Exception:
             self.year = 0
# METHODS LETS MAKE SOME METHODS TO RETURN VALUES FROM OUR ROWS             
    def get_year(self):
        return(self.year)
    def get_name(self):
        return(self.name)
    def get_team(self):
        return(self.team)
    def get_games(self):
        return(self.games)
    def get_suspensions(self):
        return(self.suspensions)
        
# make an instance for the first suspension # note that you call lines 
# now we have specific row , our class instance has inside which columns to access 

first_suspension = Suspension(nfl_suspensions[0])

# call all the methods to archive info about the first line of the data set

get_first_suspension_year = first_suspension.get_year()
get_first_suspension_name = first_suspension.get_name()
get_first_suspension_team = first_suspension.get_team()
get_first_suspension_games = first_suspension.get_games()
get_first_suspension_suspensions = first_suspension.get_suspensions()





