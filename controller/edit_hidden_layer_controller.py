from PyQt5 import QtWidgets
from view import edit_hidden_layer_window
import values

class EditHiddenLayerController():
    def __init__(self):
        self.editHiddenLayerLinkWindow = QtWidgets.QMainWindow()
        self.editHiddenLayerLinkContent = edit_hidden_layer_window.Ui_EditHiddenLayerWindow()
        self.editHiddenLayerLinkContent.setupUi(self.editHiddenLayerLinkWindow)
        self.neuron = None
        self.hiddenLayerNumber = None

    def initWindow(self, hiddenLayerNr, neuronID):
        self.neuron = values.findHiddenLayerNeuronByID(hiddenLayerNr, neuronID)
        self.hiddenLayerNumber = hiddenLayerNr
        self.editHiddenLayerLinkContent.title_value_label.setText(self.neuron.name)

        self.editHiddenLayerLinkWindow.show()