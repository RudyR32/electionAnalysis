# Objectives
# •	Total number of votes cast
# •	A complete list of candidates who received votes
# •	Total number of votes each candidate received
# •	Percentage of votes each candidate won
# •	The winner of the election based on popular vote


# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0 

# Candidate Option
candidate_options = []

# Candidate votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County Option
county_options = []

# County votes dictionary
county_votes = {}

# Largest County and Largest Count Tracker
largest_county = ""
largest_county_count = 0
largest_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        # Set county to index position 1
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Track the candidates vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidates count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county...
        if county_name not in county_options:

            # Add it to the list of county.
            county_options.append(county_name)

            # Track the county vote count
            county_votes[county_name] = 0

        # Add a vote to that county count.
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count in the terminal and Title for County Vote
    election_results =(
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n"
        f"\n"
        f"County Votes:\n"
        )
    # Mastery: All items listed in detailed rubric print to terminal.
    # Print the election results.
    print(election_results, end="")
    # Mastery: All items listed in detailed rubric save to the text file.
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# Determine the percentage of votes for each county by looping through the counts.
# Iterate through the county list.
    for county in county_votes:
        # Retrieve vote count of a candidate.
        ctvotes = county_votes[county]
        # Calculate the percentage of votes.
        ctvote_percentage = float(ctvotes) / float(total_votes) * 100

        # Create a variable for county results
        county_results = (f"{county}: {ctvote_percentage: .1f}%({ctvotes:,})\n")

        # Mastery: All items listed in detailed rubric print to terminal.
        # Print each county, its voter count and percentage to the terminal.
        print(county_results)

        # Mastery: All items listed in detailed rubric save to the text file.
        # Save the county results to the text file
        txt_file.write(county_results)

# Determine the winning county vote count and county.
# Determine if the votes are greater than the winning count (for county).
        if (ctvotes > largest_county_count) and (ctvote_percentage > largest_county_percentage):
            # If true then set largest_county_count = votes and largest_county_percentage = ctvote_percentage
            largest_county_count = ctvotes
            # Set the largest county equal to the county's name.
            largest_county = county
            largest_county_percentage = ctvote_percentage

    # Largest County summary
    largest_county_summary = (
        f"\n"
        f"----------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"----------------------\n")
    # Mastery: All items listed in detailed rubric print to terminal.
    # Print largest county summary
    print(largest_county_summary)
    # Mastery: All items listed in detailed rubric save to the text file.
    # Save the largest county's name to the text file.
    txt_file.write(largest_county_summary)             
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Create a variable for candidate results
        candidate_results = (f"{candidate}: {vote_percentage: .1f}%({votes:,})\n")

        # Mastery: All items listed in detailed rubric print to terminal.
        # Print each candidate, their voter count and percentage to the terminal.
        print(candidate_results)
        # Mastery: All items listed in detailed rubric save to the text file.
        # Save the candidate results to the text file
        txt_file.write(candidate_results)

# Determine the winning vote count and candidate.
# Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
            winning_percentage = vote_percentage
        

    # Winning candidate summary
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percent: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    # Mastery: All items listed in detailed rubric print to terminal.
    # Print winning candidate summary
    print(winning_candidate_summary)
    # Mastery: All items listed in detailed rubric save to the text file.
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)    
    


#Code used in the Module but not necessary for the Challenge

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
# Open the election results and read the file.
# election_data = open(file_to_load, 'r') First way to do this line
# with open(file_to_load) as election_data:

#     # To do : prefrom analysis.
#     print(election_data)
# Close the file
# election_data.close()

#   outfile.write("Hello World")
    # Write some data to the file.
    #.write("Hello World")
    # Write three counties to the file.
    # # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#  Write three counties to the file.
#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#     # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:# Close the file
# outfile.close()
    # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)
# # Using the with statement open the file as a text file.
# with open(file_to_load) as election_data:

#     # To do: Read and analyze the data her.
# #     file_reader = csv.reader(election_data)

#     # Print the header row.
#     headers = next(file_reader)
#     print(headers)
# Print the totla votes.
# print(total_votes)
# # Print the candidate list.
# print(candidate_options)
# # Print the candidate list.
# print(candidate_votes)
# Print the candidate name and percentage of votes.
        # print(f"{candidate}: received {vote_percentage: .1f}% of the vote.")
# Print oun the winning candidate, vote count and percentage to the terminal         
    # print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
# Print the candidate name and percentage of votes.
        # print(f"{candidate}: received {vote_percentage: .1f}% of the vote.")