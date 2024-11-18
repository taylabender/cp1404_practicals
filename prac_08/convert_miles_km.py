"""
Estimate time: 30 minutes
Actual time: 60 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONSTANT = 1.61

class ConvertMilesKm(App):
    """ This class implements converting miles to kilometers"""
    output_km = StringProperty()

    def build(self):
        """ Build the app"""
        self.title = 'Miles to KM Converter'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """ Convert miles to kilometers"""
        try:
            miles = float(text)
            self.output_km = str(miles * MILES_TO_KM_CONSTANT)
        except ValueError:
            self.output_km = "0.0"

    def handle_increment(self, text, increment):
        """ update value with up or down increments """
        try:
            self.root.ids.input_miles.text = str(float(text) + float(increment))
        except ValueError:
            self.root.ids.input_miles.text = increment


# Start the App
ConvertMilesKm().run()