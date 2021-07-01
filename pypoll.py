
# Add our Dependencies
import csv
import os
# Asssign a variable for the file to load and the path
file_to_load=os.path.join("resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis,election_analysis.txt")
# Open the election result and read the file
with open(file_to_load) as election_data:
    
    # To do: read and analyse the data here.
    # file_reader=csv.reader(election_data)

    # print each row in the CSV file.
    # for row in file_reader:
    # print(row)

    # Read the file oblect with the reader function.
    file_reader=csv.reader(election_data) 
    #print the header row. next() method will skip the first row and return the next item in the list.
    headers=next(file_reader)
    print (headers)