
class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise programming language.
            name: Name of guitar
            year: Year
            cost: Cost of guitar
            """
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """ Determine age of guitar. """
        year = self.year
        current_year = 2024
        return current_year - year

    def is_vintage(self):
        """Determine whether guitar is vintage."""
        return self.get_age() >= 50

    def __str__(self):
        """Return a string representation of guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """ Compare objects by year"""
        return self.get_age() < other.get_age()