"""
Prac 09 - Testing Taxi
"""

from prac_09.taxi import Taxi

def main():
    """ Testing Taxi class. """
    taxi = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)
    taxi.drive(40)
    print(taxi)
    print(taxi.get_fare())

    taxi.start_fare() # Start new fare
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())



main()