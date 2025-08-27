# --------------------------------------------------
# File Name : 10_TSD_JTP.py
# Problem   : Sports
# Author    : Worralop Srichainont
# Date      : 2025-08-15
# --------------------------------------------------

# Initialize dictionary to store favorite sports of each person
favorite_sports = {}


# Input favorite sports data
def input_favorite_sports_data(n):
    for _ in range(n):
        # Extract name and sports from input
        name, raw_sports = input().strip().split()
        sports = set(raw_sports.split(","))

        # Store the favorite sports of the current person in the dictionary
        favorite_sports[name] = sports


# Get common favorite sports between two people
def get_common_favorite_sports(name1, name2):
    sports1 = favorite_sports[name1]
    sports2 = favorite_sports[name2]
    return sorted(sports1 & sports2)


# Main function
def main():
    # Input favorite sports data
    n = int(input())
    input_favorite_sports_data(n)

    # Query for common favorite sports and display results
    while True:
        # Input until "q" is received
        raw_data = input().strip()
        if raw_data == "q":
            break

        # Extract names from input
        name1, name2 = raw_data.split()

        # Get and print common favorite sports
        print(get_common_favorite_sports(name1, name2))
