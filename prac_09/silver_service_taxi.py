"""
Prac 09 - silver service taxi inherits from taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        super.__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """ Add flagfall fare to Taxi. """
        return f"{super().__str__()} plus flagfall fare of ${self.flagfall}"

    def get_fare(self):
        """ Get fare price for trip. """
        return super().get_fare() + self.flagfall