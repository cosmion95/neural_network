import values
from model import neuron_link
from functions import entry, activation

class Neuron:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.links = []
        self.entry_function_id = 0
        self.activation_function_id = 0
        self.teta = 0.0
        self.a = 1.0
        self.g = 1.0
        self.binar = False
        self.entry_function_value = 0.0
        self.activation_function_value = 0.0
        self.value = value

    def add_link(self, neuron, value):
        link = neuron_link.NeuronLink(neuron, value)
        self.links.append(link)

    def calculateFunctions(self):
        if values.findNeuronType(self.name) != 0:
            neuronLinks = values.getLinksTupleFromPreviousLayer(self)
            self.entry_function_value = values.calculateEntryFunction(self.entry_function_id, neuronLinks)
            self.activation_function_value = values.calculateActivationFunction(self)

    def calculateOutputValue(self):
        if values.findNeuronType(self.name) != 0:
            self.value = values.calculateOutputValue(self)

        