from functions import entry, activation

#defining the lists of values
IL = []
HL1 = []
HL2 = []
HL3 = []
OL = []

withHL2 = False
withHL3 = False

entry_functions = [
    (0, "Suma", entry.suma),
    (1, "Produs", entry.produs),
    (3, "Maxim", entry.maxim),
    (4, "Minim", entry.minim),
]

activation_functions = [
    (0, "Treapta", activation.treapta, None),
    (1, "Sigmoidala", activation.sigmoidala, activation.binarSigmoidala),
    (2, "Signum", activation.signum, None),
    (3, "Tangenta hiperbolica", activation.tangenta_hiperbolica, activation.binarTangentaHiperbolica),
    (4, "Rampa", activation.rampa, activation.binarRampa)
]

neuron_types = [
    (0, "IL", IL),
    (1, "HL1", HL1),
    (2, "HL2", HL2),
    (3, "HL3", HL3),
    (4, "OL", OL),
]

def setWithHL2():
    global withHL2
    withHL2 = True

def setWithHL3():
    global withHL2, withHL3
    withHL2 = True
    withHL3 = True

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
    if hiddenLayerNr == 1:
        return findHL1NeuronByID(neuronID)
    elif hiddenLayerNr == 2:
        return findHL2NeuronByID(neuronID)
    elif hiddenLayerNr == 3:
        return findHL3NeuronByID(neuronID)
    else:
        return None

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


#--------------------------find neuron type -------------------------
def findNeuronType(name):
    neuronTypeName = name.split("-")[0]
    for neuronType in neuron_types:
        if neuronType[1] == neuronTypeName:
            return neuronType[0]

#-----------------------find neuron layer by type ------------------
def findNeuronLayer(neuronType):
    for layer in neuron_types:
        if layer[0] == neuronType:
            return layer[2]


#------------------retrieve links from previous layer------------
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
            if link[0].id == neuron.id:
                neuronLinks.append((n.value, link[1]))
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
            return f[3](neuron.binar, neuron.activation_function_value)
   