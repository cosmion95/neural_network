from PyQt5 import QtWidgets
from view import visualize_window
import values

class VisualizeController():
    def __init__(self):
        self.visualizeWindow = QtWidgets.QMainWindow()
        self.visualizeContent = visualize_window.Ui_VisualizeWindow()
        self.visualizeContent.setupUi(self.visualizeWindow)
        self.selectedNeuron = None

    def resizeWindow(self):
        if values.withHL2:
            if not values.withHL3:
                self.visualizeContent.hl3_label.hide()
                self.visualizeContent.hl3_listWidget.hide()
                self.visualizeContent.entry_function_label_hl3.hide()
                self.visualizeContent.entry_function_cb_hl3.hide()
                self.visualizeContent.activation_function_label_hl3.hide()
                self.visualizeContent.activation_function_cb_hl3.hide()
                self.visualizeContent.teta_label_hl3.hide()
                self.visualizeContent.teta_sb_hl3.hide()
                self.visualizeContent.a_label_hl3.hide()
                self.visualizeContent.a_sb_hl3.hide()
                self.visualizeContent.g_label_hl3.hide()
                self.visualizeContent.g_sb_hl3.hide()
                self.visualizeContent.binar_label_hl3.hide()
                self.visualizeContent.binar_cb_hl3.hide()
                self.visualizeContent.entry_function_label_ol.setGeometry(self.visualizeContent.entry_function_label_hl3.geometry())
                self.visualizeContent.entry_function_cb_ol.setGeometry(self.visualizeContent.entry_function_cb_hl3.geometry())
                self.visualizeContent.activation_function_label_ol.setGeometry(self.visualizeContent.activation_function_label_hl3.geometry())
                self.visualizeContent.activation_function_cb_ol.setGeometry(self.visualizeContent.activation_function_cb_hl3.geometry())
                self.visualizeContent.teta_label_ol.setGeometry(self.visualizeContent.teta_label_hl3.geometry())
                self.visualizeContent.teta_sb_ol.setGeometry(self.visualizeContent.teta_sb_hl3.geometry())
                self.visualizeContent.a_label_ol.setGeometry(self.visualizeContent.a_label_hl3.geometry())
                self.visualizeContent.a_sb_ol.setGeometry(self.visualizeContent.a_sb_hl3.geometry())
                self.visualizeContent.g_label_ol.setGeometry(self.visualizeContent.g_label_hl3.geometry())
                self.visualizeContent.g_sb_ol.setGeometry(self.visualizeContent.g_sb_hl3.geometry())
                self.visualizeContent.binar_label_ol.setGeometry(self.visualizeContent.binar_label_hl3.geometry())
                self.visualizeContent.binar_cb_ol.setGeometry(self.visualizeContent.binar_cb_hl3.geometry())
                self.visualizeContent.recalculate_button.resize(self.visualizeContent.recalculate_button.width() - self.visualizeContent.hl3_listWidget.width(), self.visualizeContent.recalculate_button.height())
                self.visualizeContent.output_listWidget.setGeometry(self.visualizeContent.hl3_listWidget.geometry())
                self.visualizeContent.output_label.setGeometry(self.visualizeContent.hl3_label.geometry())
                self.visualizeWindow.resize(self.visualizeWindow.width() - self.visualizeContent.hl3_listWidget.width(), self.visualizeWindow.height())
        else:
            self.visualizeContent.hl2_label.hide()
            self.visualizeContent.hl2_listWidget.hide()
            self.visualizeContent.hl3_label.hide()
            self.visualizeContent.hl3_listWidget.hide()
            self.visualizeContent.entry_function_label_hl3.hide()
            self.visualizeContent.entry_function_cb_hl3.hide()
            self.visualizeContent.activation_function_label_hl3.hide()
            self.visualizeContent.activation_function_cb_hl3.hide()
            self.visualizeContent.teta_label_hl3.hide()
            self.visualizeContent.teta_sb_hl3.hide()
            self.visualizeContent.a_label_hl3.hide()
            self.visualizeContent.a_sb_hl3.hide()
            self.visualizeContent.g_label_hl3.hide()
            self.visualizeContent.g_sb_hl3.hide()
            self.visualizeContent.binar_label_hl3.hide()
            self.visualizeContent.binar_cb_hl3.hide()
            self.visualizeContent.entry_function_label_hl2.hide()
            self.visualizeContent.entry_function_cb_hl2.hide()
            self.visualizeContent.activation_function_label_hl2.hide()
            self.visualizeContent.activation_function_cb_hl2.hide()
            self.visualizeContent.teta_label_hl2.hide()
            self.visualizeContent.teta_sb_hl2.hide()
            self.visualizeContent.a_label_hl2.hide()
            self.visualizeContent.a_sb_hl2.hide()
            self.visualizeContent.g_label_hl2.hide()
            self.visualizeContent.g_sb_hl2.hide()
            self.visualizeContent.binar_label_hl2.hide()
            self.visualizeContent.binar_cb_hl2.hide()
            self.visualizeContent.entry_function_label_ol.setGeometry(self.visualizeContent.entry_function_label_hl2.geometry())
            self.visualizeContent.entry_function_cb_ol.setGeometry(self.visualizeContent.entry_function_cb_hl2.geometry())
            self.visualizeContent.activation_function_label_ol.setGeometry(self.visualizeContent.activation_function_label_hl2.geometry())
            self.visualizeContent.activation_function_cb_ol.setGeometry(self.visualizeContent.activation_function_cb_hl2.geometry())
            self.visualizeContent.teta_label_ol.setGeometry(self.visualizeContent.teta_label_hl2.geometry())
            self.visualizeContent.teta_sb_ol.setGeometry(self.visualizeContent.teta_sb_hl2.geometry())
            self.visualizeContent.a_label_ol.setGeometry(self.visualizeContent.a_label_hl2.geometry())
            self.visualizeContent.a_sb_ol.setGeometry(self.visualizeContent.a_sb_hl2.geometry())
            self.visualizeContent.g_label_ol.setGeometry(self.visualizeContent.g_label_hl2.geometry())
            self.visualizeContent.g_sb_ol.setGeometry(self.visualizeContent.g_sb_hl2.geometry())
            self.visualizeContent.binar_label_ol.setGeometry(self.visualizeContent.binar_label_hl2.geometry())
            self.visualizeContent.binar_cb_ol.setGeometry(self.visualizeContent.binar_cb_hl2.geometry())
            self.visualizeContent.recalculate_button.resize(self.visualizeContent.recalculate_button.width() - self.visualizeContent.hl3_listWidget.width()*2, self.visualizeContent.recalculate_button.height())
            self.visualizeContent.output_listWidget.setGeometry(self.visualizeContent.hl2_listWidget.geometry())
            self.visualizeContent.output_label.setGeometry(self.visualizeContent.hl2_label.geometry())
            self.visualizeWindow.resize(self.visualizeWindow.width() - (self.visualizeContent.hl3_listWidget.width()*2), self.visualizeWindow.height())
    
    def clearLists(self):
        self.visualizeContent.input_listWidget.clear()
        self.visualizeContent.hl1_listWidget.clear()
        self.visualizeContent.hl2_listWidget.clear()
        self.visualizeContent.hl3_listWidget.clear()
        self.visualizeContent.output_listWidget.clear()
    
    def setComboBoxValues(self):
        self.visualizeContent.entry_function_cb_hl1.clear()
        self.visualizeContent.entry_function_cb_hl2.clear()
        self.visualizeContent.entry_function_cb_hl3.clear()
        self.visualizeContent.entry_function_cb_ol.clear()
        self.visualizeContent.activation_function_cb_hl1.clear()
        self.visualizeContent.activation_function_cb_hl2.clear()
        self.visualizeContent.activation_function_cb_hl3.clear()
        self.visualizeContent.activation_function_cb_ol.clear()
        for entry_function in values.entry_functions:
            self.visualizeContent.entry_function_cb_hl1.addItem(entry_function[1])
            if values.withHL2: 
                self.visualizeContent.entry_function_cb_hl2.addItem(entry_function[1])
            if values.withHL3: 
                self.visualizeContent.entry_function_cb_hl3.addItem(entry_function[1])
            self.visualizeContent.entry_function_cb_ol.addItem(entry_function[1])
        for activation_function in values.activation_functions:
            self.visualizeContent.activation_function_cb_hl1.addItem(activation_function[1])
            if values.withHL2: 
                self.visualizeContent.activation_function_cb_hl2.addItem(activation_function[1])
            if values.withHL3: 
                self.visualizeContent.activation_function_cb_hl3.addItem(activation_function[1])
            self.visualizeContent.activation_function_cb_ol.addItem(activation_function[1])
        self.visualizeContent.entry_function_cb_hl1.setCurrentIndex(values.HL1[0].entry_function_id)
        if values.withHL2: 
            self.visualizeContent.entry_function_cb_hl2.setCurrentIndex(values.HL2[0].entry_function_id)
        if values.withHL3: 
            self.visualizeContent.entry_function_cb_hl3.setCurrentIndex(values.HL3[0].entry_function_id)
        self.visualizeContent.entry_function_cb_ol.setCurrentIndex(values.OL[0].entry_function_id)
        self.visualizeContent.activation_function_cb_hl1.setCurrentIndex(values.HL1[0].activation_function_id)
        if values.withHL2: 
            self.visualizeContent.activation_function_cb_hl2.setCurrentIndex(values.HL2[0].activation_function_id)
        if values.withHL3: 
            self.visualizeContent.activation_function_cb_hl3.setCurrentIndex(values.HL3[0].activation_function_id)
        self.visualizeContent.activation_function_cb_ol.setCurrentIndex(values.OL[0].activation_function_id)

    def setVariablesValues(self):
        self.visualizeContent.teta_sb_hl1.setValue(values.HL1[0].teta)
        if values.withHL2:
            self.visualizeContent.teta_sb_hl2.setValue(values.HL2[0].teta)
        if values.withHL3:
            self.visualizeContent.teta_sb_hl3.setValue(values.HL3[0].teta)
        self.visualizeContent.teta_sb_ol.setValue(values.OL[0].teta)
        self.visualizeContent.a_sb_hl1.setValue(values.HL1[0].a)
        if values.withHL2:
            self.visualizeContent.a_sb_hl2.setValue(values.HL2[0].a)
        if values.withHL3:
            self.visualizeContent.a_sb_hl3.setValue(values.HL3[0].a)
        self.visualizeContent.a_sb_ol.setValue(values.OL[0].a)
        self.visualizeContent.g_sb_hl1.setValue(values.HL1[0].g)
        if values.withHL2:
            self.visualizeContent.g_sb_hl2.setValue(values.HL2[0].g)
        if values.withHL3:
            self.visualizeContent.g_sb_hl3.setValue(values.HL3[0].g)
        self.visualizeContent.g_sb_ol.setValue(values.OL[0].g)
        self.visualizeContent.binar_cb_hl1.setChecked(values.HL1[0].binar)
        if values.withHL2:
            self.visualizeContent.binar_cb_hl2.setChecked(values.HL2[0].binar)
        if values.withHL3:
            self.visualizeContent.binar_cb_hl3.setChecked(values.HL3[0].binar)
        self.visualizeContent.binar_cb_ol.setChecked(values.OL[0].binar)
        self.visualizeContent.selected_neuron_widget.hide()
        self.visualizeContent.selected_input_neuron_widget.setGeometry(self.visualizeContent.selected_neuron_widget.geometry())
        self.visualizeContent.selected_input_neuron_widget.hide()
        self.visualizeContent.selected_neuron_value.setText("")

    def setResultValues(self):
        self.visualizeContent.selected_neuron_value.setText(self.selectedNeuron.name)
        self.visualizeContent.selected_neuron_entry_function_value.setText(str(self.selectedNeuron.entry_function_value))
        self.visualizeContent.selected_neuron_activation_function_value.setText(str(self.selectedNeuron.activation_function_value))
        self.visualizeContent.selected_neuron_output_value.setText(str(self.selectedNeuron.value))
        self.visualizeContent.selected_input_neuron_value.setValue(self.selectedNeuron.value)

    def neuronClicked(self, layerNR, neuronID):
        neuron = values.findHiddenLayerNeuronByID(layerNR, neuronID)
        self.selectedNeuron = neuron
        self.setResultValues()
        self.visualizeContent.selected_input_neuron_widget.hide()
        self.visualizeContent.selected_neuron_widget.show()

    def inputNeuronClicked(self, neuronID):
        neuron = values.findInputLayerNeuronByID(neuronID)
        self.selectedNeuron = neuron
        self.setResultValues()
        self.visualizeContent.selected_neuron_widget.hide()
        self.visualizeContent.selected_input_neuron_widget.show()
    
    def addNeuronsToLists(self):
        for inputNeuron in values.IL:
            self.visualizeContent.input_listWidget.insertItem(inputNeuron.id, inputNeuron.name + ": i - " + str(inputNeuron.value))
        for hiddenNeuron in values.HL1:
            self.visualizeContent.hl1_listWidget.insertItem(hiddenNeuron.id, hiddenNeuron.name + ": i - " + str(hiddenNeuron.value))
        if values.withHL2:
            for hiddenNeuron in values.HL2:
                self.visualizeContent.hl2_listWidget.insertItem(hiddenNeuron.id, hiddenNeuron.name + ": i - " + str(hiddenNeuron.value))
            if values.withHL3:
                for hiddenNeuron in values.HL3:
                    self.visualizeContent.hl3_listWidget.insertItem(hiddenNeuron.id, hiddenNeuron.name + ": i - " + str(hiddenNeuron.value))
        for outputNeuron in values.OL:
            self.visualizeContent.output_listWidget.insertItem(outputNeuron.id, outputNeuron.name + ": i - " + str(outputNeuron.value))
        
    
    def initWindow(self):
        self.addNeuronsToLists()
        self.setComboBoxValues()
        self.setVariablesValues()
        self.resizeWindow()
        self.visualizeWindow.show()

    def windowDataChanged(self):
        values.calculateNeuralNetworkValues()
        self.clearLists()
        self.addNeuronsToLists()
        self.setResultValues()

    def recalculatePressed(self):
        for neuron in values.HL1:
            neuron.entry_function_id = self.visualizeContent.entry_function_cb_hl1.currentIndex()
            neuron.activation_function_id = self.visualizeContent.activation_function_cb_hl1.currentIndex()
            neuron.teta = self.visualizeContent.teta_sb_hl1.value()
            neuron.a = self.visualizeContent.a_sb_hl1.value()
            neuron.g = self.visualizeContent.g_sb_hl1.value()
            neuron.binar = self.visualizeContent.binar_cb_hl1.checkState()
        if values.withHL2: 
            for neuron in values.HL2:
                neuron.entry_function_id = self.visualizeContent.entry_function_cb_hl2.currentIndex()
                neuron.activation_function_id = self.visualizeContent.activation_function_cb_hl2.currentIndex()
                neuron.teta = self.visualizeContent.teta_sb_hl2.value()
                neuron.a = self.visualizeContent.a_sb_hl2.value()
                neuron.g = self.visualizeContent.g_sb_hl2.value()
                neuron.binar = self.visualizeContent.binar_cb_hl2.checkState()
        if values.withHL3:
            for neuron in values.HL3:
                neuron.entry_function_id = self.visualizeContent.entry_function_cb_hl3.currentIndex()
                neuron.activation_function_id = self.visualizeContent.activation_function_cb_hl3.currentIndex()
                neuron.teta = self.visualizeContent.teta_sb_hl3.value()
                neuron.a = self.visualizeContent.a_sb_hl3.value()
                neuron.g = self.visualizeContent.g_sb_hl3.value()
                neuron.binar = self.visualizeContent.binar_cb_hl3.checkState()
        for neuron in values.OL:
            neuron.entry_function_id = self.visualizeContent.entry_function_cb_ol.currentIndex()
            neuron.activation_function_id = self.visualizeContent.activation_function_cb_ol.currentIndex()
            neuron.teta = self.visualizeContent.teta_sb_ol.value()
            neuron.a = self.visualizeContent.a_sb_ol.value()
            neuron.g = self.visualizeContent.g_sb_ol.value()
            neuron.binar = self.visualizeContent.binar_cb_ol.checkState()
        self.windowDataChanged()

    def resetValues(self):
        values.resetValues()
        self.windowDataChanged()

    def reconfigureNetwork(self):
        values.reconfigureNetwork()
        self.visualizeWindow.hide()
