# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:

    # To do: Read and analyze the data her.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
  






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

