# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/training.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_trainingWindow(object):
    def setupUi(self, trainingWindow):
        trainingWindow.setObjectName("trainingWindow")
        trainingWindow.resize(1176, 1240)
        self.centralwidget = QtWidgets.QWidget(trainingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 50, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 1141, 451))
        self.tableWidget.setRowCount(765)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setObjectName("tableWidget")
        self.normalizedTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.normalizedTableWidget.setGeometry(QtCore.QRect(20, 660, 1141, 471))
        self.normalizedTableWidget.setRowCount(765)
        self.normalizedTableWidget.setColumnCount(16)
        self.normalizedTableWidget.setObjectName("normalizedTableWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 560, 291, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 201, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 640, 121, 16))
        self.label_3.setObjectName("label_3")
        trainingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(trainingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 21))
        self.menubar.setObjectName("menubar")
        trainingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(trainingWindow)
        self.statusbar.setObjectName("statusbar")
        trainingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(trainingWindow)
        QtCore.QMetaObject.connectSlotsByName(trainingWindow)

    def retranslateUi(self, trainingWindow):
        _translate = QtCore.QCoreApplication.translate
        trainingWindow.setWindowTitle(_translate("trainingWindow", "Training window"))
        self.pushButton.setText(_translate("trainingWindow", "Load data"))
        self.label.setText(_translate("trainingWindow", "Data not loaded."))
        self.pushButton_2.setText(_translate("trainingWindow", "Normalize"))
        self.label_2.setText(_translate("trainingWindow", "Initial data"))
        self.label_3.setText(_translate("trainingWindow", "Normalized data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trainingWindow = QtWidgets.QMainWindow()
    ui = Ui_trainingWindow()
    ui.setupUi(trainingWindow)
    trainingWindow.show()
    sys.exit(app.exec_())
