log_file = open("um-server-01.txt") 
# this line is opening the file 'um-server-01.txt' for reference and stores it to a variable


def sales_reports(log_file):
    #creating a function
    for line in log_file:
         # this is looping through the value of file
        line = line.rstrip() 
        # this is a method that removes whitespace from line
        day = line[0:3] 
        # this is setting a day variable 
        if day == "Mon": 
            # this is looking to see if day variable is = to Tues/changed to monday per 
            print(line) 
            # this prints out the variable.


sales_reports(log_file) 
# invokes the function when software runs
