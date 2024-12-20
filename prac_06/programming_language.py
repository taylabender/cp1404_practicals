"""
Estimate time: 30 min
Actual time: 40 mins
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
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

