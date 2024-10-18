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
champion_count = {}
countries = set()
for record in records:
    champion = record[1]  # Adjust index based on actual CSV structure
    if champion in champion_count:
        champion_count[champion] += 1
    else:
        champion_count[champion] = 1

# Display champions and their wins
print("Wimbledon Champions:")
for champion, wins in champion_count.items():
    print(f"{champion} {wins}")

# Get unique countries and sort them
# convert set to sorted list
# Display countries

