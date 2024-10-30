"""
Estimate time: 30 min
Actual time:
"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="True", year=0):
        """Initialise programming language.
        name: Name of string
        typing: Static or Dynamic
        reflection: True or False
        year: Year
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = 0

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name} {self.typing} {self.reflection}, First appeared in {self.year}"
