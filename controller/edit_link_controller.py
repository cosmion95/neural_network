from PyQt5 import QtWidgets
from view import edit_link_window
import values


class EditLinkController():
    def __init__(self):
        self.EditLinkWindow = QtWidgets.QMainWindow()
        self.EditLinkContent = edit_link_window.Ui_EditLinkWindow()
        self.EditLinkContent.setupUi(self.EditLinkWindow)
        self.fromNeuron = None
        self.toNeuron = None
        self.currentLinkValue = None
        self.currentHiddenLayer = None

    def initWindowFrom(self, fromNeuronID, toNeuronID):
        self.currentHiddenLayer = values.currentHiddenLayer - 1
        self.fromNeuron = values.findHiddenLayerNeuronByID(self.currentHiddenLayer, fromNeuronID)
        self.toNeuron = values.findHiddenLayerNeuronByID(self.currentHiddenLayer+1, toNeuronID)
        self.currentLinkValue = self.fromNeuron.getLinkValue(self.toNeuron)
        self.EditLinkContent.from_value_label.setText(self.fromNeuron.name)
        self.EditLinkContent.to_value_label.setText(self.toNeuron.name)
        self.EditLinkContent.value_sb.setValue(self.currentLinkValue)
        self.EditLinkWindow.show()

    def initWindowTo(self, fromNeuronID, toNeuronID):
        self.currentHiddenLayer = values.currentHiddenLayer
        self.fromNeuron = values.findHiddenLayerNeuronByID(self.currentHiddenLayer, fromNeuronID)
        self.toNeuron = values.findHiddenLayerNeuronByID(self.currentHiddenLayer+1, toNeuronID)
        self.currentLinkValue = self.fromNeuron.getLinkValue(self.toNeuron)
        self.EditLinkContent.from_value_label.setText(self.fromNeuron.name)
        self.EditLinkContent.to_value_label.setText(self.toNeuron.name)
        self.EditLinkContent.value_sb.setValue(self.currentLinkValue)
        self.EditLinkWindow.show()

    def okButtonPressed(self):
        if self.currentLinkValue != self.EditLinkContent.value_sb.value():
            values.modifyLayerLinkValue(self.currentHiddenLayer, self.fromNeuron.id, self.toNeuron.id, self.EditLinkContent.value_sb.value())
            self.currentLinkValue = self.EditLinkContent.value_sb.value()
        self.EditLinkWindow.close()