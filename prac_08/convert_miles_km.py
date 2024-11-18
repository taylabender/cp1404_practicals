"""
Estimate time: 30 minutes
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONSTANT = 1.61

class ConvertMilesKm(App):
    """ This class implements converting miles to kilometers"""
    message = StringProperty()

    def build(self):
        self.title = 'Miles to KM Converter'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ''
        return self.root

    def handle_conversion(self, value):
        try:
            miles = float(value)
            kilometers = miles * MILES_TO_KM_CONSTANT
            self.message = str(kilometers)
        except ValueError:
            self.message = 'Please enter a valid kilometer'

# Start the App
ConvertMilesKm().run()