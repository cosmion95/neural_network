from PyQt5 import QtWidgets
from view import edit_hidden_layer_window
import values

class EditHiddenLayerController():
    def __init__(self):
        self.editHiddenLayerWindow = QtWidgets.QMainWindow()
        self.editHiddenLayerContent = edit_hidden_layer_window.Ui_EditHiddenLayerWindow()
        self.editHiddenLayerContent.setupUi(self.editHiddenLayerWindow)
        self.neuron = None
        self.hiddenLayerNumber = None

    def setResultValues(self):
        self.editHiddenLayerContent.entry_function_result_value.setText(str(self.neuron.entry_function_value))
        self.editHiddenLayerContent.activation_function_result_value.setText(str(self.neuron.activation_function_value))
        self.editHiddenLayerContent.output_value.setText(str(self.neuron.value))

    def setComboBoxValues(self):
        self.editHiddenLayerContent.entry_function_cb.clear()
        self.editHiddenLayerContent.activation_function_cb.clear()
        for entry_function in values.entry_functions:
            self.editHiddenLayerContent.entry_function_cb.addItem(entry_function[1])
        for activation_function in values.activation_functions:
            self.editHiddenLayerContent.activation_function_cb.addItem(activation_function[1])
        self.editHiddenLayerContent.entry_function_cb.setCurrentIndex(self.neuron.entry_function_id)
        self.editHiddenLayerContent.activation_function_cb.setCurrentIndex(self.neuron.activation_function_id)

    def initWindow(self, hiddenLayerNr, neuronID):
        self.neuron = values.findHiddenLayerNeuronByID(hiddenLayerNr, neuronID)
        self.setComboBoxValues()
        self.hiddenLayerNumber = hiddenLayerNr
        self.editHiddenLayerContent.title_value_label.setText(self.neuron.name)
        self.editHiddenLayerContent.teta_sb.setValue(self.neuron.teta)
        self.editHiddenLayerContent.a_sb.setValue(self.neuron.a)
        self.editHiddenLayerContent.g_sb.setValue(self.neuron.g)
        self.editHiddenLayerContent.binar_cb.setCheckable(self.neuron.binar)
        self.setResultValues()
        self.editHiddenLayerWindow.show()

    def changeEntryFunction(self):
        functionID = self.editHiddenLayerContent.entry_function_cb.currentIndex()
        self.neuron.entry_function_id = functionID

    def changeActivationFunction(self):
        functionID = self.editHiddenLayerContent.activation_function_cb.currentIndex()
        self.neuron.activation_function_id = functionID