"""
Project class
"""
from datetime import datetime



class Project:
    def __init__(self, name="", start_date="", priority=0, cost=0.0, percentage=100):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __repr__(self):
        """Return a string representation of project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, Estimate: ${self.cost:.2f}, completion:{self.percentage:}%"

