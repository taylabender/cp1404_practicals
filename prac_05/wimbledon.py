"""
Wimbledon champions data
"""

# Read and analyse CSV file
FILENAME = 'wimbledon.csv'
COUNTRY = 1
CHAMPION = 2


records = []
with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        records.append(parts)


# Create dictionary of champions and their wins
champion_count = {}
countries = set()
for record in records:
    countries.add(record[COUNTRY])
    champion_count[record[CHAMPION]] = champion_count.get(record[CHAMPION], 0) + 1

# Display champions and their wins
print("Wimbledon Champions:")
for name, count in champion_count.items():
    print(f"{name:18} - {count}")

# Display countries
print(f"\nThese {len(countries)} countries have won Wimbledon: ")
print(", ".join(country for country in sorted(countries)))





