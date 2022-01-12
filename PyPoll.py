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


# Initialize a total vote counter
total_votes = 0

# Initialize a list to store candidates' names
candidate_options = []

# Initialize vote counter dictionary
candidate_votes = {}



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
    #print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list and vote count
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate count
        candidate_votes[candidate_name] += 1


# Print the total votes
print(total_votes)

# Print the candidate list
print(candidate_options)

# Print the candidate vote dictionary
print(candidate_votes)

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
for candidate_name in candidate_votes:
    # Retrieve vot count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and the percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1F}% of the vote.")

    # Print candiate, vote count, and percentage 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning candidate equal to the candidates name
        winning_candiate = candidate_name

winning_candidate_summary = (

    f"--------------------------\n"
    f"Winner: {winning_candiate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n"
)

print(winning_candidate_summary)









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

