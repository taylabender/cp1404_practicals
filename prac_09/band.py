"""
Prac 09 - Band class for my_band program
"""

class Band():
    def __init__(self, name=""):
        self.name = name
        self.musician = []

    def __str__(self):
        """ Return string representation of Band object. """
        band_string = f"{self.name} "
        musician_string = []
        for musician in self.musician:
            musician_string.append(f"{musician.name} ({musician.instruments})")
        band_string += f'({", ".join(musician_string)})'
        return band_string

    def add(self, musician):
        """ Add musician to Band object. """
        self.musician.append(musician)

    def play(self):
        """ Return """
        band_string = ""
        for musician in self.musician:
            if not musician.instruments:
                band_string += f"{musician.name} needs an instrument!\n"
            else:
                band_string += f"{musician.name} is playing: {musician.instruments[0]}\n"
        return band_string

