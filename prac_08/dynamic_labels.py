"""
Prac_08 Dynamic Labels
Estimate time: 45 minutes
Actual time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty



class DynamicLabelsApp(App):


    def __init__(self, **kwargs):
        super(DynamicLabelsApp, self).__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]



DynamicLabelsApp().run()