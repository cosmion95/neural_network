import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from controller import config_controller, visualize_controller, edit_input_layer_controller
from controller import edit_input_layer_link_controller, edit_hidden_layer_controller, edit_link_controller

#defining all windows
app = QtWidgets.QApplication(sys.argv)

configController = config_controller.ConfigController()
visualizeController = visualize_controller.VisualizeController()
editInputLayerController = edit_input_layer_controller.EditInputLayerController()
editInputLayerLinkController = edit_input_layer_link_controller.EditInputLayerLinkController()
editHiddenLayerController = edit_hidden_layer_controller.EditHiddenLayerController()
editLinkController = edit_link_controller.EditLinkController()

configController.configWindow.show()

#functions
def clickedConfigOK():
    configController.configOK()
    visualizeController.initWindow()

def editInputLayerNeuron():
    editInputLayerController.initWindow(visualizeController.visualizeContent.input_listWidget.currentRow())

def editInputLayerNeuronOK():
    newValue = editInputLayerController.okButtonPressed()
    if newValue[0]:
        visualizeController.windowDataChanged()

def editInputLayerLink():
    fromNeuronID = editInputLayerController.neuron.id
    toNeuronID = editInputLayerController.editInputLayerContent.sinaptics_listWidget.currentRow()
    editInputLayerLinkController.initWindow(fromNeuronID, toNeuronID)

def editInputLayerLinkOK():
    newValue = editInputLayerLinkController.okButtonPressed()
    if newValue[0]:
        editInputLayerController.inputLayerLinkChanged(newValue[1][0], newValue[1][1])
        visualizeController.windowDataChanged()

def editHiddenLayerRecalculate():
    editHiddenLayerController.recalculateButtonPressed()
    visualizeController.windowDataChanged()

def editHiddenLayerLinkFrom():
    fromNeuronID = editHiddenLayerController.editHiddenLayerContent.synaptic_links_from.currentRow()
    toNeuronID = editHiddenLayerController.neuron.id
    editLinkController.initWindowFrom(fromNeuronID, toNeuronID)

def editHiddenLayerLinkTo():
    toNeuronID = editHiddenLayerController.editHiddenLayerContent.synaptic_links_to.currentRow()
    fromNeuronID = editHiddenLayerController.neuron.id
    editLinkController.initWindowTo(fromNeuronID, toNeuronID)

def editLinkOK():
    editLinkController.okButtonPressed()
    editHiddenLayerController.windowDataChanged()

def editHL1Neuron():
    editHiddenLayerController.initWindow(1, visualizeController.visualizeContent.hl1_listWidget.currentRow())
def editHL2Neuron():
    editHiddenLayerController.initWindow(2, visualizeController.visualizeContent.hl2_listWidget.currentRow())
def editHL3Neuron():
    editHiddenLayerController.initWindow(3, visualizeController.visualizeContent.hl3_listWidget.currentRow())
def editOutputNeuron():
    editHiddenLayerController.initWindowOutput(4, visualizeController.visualizeContent.output_listWidget.currentRow())


#linking buttons with functions

#config window
configController.configContent.hl2_cb.stateChanged.connect(configController.checkedHL2)
configController.configContent.hl3_cb.stateChanged.connect(configController.checkedHL3)
configController.configContent.ok_button.clicked.connect(clickedConfigOK)

#visualize window
visualizeController.visualizeContent.input_listWidget.itemDoubleClicked.connect(editInputLayerNeuron)
visualizeController.visualizeContent.hl1_listWidget.itemDoubleClicked.connect(editHL1Neuron)
visualizeController.visualizeContent.hl2_listWidget.itemDoubleClicked.connect(editHL2Neuron)
visualizeController.visualizeContent.hl3_listWidget.itemDoubleClicked.connect(editHL3Neuron)
visualizeController.visualizeContent.output_listWidget.itemDoubleClicked.connect(editOutputNeuron)

#edit input layer window
editInputLayerController.editInputLayerContent.okButton.clicked.connect(editInputLayerNeuronOK)
editInputLayerController.editInputLayerContent.sinaptics_listWidget.itemDoubleClicked.connect(editInputLayerLink)

#edit input layer link window
editInputLayerLinkController.editInputLayerLinkContent.ok_button.clicked.connect(editInputLayerLinkOK)

#edit hidden layer window
editHiddenLayerController.editHiddenLayerContent.recalculate_button.clicked.connect(editHiddenLayerRecalculate)
editHiddenLayerController.editHiddenLayerContent.ok_button.clicked.connect(editHiddenLayerController.okButtonPressed)
editHiddenLayerController.editHiddenLayerContent.synaptic_links_from.itemDoubleClicked.connect(editHiddenLayerLinkFrom)
editHiddenLayerController.editHiddenLayerContent.synaptic_links_to.itemDoubleClicked.connect(editHiddenLayerLinkTo)

#edit link
editLinkController.EditLinkContent.ok_button.clicked.connect(editLinkOK)

sys.exit(app.exec_())


