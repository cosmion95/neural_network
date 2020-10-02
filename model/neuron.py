from model import neuron_link
from functions import entry, activation

class Neuron:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.links = []
        self.entry_function = None
        self.activation_function = None
        self.teta = 0.0
        self.a = 0.0
        self.g = 0.0
        self.binar = False
        self.entry_function_value = 0.0
        self.activation_function_value = 0.0
        self.value = value

    def add_link(self, neuron, value):
        link = neuron_link.NeuronLink(neuron, value)
        self.links.append(link)

    #def calculate_entry_function(self):
        