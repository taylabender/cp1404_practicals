"""
Prac 09 - Band class for my_band program
"""

class Band():
    def __init__(self, name=""):
        self.name = name
        self.musician = []

    def __str__(self):
        """ Return string representation of Band object """
        band_string = f"{self.name} "
        musician_string = []
        for musician in self.musician:
            musician_string.append(f"{musician.name} {musician.instruments}")
        band_string += ", ".join(musician_string)
        return band_string
