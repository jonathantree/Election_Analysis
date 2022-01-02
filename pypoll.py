# Data that needs to be obtained:
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote


#=======================================================
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Candidate options variable
candidate_options = []

#Set up empty dictionary to capture the votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
     print("helo")

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # Print the header row.
     headers = next(file_reader)
     #print(headers)

     # Print each row in the CSV file.
     for row in file_reader:
                    
          #Increment the total vote count
          total_votes += 1
          
          # Print the candidate name from each row
          candidate_name = row[2]

          # If statement to exctract the unique candidate names and taly their votes
          if candidate_name not in candidate_options:
               
               # Add it to the list of candidates.
               candidate_options.append(candidate_name)
               
               # 2. Begin tracking that candidate's vote count and store it in the candidate_vote dictionary.
               candidate_votes[candidate_name] = 0

          # Add a vote to that candidate's count.
          candidate_votes[candidate_name] += 1
          
# 3. Print the total votes.
#print(total_votes)

# Print the candidate list
# One liner to exctract the unique name list from the candidate_options list
# candidate_options = list(set(candidate_options))
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:

     # 2. Retrieve vote count of a candidate.
     votes = candidate_votes[candidate_name]

     # 3. Calculate the percentage of votes.
     vote_percentage = float(votes) / float(total_votes) * 100

     # 4. Print the candidate name and percentage of votes.
     # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
     
     # print out each candidate's name, vote count, and percentage of
     # votes to the terminal.
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     
     # Determine winning vote count and candidate
     # Determine if the votes is greater than the winning count.
     if (votes > winning_count) and (vote_percentage > winning_percentage):
          # If true then set winning_count = votes and winning_percent =
          # vote_percentage.
          winning_count = votes
          winning_percentage = vote_percentage
          # And, set the winning_candidate equal to the candidate's name.
          winning_candidate = candidate_name
     
     #Print out the winning candidate summary
     winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Counties in the Election")
     txt_file.write("\n-------------------------")
     txt_file.write("\nArapahoe\nDenver\nJefferson")