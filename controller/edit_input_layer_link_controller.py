from PyQt5 import QtWidgets
from view import edit_input_layer_link_window
import values


class EditInputLayerLinkController():
    def __init__(self):
        self.editInputLayerLinkWindow = QtWidgets.QMainWindow()
        self.editInputLayerLinkContent = edit_input_layer_link_window.Ui_EditInputLayerLinkWindow()
        self.editInputLayerLinkContent.setupUi(self.editInputLayerLinkWindow)
        self.fromNeuron = None
        self.toNeuron = None
        self.currentLinkValue = None

    def initWindow(self, fromNeuronID, toNeuronID):
        self.fromNeuron = values.findInputLayerNeuronByID(fromNeuronID)
        self.toNeuron = values.findHL1NeuronByID(toNeuronID)
        self.currentLinkValue = values.getInputLayerLinkValue(fromNeuronID, toNeuronID)
        self.editInputLayerLinkContent.from_value_label.setText(self.fromNeuron.name)
        self.editInputLayerLinkContent.to_value_label.setText(self.toNeuron.name)
        self.editInputLayerLinkContent.value_sb.setValue(self.currentLinkValue)
        self.editInputLayerLinkWindow.show()

    def okButtonPressed(self):
        valueHasChanged = False
        if self.currentLinkValue != self.editInputLayerLinkContent.value_sb.value():
            values.modifyInputLayerLinkValue(self.fromNeuron.id, self.toNeuron.id, self.editInputLayerLinkContent.value_sb.value())
            self.currentLinkValue = self.editInputLayerLinkContent.value_sb.value()
            valueHasChanged = True
        self.editInputLayerLinkWindow.close()
        return (valueHasChanged, (self.toNeuron, self.editInputLayerLinkContent.value_sb.value()))