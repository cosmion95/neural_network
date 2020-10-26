import sys
import xlrd
from PyQt5 import QtCore, QtGui, QtWidgets
from controller import training_controller
from model import laptop

# defining all windows
app = QtWidgets.QApplication(sys.argv)

trainingController = training_controller.TrainingController()
trainingController.trainingWindow.show()

xl_workbook = xlrd.open_workbook("dataset.xlsx")

xl_sheet = xl_workbook.sheet_by_index(0)

# calculate mins and maxes
minMaxList = []
laptops = []
normalizedLaptops = []


def normalizeResult(x, min, max):
    return (x - min) / (max - min)


def loadData():
    num_cols = xl_sheet.ncols
    for col_idx in range(0, num_cols):
        currentMin = xl_sheet.cell(1, col_idx).value
        currentMax = xl_sheet.cell(1, col_idx).value
        for row_idx in range(1, xl_sheet.nrows):
            if xl_sheet.cell(row_idx, col_idx).value < currentMin:
                currentMin = xl_sheet.cell(row_idx, col_idx).value
            if xl_sheet.cell(row_idx, col_idx).value > currentMax:
                currentMax = xl_sheet.cell(row_idx, col_idx).value
        minMaxList.append((currentMin, currentMax))

    for row_idx in range(1, xl_sheet.nrows):
        lp = laptop.Laptop(float(xl_sheet.cell(row_idx, 0).value), float(xl_sheet.cell(row_idx, 1).value),
                           float(xl_sheet.cell(row_idx, 2).value), float(xl_sheet.cell(row_idx, 3).value),
                           float(xl_sheet.cell(row_idx, 4).value), float(xl_sheet.cell(row_idx, 5).value),
                           float(xl_sheet.cell(row_idx, 6).value), float(xl_sheet.cell(row_idx, 7).value),
                           float(xl_sheet.cell(row_idx, 8).value), float(xl_sheet.cell(row_idx, 9).value),
                           float(xl_sheet.cell(row_idx, 10).value), float(xl_sheet.cell(row_idx, 11).value),
                           float(xl_sheet.cell(row_idx, 12).value), float(xl_sheet.cell(row_idx, 13).value),
                           float(xl_sheet.cell(row_idx, 14).value), float(xl_sheet.cell(row_idx, 15).value))
        laptops.append(lp)
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(
            str(lp.maxHorizontalResolution)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(
            str(lp.memoryTechnology)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(
            str(lp.installedMemory)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 3,
                                                                     QtWidgets.QTableWidgetItem(str(lp.processorSpeed)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 4,
                                                                     QtWidgets.QTableWidgetItem(str(lp.processor)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 5,
                                                                     QtWidgets.QTableWidgetItem(str(lp.manufacturer)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 6,
                                                                     QtWidgets.QTableWidgetItem(str(lp.infrared)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 7,
                                                                     QtWidgets.QTableWidgetItem(str(lp.bluetooth)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 8,
                                                                     QtWidgets.QTableWidgetItem(str(lp.dockingStation)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 9,
                                                                     QtWidgets.QTableWidgetItem(str(lp.portReplicator)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 10,
                                                                     QtWidgets.QTableWidgetItem(str(lp.fingerprint)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 11,
                                                                     QtWidgets.QTableWidgetItem(str(lp.subwoofer)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 12, QtWidgets.QTableWidgetItem(
            str(lp.externalBattery)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 13, QtWidgets.QTableWidgetItem(
            str(lp.operatingSystem)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 14,
                                                                     QtWidgets.QTableWidgetItem(str(lp.warrantyDays)))
        trainingController.trainingWindowContent.tableWidget.setItem(row_idx, 15,
                                                                     QtWidgets.QTableWidgetItem(str(lp.price)))


def normalize():
    counter = 1
    for lp in laptops:
        NmaxHorizontalResolution = normalizeResult(lp.maxHorizontalResolution, minMaxList[0][0], minMaxList[0][1])
        NmemoryTechnology = normalizeResult(lp.memoryTechnology, minMaxList[1][0], minMaxList[1][1])
        NinstalledMemory = normalizeResult(lp.installedMemory, minMaxList[2][0], minMaxList[2][1])
        NprocessorSpeed = normalizeResult(lp.processorSpeed, minMaxList[3][0], minMaxList[3][1])
        Nprocessor = normalizeResult(lp.processor, minMaxList[4][0], minMaxList[4][1])
        Nmanufacturer = normalizeResult(lp.manufacturer, minMaxList[5][0], minMaxList[5][1])
        Ninfrared = normalizeResult(lp.infrared, minMaxList[6][0], minMaxList[6][1])
        Nbluetooth = normalizeResult(lp.bluetooth, minMaxList[7][0], minMaxList[7][1])
        NdockingStation = normalizeResult(lp.dockingStation, minMaxList[8][0], minMaxList[8][1])
        NportReplicator = normalizeResult(lp.portReplicator, minMaxList[9][0], minMaxList[9][1])
        Nfingerprint = normalizeResult(lp.fingerprint, minMaxList[10][0], minMaxList[10][1])
        Nsubwoofer = normalizeResult(lp.subwoofer, minMaxList[11][0], minMaxList[11][1])
        NexternalBattery = normalizeResult(lp.externalBattery, minMaxList[12][0], minMaxList[12][1])
        NoperatingSystem = normalizeResult(lp.operatingSystem, minMaxList[13][0], minMaxList[13][1])
        NwarrantyDays = normalizeResult(lp.warrantyDays, minMaxList[14][0], minMaxList[14][1])
        Nprice = normalizeResult(lp.warrantyDays, minMaxList[14][0], minMaxList[14][1])
        nLp = laptop.Laptop(NmaxHorizontalResolution, NmemoryTechnology, NinstalledMemory, NprocessorSpeed, Nprocessor,
                            Nmanufacturer, Ninfrared, Nbluetooth, NdockingStation, NportReplicator, Nfingerprint,
                            Nsubwoofer, NexternalBattery, NoperatingSystem, NwarrantyDays, Nprice)
        normalizedLaptops.append(nLp)
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 0, QtWidgets.QTableWidgetItem(
            str(nLp.maxHorizontalResolution)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 1, QtWidgets.QTableWidgetItem(
            str(nLp.memoryTechnology)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 2, QtWidgets.QTableWidgetItem(
            str(nLp.installedMemory)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 3, QtWidgets.QTableWidgetItem(
            str(nLp.processorSpeed)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 4, QtWidgets.QTableWidgetItem(
            str(nLp.processor)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 5, QtWidgets.QTableWidgetItem(
            str(nLp.manufacturer)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 6, QtWidgets.QTableWidgetItem(
            str(nLp.infrared)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 7, QtWidgets.QTableWidgetItem(
            str(nLp.bluetooth)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 8, QtWidgets.QTableWidgetItem(
            str(nLp.dockingStation)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 9, QtWidgets.QTableWidgetItem(
            str(nLp.portReplicator)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 10, QtWidgets.QTableWidgetItem(
            str(nLp.fingerprint)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 11, QtWidgets.QTableWidgetItem(
            str(nLp.subwoofer)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 12, QtWidgets.QTableWidgetItem(
            str(nLp.externalBattery)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 13, QtWidgets.QTableWidgetItem(
            str(nLp.operatingSystem)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 14, QtWidgets.QTableWidgetItem(
            str(nLp.warrantyDays)))
        trainingController.trainingWindowContent.normalizedTableWidget.setItem(counter, 15, QtWidgets.QTableWidgetItem(
            str(nLp.price)))
        counter += 1


trainingController.trainingWindowContent.pushButton.clicked.connect(loadData)
trainingController.trainingWindowContent.pushButton_2.clicked.connect(normalize)

sys.exit(app.exec_())
