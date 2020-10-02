from PyQt5 import QtWidgets
from view import visualize_window
import values

class VisualizeController():
    def __init__(self):
        self.visualizeWindow = QtWidgets.QMainWindow()
        self.visualizeContent = visualize_window.Ui_VisualizeWindow()
        self.visualizeContent.setupUi(self.visualizeWindow)

    def resizeWindow(self):
        if values.withHL2:
            if not values.withHL3:
                self.visualizeContent.hl3_label.hide()
                self.visualizeContent.hl3_listWidget.hide()
                self.visualizeContent.output_listWidget.setGeometry(self.visualizeContent.hl3_listWidget.geometry())
                self.visualizeContent.output_label.setGeometry(self.visualizeContent.hl3_label.geometry())
                self.visualizeWindow.resize(self.visualizeWindow.width() - self.visualizeContent.hl3_listWidget.width(), self.visualizeWindow.height())
        else:
            self.visualizeContent.hl2_label.hide()
            self.visualizeContent.hl2_listWidget.hide()
            self.visualizeContent.hl3_label.hide()
            self.visualizeContent.hl3_listWidget.hide()
            self.visualizeContent.output_listWidget.setGeometry(self.visualizeContent.hl2_listWidget.geometry())
            self.visualizeContent.output_label.setGeometry(self.visualizeContent.hl2_label.geometry())
            self.visualizeWindow.resize(self.visualizeWindow.width() - (self.visualizeContent.hl3_listWidget.width()*2), self.visualizeWindow.height())
    
    def initWindow(self):
        for inputNeuron in values.IL:
            print(inputNeuron.name)
            self.visualizeContent.input_listWidget.insertItem(inputNeuron.id, inputNeuron.name + " --- " + str(inputNeuron.value))
        for hiddenNeuron in values.HL1:
            self.visualizeContent.hl1_listWidget.insertItem(hiddenNeuron.id, hiddenNeuron.name + " --- " + str(hiddenNeuron.value))
        if values.withHL2:
            for hiddenNeuron in values.HL2:
                self.visualizeContent.hl2_listWidget.insertItem(hiddenNeuron.id, hiddenNeuron.name + " --- " + str(hiddenNeuron.value))
            if values.withHL3:
                for hiddenNeuron in values.HL3:
                    self.visualizeContent.hl3_listWidget.insertItem(hiddenNeuron.id, hiddenNeuron.name + " --- " + str(hiddenNeuron.value))
        for outputNeuron in values.OL:
            self.visualizeContent.output_listWidget.insertItem(outputNeuron.id, outputNeuron.name + " --- " + str(outputNeuron.value))
        self.resizeWindow()
        self.visualizeWindow.show()

    def inputLayerChanged(self, neuron):
        self.visualizeContent.input_listWidget.item(neuron.id).setText(neuron.name + " --- " + str(neuron.value))
