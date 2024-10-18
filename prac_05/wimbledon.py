"""
Wimbledon champions data
"""

# Read and analyse CSV file
FILENAME = 'wimbledon.csv'

records = []
with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        records.append(parts)
print(records)

# Create dictionary of champions and their wins
# Display champions and their wins
# Get unique countries and sort them
# convert set to sorted list
# Display countries

