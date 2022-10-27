# Add our dependencies.
import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
# file_to_load = os.path.join("C:/Users/9G1/Desktop/UofT/assignment/Python_assignment/Election_Analysis/Resources/election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
winning_count = 0
winning_percentage = 0
largest_country_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
Country_names=[]
country_votes = {}
winning_candidate = ""
largest_country_turnout= ""


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        Country_name= row[1]

        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        if Country_name not in Country_names:
            Country_names.append(Country_name)
            country_votes[Country_name] = 0

        country_votes[Country_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    
    for country in country_votes:
        country_vote=country_votes[country]
        vote_percentage=(int(country_vote)/int(total_votes))*100
        country_results =(
            f"{country}: {vote_percentage:.1f}% ({country_vote:,})\n")                                                                                                                            
        print(country_results)
        txt_file.write(country_results)
        if country_vote > largest_country_votes:
            largest_country_votes = country_vote
            largest_country_turnout= country


    largest_turnout =(
    f"\n"
    f"-----------------------\n"
    f"Largest Country Turnour : {largest_country_turnout}\n"
    f"-----------------------\n"
    )
    print(largest_turnout)
    txt_file.write(largest_turnout)

    for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

       
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
