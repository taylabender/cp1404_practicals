"""
Prac 09 - Silver service taxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Taxi", 100, 2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())


