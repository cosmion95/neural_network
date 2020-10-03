from view import config_window
from PyQt5 import QtWidgets
from model import neuron
import values

class ConfigController():
    def __init__(self):
        self.configWindow = QtWidgets.QMainWindow()
        self.configContent = config_window.Ui_ConfigWindow()
        self.configContent.setupUi(self.configWindow)

    def checkedHL2(self):
        if self.configContent.hl2_cb.checkState():
            self.configContent.hl2_neurons_sb.setEnabled(True)
            self.configContent.hl3_cb.setEnabled(True)
        else:
            self.configContent.hl2_neurons_sb.setEnabled(False)
            self.configContent.hl3_cb.setChecked(False)
            self.configContent.hl3_cb.setEnabled(False)

    def checkedHL3(self):
        if self.configContent.hl3_cb.checkState():
            self.configContent.hl3_neurons_sb.setEnabled(True)
        else:
            self.configContent.hl3_neurons_sb.setEnabled(False)

    def configOK(self):
        for i in range(self.configContent.il_neurons_sb.value()):
            inputNeuron = neuron.Neuron(i, "IL-" + str(i + 1), 0.0)
            values.IL.append(inputNeuron)
        for i in range(self.configContent.hl1_neurons_sb.value()):
            hiddenNeuron = neuron.Neuron(i, "HL1-" + str(i + 1), 0.0)
            values.HL1.append(hiddenNeuron)
            for n in values.IL:
                n.add_link(hiddenNeuron, 0.0)
        if self.configContent.hl2_cb.checkState():
            for i in range(self.configContent.hl2_neurons_sb.value()):
                hiddenNeuron = neuron.Neuron(i, "HL2-" + str(i + 1), 0.0)
                values.HL2.append(hiddenNeuron)
                for n in values.HL1:
                    n.add_link(hiddenNeuron, 0.0)
        if self.configContent.hl3_cb.checkState():
            for i in range(self.configContent.hl3_neurons_sb.value()):
                hiddenNeuron = neuron.Neuron(i, "HL3-" + str(i + 1), 0.0)
                values.HL3.append(hiddenNeuron)
                for n in values.HL2:
                    n.add_link(hiddenNeuron, 0.0)
        for i in range(self.configContent.ol_neurons_sb.value()):
            outputNeuron = neuron.Neuron(i, "OL-" + str(i + 1), 0.0)
            values.OL.append(outputNeuron)
            if self.configContent.hl2_cb.checkState():
                if self.configContent.hl3_cb.checkState():
                    values.setWithHL3()
                    for n in values.HL3:
                        n.add_link(outputNeuron, 0.0)
                else:
                    values.setWithHL2()
                    for n in values.HL2:
                        n.add_link(outputNeuron, 0.0)
            else:
                for n in values.HL1:
                    n.add_link(outputNeuron, 0.0)
        values.calculateNeuralNetworkValues()
        self.configWindow.hide()
