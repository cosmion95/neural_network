from functions import entry, activation

#defining the lists of values
IL = []
HL1 = []
HL2 = []
HL3 = []
OL = []

withHL2 = False
withHL3 = False

currentHiddenLayer = 1

entry_functions = [
    (0, "Suma", entry.suma),
    (1, "Produs", entry.produs),
    (2, "Maxim", entry.maxim),
    (3, "Minim", entry.minim),
]

activation_functions = [
    (0, "Treapta", activation.treapta, None),
    (1, "Sigmoidala", activation.sigmoidala, activation.binarSigmoidala),
    (2, "Signum", activation.signum, None),
    (3, "Tangenta hiperbolica", activation.tangenta_hiperbolica, activation.binarTangentaHiperbolica),
    (4, "Rampa", activation.rampa, activation.binarRampa)
]

layer_types = [
    (0, "IL", IL),
    (1, "HL1", HL1),
    (2, "HL2", HL2),
    (3, "HL3", HL3),
    (4, "OL", OL),
]

def setWithHL2(value = True):
    global withHL2
    withHL2 = value

def setWithHL3(value = True):
    global withHL2, withHL3
    withHL2 = value
    withHL3 = value

def setCurrentHiddenLayer(nr):
    global currentHiddenLayer
    currentHiddenLayer = nr

#find neurons by ID
def findInputLayerNeuronByID(neuronID):
    for neuron in IL:
        if neuron.id == neuronID:
            return neuron

def findHL1NeuronByID(neuronID):
    for neuron in HL1:
        if neuron.id == neuronID:
            return neuron

def findHL2NeuronByID(neuronID):
    for neuron in HL2:
        if neuron.id == neuronID:
            return neuron

def findHL3NeuronByID(neuronID):
    for neuron in HL3:
        if neuron.id == neuronID:
            return neuron

def findHiddenLayerNeuronByID(hiddenLayerNr, neuronID):
    for layer in layer_types:
        if layer[0] == hiddenLayerNr:
            for neuron in layer[2]:
                if neuron.id == neuronID:
                    return neuron

def findOutputLayerNeuronByID(neuronID):
    for neuron in OL:
        if neuron.id == neuronID:
            return neuron

#-----------------------retrieve link values------------------------------------
def getInputLayerLinkValue(fromNeuronID, toNeuronID):
    for neuron in IL:
        if neuron.id == fromNeuronID:
            for link in neuron.links:
                if link.neuron.id == toNeuronID:
                    return link.value


#---------------------- modify values ----------------------------------
#input neuron value
def modifyInputLayerNeuronValue(neuronID, value):
    for neuron in IL:
        if neuron.id == neuronID:
            neuron.value = value

#input neuron link value to another neuron
def modifyInputLayerLinkValue(fromNeuronID, toNeuronID, value):
    for neuron in IL:
        if neuron.id == fromNeuronID:
            for link in neuron.links:
                if link.neuron.id == toNeuronID:
                    link.value = value

def modifyLayerLinkValue(layerNumber, fromNeuronID, toNeuronID, newValue):
    for layer in layer_types:
        if layer[0] == layerNumber:
            for neuron in layer[2]:
                if neuron.id == fromNeuronID:
                    for link in neuron.links:
                        if link.neuron.id == toNeuronID:
                            link.value = newValue


#--------------------------find neuron type -------------------------
def findNeuronType(name):
    neuronTypeName = name.split("-")[0]
    for neuronType in layer_types:
        if neuronType[1] == neuronTypeName:
            return neuronType[0]

#-----------------------find neuron layer by type ------------------
def findNeuronLayer(neuronType):
    for layer in layer_types:
        if layer[0] == neuronType:
            return layer[2]

#------------------retrieve links from previous layer------------
def getLinksTupleFromPreviousLayer(neuron):
    neuronType = findNeuronType(neuron.name)
    neuronLinksInType = neuronType-1
    if neuronType == 4:
        if not withHL3:
            if not withHL2:
                neuronLinksInType = neuronType - 3
            else:
                neuronLinksInType = neuronType - 2
    neuronLayer = findNeuronLayer(neuronLinksInType)
    neuronLinks = []
    for n in neuronLayer:
        for link in n.links:
            if link.neuron.id == neuron.id:
                neuronLinks.append((n.value, link.value))
                break
    return neuronLinks

def getLinksFromPreviousLayer(neuron):
    neuronType = findNeuronType(neuron.name)
    neuronLinksInType = neuronType-1
    if neuronType == 4:
        if not withHL3:
            if not withHL2:
                neuronLinksInType = neuronType - 3
            else:
                neuronLinksInType = neuronType - 2
    neuronLayer = findNeuronLayer(neuronLinksInType)
    neuronLinks = []
    for n in neuronLayer:
        for link in n.links:
            if link.neuron.id == neuron.id:
                neuronLinks.append((n, link.value))
                break
    return neuronLinks
    

#----------------calculate entry function ----------------
def calculateEntryFunction(functionID, inputs):
    for f in entry_functions:
        if f[0] == functionID:
            return f[2](inputs)

def calculateActivationFunction(neuron):
    for f in activation_functions:
        if f[0] == neuron.activation_function_id:
            return f[2](neuron.entry_function_value, neuron.teta, neuron.g, neuron.a)

def calculateOutputValue(neuron):
    for f in activation_functions:
        if f[0] == neuron.activation_function_id:
            if f[3] is not None:
                return f[3](neuron.binar, neuron.activation_function_value)
            else:
                return neuron.activation_function_value
   

#--------------CALCULATE NEURAL NETWORK VALUES------------------
def calculateNeuralNetworkValues():
    for layer in layer_types:
        for neuron in layer[2]:
            neuron.calculateFunctions()
            neuron.calculateOutputValue()


def recalculateNeuralNetworkFromLayer(neuron):
    layerType = findNeuronType(neuron.name)
    for layer in layer_types:
        if layer[0] > layerType:
            for n in layer[2]:
                neuron.calculateFunctions()
                neuron.calculateOutputValue()

def resetValues():
    for layer in layer_types:
        for neuron in layer[2]:
            neuron.entry_function_id = 0
            neuron.activation_function_id = 0
            neuron.teta = 0.0
            neuron.a = 1.0
            neuron.g = 1.0
            neuron.binar = False
            neuron.entry_function_value = 0.0
            neuron.activation_function_value = 0.0
            neuron.value = 0.0
            for link in neuron.links:
                link.value = 0.0

def reconfigureNetwork():
    for layer in layer_types:
        layer[2].clear()
    setWithHL3(False)