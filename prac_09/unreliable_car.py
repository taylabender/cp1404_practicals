"""
Prac 09 - Unreliable car
"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """ Add reliability to Car string. """
        return f"{super().__str__()}, reliability: {self.reliability})"

    def drive(self, distance):
        """ Generate a random number between 0 and 100 for the car's reliability."""
        if random.uniform(0, 100) < self.reliability:
            super().drive(distance)
        else:
            return 0