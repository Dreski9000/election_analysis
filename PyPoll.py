# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
import datetime as dt
# Use the now() attribute on the dateime class to get the present time
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)
# Import csv module and display its functions
import csv
# print(dir(csv))

# Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'
import os
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis

# Close the file

#election_data.close()
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:

    #To do: Read an analyze data
    #print(election_data)

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the csv file
    # for row in file_reader:
    #     print(row)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)


#Using the open() function with the "w" mode we will write data to the file
#outfile = open(file_to_save, "w")
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file
#     #txt_file.write("Hello World")

#     # Write three counties to the file
#     txt_file.write("Arapahoe\n")
#     txt_file.write("Denver\n")
#     txt_file.write("Jefferson\n")

# Close the file
#outfile.close()

