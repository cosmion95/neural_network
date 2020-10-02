from PyQt5 import QtWidgets
from view import edit_input_layer_window
import values

class EditInputLayerController():
    def __init__(self):
        self.editInputLayerWindow = QtWidgets.QMainWindow()
        self.editInputLayerContent = edit_input_layer_window.Ui_EditInputLayerWindow()
        self.editInputLayerContent.setupUi(self.editInputLayerWindow)
        self.neuron = None
 
    def clearSinaptics(self):
        self.editInputLayerContent.sinaptics_listWidget.clear()

    def okButtonPressed(self):
        valueHasChanged = False
        if self.neuron.value != self.editInputLayerContent.value_sb.value():
            values.modifyInputLayerNeuronValue(self.neuron.id, self.editInputLayerContent.value_sb.value())
            self.neuron.value = self.editInputLayerContent.value_sb.value()
            valueHasChanged = True
        self.editInputLayerWindow.close()
        return (valueHasChanged, self.neuron)

    def initWindow(self, neuronID):
        self.clearSinaptics()
        self.neuron = values.findInputLayerNeuronByID(neuronID)
        self.editInputLayerContent.neuron_name.setText(self.neuron.name)
        self.editInputLayerContent.value_sb.setValue(self.neuron.value)
        for link in self.neuron.links:
            self.editInputLayerContent.sinaptics_listWidget.insertItem(link.neuron.id, link.neuron.name + " --- " + str(link.value))
        self.editInputLayerWindow.show()

    def inputLayerLinkChanged(self, neuron, newValue):
        self.editInputLayerContent.sinaptics_listWidget.item(neuron.id).setText(neuron.name + " --- " + str(newValue))

    