# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Python/Python Bootcamp/QT/BMI_Rechner/ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 496)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.height = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.height.setMinimum(0.01)
        self.height.setMaximum(2.5)
        self.height.setSingleStep(0.01)
        self.height.setObjectName("height")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.height)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.weigth = QtWidgets.QSpinBox(self.centralWidget)
        self.weigth.setObjectName("weigth")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.weigth)
        self.calculate = QtWidgets.QPushButton(self.centralWidget)
        self.calculate.setObjectName("calculate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.calculate)
        self.result = QtWidgets.QLabel(self.centralWidget)
        self.result.setObjectName("result")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.result)
        self.result_label = QtWidgets.QLabel(self.centralWidget)
        self.result_label.setEnabled(True)
        self.result_label.setObjectName("result_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.result_label)
        self.gridLayout_2.addLayout(self.formLayout, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 371, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "K&ouml;rpergr&ouml;&szlig;e in m:"))
        self.label_2.setText(_translate("MainWindow", "Gewicht in kg:"))
        self.calculate.setText(_translate("MainWindow", "BMI Berechnen!"))
        self.result.setText(_translate("MainWindow", "20"))
        self.result_label.setText(_translate("MainWindow", "Dein BMI ist:"))

