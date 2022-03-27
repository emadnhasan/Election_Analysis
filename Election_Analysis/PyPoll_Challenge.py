

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join(r"Resources\election_results.csv") 

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_county_vote = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:

    # Reader file   
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:
           
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1


# Functions
def getCountyWithLargestTurnout(county_votes):
    # Initialize a variable to hold the county with the largest turnout
    largest_county_turnout = ""

    # Initialize a variable to hold the largest turnout count
    largest_county_vote = 0

    # Loop through the county votes dictionary
    for county in county_votes:

        # Retrieve the vote count of the current county
        votes = county_votes[county]

        # If the votes are greater than the largest turnout count
        if (votes > largest_county_vote):

            # Set the largest turnout count = to the votes
            largest_county_vote = votes

            # Set the largest turnout county = to the county
            largest_county_turnout = county

    # Return the largest turnout county name
    return largest_county_turnout

def getWinner(candidate_votes):
    winner = ""
    highest_count = 0
    for candidate in candidate_votes:
        if candidate_votes[candidate] > highest_count:
            highest_count = candidate_votes[candidate]
            winner = candidate
    return winner



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    total_votes_str = '{:,}'.format(total_votes)

    # Print the final vote count (to terminal)
    election_results = (
        f"|------------------------------------------------------|\n"
        f"|-----------------| Election Results |-----------------|\n"
        f"|------------------------------------------------------|\n"
        f"| Total Votes:         {total_votes_str.rjust(27)}     |\n"
        f"|------------------------------------------------------|\n"
        f"| County Votes:                                        |\n")

    # Print Election Results
    print(election_results, end="")

    # ???
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:

        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]
        
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = vote_percentage_county = int(county_vote) / int(total_votes) * 100 

        # 6d: Format County Results & Print the county results to the terminal.
        county_res_str = f"{county_percentage:.1f}% ({county_vote:,})"
        county_result = (
            f"|  -> {str(county).ljust(12)}: {county_res_str.rjust(34)} |\n"
        )
        print(county_result, end="")
        
        # Write County Results to File
        txt_file.write(county_result)
          

# Reopen the analysis text in append mode
with open(file_to_save, "a") as txt_file:
    largest_county_turnout = getCountyWithLargestTurnout(county_votes)
    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
        f"|------------------------------------------------------|\n"
        f"| Largest County Turnout {largest_county_turnout.rjust(29)} |\n"
        f"|------------------------------------------------------|\n"
        f"|                                                      |\n"
        f"| Candidate Votes:                                     |\n"
    )
    # ???
    print(largest_county_turnout)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout)

    # print all candidate results to the terminal
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results_str = f"{vote_percentage:.1f}% ({votes:,})"
        candidate_results = (
            f"| {candidate.ljust(25)}: {candidate_results_str.rjust(25)} |\n")
    
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # 9: Write a function to determine the winner of the election.
    won_candidate = getWinner(candidate_votes)
    won_candidate_votes = candidate_votes[won_candidate]
    won_candidate_percentage = float(won_candidate_votes) / float(total_votes) * 100

    won_candidate_votes_str = '{:,}'.format(won_candidate_votes)
    won_candidate_percentage_str = '{:.1f}'.format(won_candidate_percentage)
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"|------------------------------------------------------|\n"
        f"| Winner -> {won_candidate.rjust(42)} |\n"
        f"| Winning Vote Count -> {won_candidate_votes_str.rjust(30)} |\n"
        f"| Winning Percentage > {won_candidate_percentage_str.rjust(30)}% |\n"
        f"|------------------------------------------------------|\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
