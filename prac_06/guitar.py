"""
Estimate time: 30 min
Actual time:
"""

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
        self.year = 2024 - int(self.year)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"