# Add our Dependencies
import csv
import os
# Asssign a variable for the file to load form a path
file_to_load=os.path.join("resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis,election_analysis.txt")

# 1. Initialise a total volume counter set to 0
total_votes=0

# Candidate Option
candidate_option=[]
# Declare empty Candidate votes dictionary
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election result and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data) 
    
    # Read the header row..
    headers=next(file_reader)
    
    
    # print each row in the CSV file.
    for row in file_reader:
    
        #2. Add to the total vote count. 
        total_votes +=1

        # Print Candidate name from each row
        candidate_name=row[2]

        #if the candidate does not match any existing candidate (code will skip candidate already found add new candidate)
        if candidate_name not in candidate_option:
            # Add it to the list of candidates.
            candidate_option.append(candidate_name)
            
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
            
        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

#Determine the percentage of votes for each candidate by looping through the counts
# 1. Iterate throught the candidate list.
for candidate_name in candidate_votes:
   # 2. Retrieve vote count of a candidate. 
   votes = candidate_votes[candidate_name] 
   # 3. Calculate the percentage of votes
   vote_percentage=float(votes)/float(total_votes)*100

   # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.   
   print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
   
   # Determine winning vote count and candidate
   # Determine if the votes is greater than the winning count.
   if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)