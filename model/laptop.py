class Laptop:
    def __init__(self, maxHorizontalResolution, memoryTechnology, installedMemory, processorSpeed, processor,
                 manufacturer, infrared, bluetooth, dockingStation, portReplicator, fingerprint, subwoofer,
                 externalBattery, operatingSystem, warrantyDays, price):
        self.maxHorizontalResolution = maxHorizontalResolution
        self.memoryTechnology = memoryTechnology
        self.installedMemory = installedMemory
        self.processorSpeed = processorSpeed
        self.processor = processor
        self.manufacturer = manufacturer
        self.infrared = infrared
        self.bluetooth = bluetooth
        self.dockingStation = dockingStation
        self.portReplicator = portReplicator
        self.fingerprint = fingerprint
        self.subwoofer = subwoofer
        self.externalBattery = externalBattery
        self.operatingSystem = operatingSystem
        self.warrantyDays = warrantyDays
        self.price = price

    def printLaptop(self):
        print(self)
        print(" Max horizontal resolution: " + str(self.maxHorizontalResolution))
        print(" Memory technology: " + str(self.memoryTechnology))
        print(" Installed memory: " + str(self.installedMemory))
        print(" Processor speed: " + str(self.processorSpeed))
        print(" Processor: " + str(self.processor))
        print(" Manufacturer: " + str(self.manufacturer))
        print(" Infrared: " + str(self.infrared))
        print(" Bluetooth: " + str(self.bluetooth))
        print(" Docking station: " + str(self.dockingStation))
        print(" Port replicator: " + str(self.portReplicator))
        print(" Fingerprint: " + str(self.fingerprint))
        print(" Subwoofer: " + str(self.subwoofer))
        print(" External battery: " + str(self.externalBattery))
        print(" Operating system: " + str(self.operatingSystem))
        print(" Warranty days: " + str(self.warrantyDays))
        print(" Price: " + str(self.price))
