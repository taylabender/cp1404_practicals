"""
Project class
"""
from datetime import datetime

class Project:
    def __init__(self, project="", start_date="", priority=0, cost=0.0, percentage=100):
        self.project = project
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __repr__(self):
        """Return a string representation of project."""
        return f"{self.project}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, Estimate: ${self.cost:.2f}, completion:{self.percentage:}%"

    def is_complete(self):
        """Return True if the project is 100% complete"""
        return self.percentage == 100

    def __lt__(self, other):
        """Less than (<) will compare priority for this class"""
        return self.priority < other.priority
