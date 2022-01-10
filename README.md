# Election_Analysis

## Project Overview
There has been a recent local congressional election in Colorado and a Colorado Board of Elections Office (CBE) employee has requested an audit be done using python as the analysis tool of choice. The requested audit details are as follows:

1. Calculate the total number of votes cast.
2. Obtain a list of all of the candidates who recieved votes.
3. Calculate the total number of votes each of the candidates recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Format a text document which can be delivered to the Election Commission summarizing the results.

## Resources Used
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.63.2

## Challenge Overview
In addition to the auddit results for the candidates, the election commision has requested some additional data to complete the audit:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Election Audit Results

- The total number of votes that were cast in this election were 369,711.
  
- A breakdown of the percentage of total votes and the number of votes for each county in the precinct:
  - Jefferson County cast 10.5% of the total vote with 38,855 votes.
  - Denver County cast 82.8% of the votes with 306,055 votes
  - Arapahoe County cast 6.7% of the votes with 24,801 votes

- Which county had the largest number of votes?
  - Denver County had the largest number of votes, making up 82.8% (306,055 out of 369,711 votes) of the total number of votes.
  
- A breakdown of the percentage of total votes and the number of votes each candidate received:
  - The candidate results were:
    - Charles Casper Stockam received 23.0% of the vote and 85,213 votes
    - Diana DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes 

### -The winner of the election was Diana Degette who recieved 73.8% of the vote and 272,892 votes

## Election Audit Summary

Using Python to achieve the audit of the election results has produced an analysis tool that can dynamically handle any election at the state level in which any number of candidates and counties can be included. In the case of analyzing multiple elections simultaneously, each election would have to be ran independently as this version of the python program cannot run multiple elections at once. This means that if there is more than one election data file, or multiple election results within one data file, the python script would not currently produce results. As written, the python script also cannot achieve analysis of the votes cast for a candidate from each county. This tool will also not run a national level election audit as it is currently written to report data on counties and not states.

Working with this auditing script as a foundation, these features could easily be added into the analysis making this approach to auditing election data more robust. To automate the results from multiple elections if each election has it's own data file, the script could step through each file from a list of the files generated inside the script in a for loop and write out the results to a text file specific to that election. Additionally, to retreave the number of votes from each county for each candidate, a conditional statement within a for loop on a list of candidate options checking if each vote is a vote for the candidate and if so, tally the vote under the county that it was cast in for each iteration of the candidates would achieve this. Lastly, if national level election results were desired, the substitution of "county" parameters with "state" parameters throughout the script would handle this.
