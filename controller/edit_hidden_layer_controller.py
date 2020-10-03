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

    def addSynapticLinks(self):
        self.editHiddenLayerContent.synaptic_links_from.clear()
        self.editHiddenLayerContent.synaptic_links_to.clear()
        links = values.getLinksFromPreviousLayer(self.neuron)
        for link in links:
            self.editHiddenLayerContent.synaptic_links_from.insertItem(link[0].id, link[0].name + ": i - " + str(link[0].value) + "   w - " + str(link[1]))
        for link in self.neuron.links:
            self.editHiddenLayerContent.synaptic_links_to.insertItem(link.neuron.id, link.neuron.name + ": w - " + str(link.value))
    
    def addSynapticLinksOutput(self):
        self.editHiddenLayerContent.synaptic_links_from.clear()
        self.editHiddenLayerContent.synaptic_links_to.clear()
        links = values.getLinksFromPreviousLayer(self.neuron)
        for link in links:
            self.editHiddenLayerContent.synaptic_links_from.insertItem(link[0].id, link[0].name + ": i - " + str(link[0].value) + "   w - " + str(link[1]))
       
    def setWindowValues(self):
        self.setComboBoxValues()
        self.editHiddenLayerContent.title_value_label.setText(self.neuron.name)
        self.editHiddenLayerContent.teta_sb.setValue(self.neuron.teta)
        self.editHiddenLayerContent.a_sb.setValue(self.neuron.a)
        self.editHiddenLayerContent.g_sb.setValue(self.neuron.g)
        self.editHiddenLayerContent.binar_cb.setChecked(self.neuron.binar)
        self.setResultValues()
    
    def initWindow(self, hiddenLayerNr, neuronID):
        self.neuron = values.findHiddenLayerNeuronByID(hiddenLayerNr, neuronID)
        self.hiddenLayerNumber = hiddenLayerNr
        values.setCurrentHiddenLayer(hiddenLayerNr)
        self.editHiddenLayerContent.synaptic_links_to_label.show()
        self.editHiddenLayerContent.synaptic_links_to.show()
        self.setWindowValues()
        self.addSynapticLinks()
        self.editHiddenLayerWindow.show()

    def initWindowOutput(self, hiddenLayerNr, neuronID):
        self.neuron = values.findHiddenLayerNeuronByID(hiddenLayerNr, neuronID)
        self.hiddenLayerNumber = hiddenLayerNr
        values.setCurrentHiddenLayer(hiddenLayerNr)
        self.editHiddenLayerContent.synaptic_links_to_label.hide()
        self.editHiddenLayerContent.synaptic_links_to.hide()
        self.setWindowValues()
        self.addSynapticLinksOutput()
        self.editHiddenLayerWindow.show()


    def recalculateButtonPressed(self):
        if self.editHiddenLayerContent.teta_sb.value() != self.neuron.teta:
            self.neuron.teta = self.editHiddenLayerContent.teta_sb.value()
        if self.editHiddenLayerContent.a_sb.value() != self.neuron.a:
            self.neuron.a = self.editHiddenLayerContent.a_sb.value()
        if self.editHiddenLayerContent.g_sb.value() != self.neuron.g:
            self.neuron.g = self.editHiddenLayerContent.g_sb.value()
        if self.editHiddenLayerContent.binar_cb.checkState() != self.neuron.binar:
            self.neuron.binar = self.editHiddenLayerContent.binar_cb.checkState()
        if self.editHiddenLayerContent.entry_function_cb.currentIndex() != self.neuron.entry_function_id:
            self.neuron.entry_function_id = self.editHiddenLayerContent.entry_function_cb.currentIndex()
        if self.editHiddenLayerContent.activation_function_cb.currentIndex() != self.neuron.activation_function_id:
            self.neuron.activation_function_id = self.editHiddenLayerContent.activation_function_cb.currentIndex()
        self.neuron.calculateFunctions()
        self.neuron.calculateOutputValue()
        self.setResultValues()
    
    def okButtonPressed(self):
        self.editHiddenLayerWindow.hide()

    def windowDataChanged(self):
        values.calculateNeuralNetworkValues()
        self.setWindowValues()
        self.addSynapticLinks()