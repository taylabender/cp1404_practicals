"""
Wimbledon champions data
"""

# Read and analyse CSV file
FILENAME = 'wimbledon.csv'
COUNTRY = 1
CHAMPION = 2

def main():
    records = get_records_from_file()
    champion_count, countries = create_dictionary(records)
    print_results(champion_count, countries)


def get_records_from_file():
    records = []
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def create_dictionary(records):
    # Create dictionary of champions and their wins
    champion_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY])
        champion_count[record[CHAMPION]] = champion_count.get(record[CHAMPION], 0) + 1
    return champion_count, countries


def print_results(champion_count, countries):
    """Display champions and their wins"""
    print("Wimbledon Champions:")
    for name, count in champion_count.items():
        print(f"{name:18} - {count}")

    """Display countries"""
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()


