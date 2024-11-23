"""
Prac_08 Dynamic Labels
Estimate time: 45 minutes
Actual time: 20 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from random import random



class DynamicLabelsApp(App):
    """ Kivy app to demo dynamic widget creation"""
    message = StringProperty()

    def __init__(self, **kwargs):
        """ Construct app. """
        super(DynamicLabelsApp, self).__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """ Build app. """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """ Create dynamic labels from a list and set text colour to random colour"""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (random(), random(), random(), 1)
            temp_label.font_size = 45
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()