# Data that needs to be obtained:
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

#OLD FILE LOAD  SCRIPT
#{}{}}{}{}{}{}{}{{}{}{}{}{}}{{{{{{{{{{{{{}}}}}}}}}}}}}
#path to data: .\Resources\election_results.csv
# Assign a variable for the file to load and the path.
#file_to_load = '.\Resources\election_results.csv'

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
#     print(election_data)

#=======================================================
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

#==========================================================
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
# !!Not needed when using the with statement
# outfile = open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Counties in the Election")
     txt_file.write("\n-------------------------")
     txt_file.write("\nArapahoe\nDenver\nJefferson")

# Write some data to the file.
#outfile.write("Hello World")

# Close the file (not needed if using a with statement)
#outfile.close()