# Install: PySide2 (free Licence), qtpy

# GUI-Generator: pyqt5 (GPL Licence), pyqt5-tools
#                Found in: c:\program files\python37\lib\site-packages\pyqt5_tools\designer.exe
#                Save ui file
#                Convert ui file with build.py
#                Change import PyQt5 to import PySide2 in converted file 


import sys
import csv
from PySide2 import QtWidgets, QtGui

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Studierendenverwaltung")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.readCsvFile("./Python/Python Bootcamp/QT/CSV_Import/students.csv")
        self.ui.newEntryButton.clicked.connect(self.onNewEntry)
        self.ui.saveButton.clicked.connect(self.onSave)
        self.ui.actionSave.triggered.connect(self.onSave)

    def onSave(self):
        with open('./Python/Python Bootcamp/QT/CSV_Import/students.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=",", quotechar='"')

            rows = self.ui.studentsTable.rowCount()
            for i in range(0, rows):
                rowContent = [
                    self.ui.studentsTable.item(i, 0).text(),
                    self.ui.studentsTable.item(i, 1).text(),
                    self.ui.studentsTable.item(i, 2).text()
                ]
                writer.writerow(rowContent)

    def onNewEntry(self):
        row = self.ui.studentsTable.rowCount()
        self.ui.studentsTable.insertRow(row)

        self.ui.studentsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(""))
        self.ui.studentsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(""))
        self.ui.studentsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(""))

        cell = self.ui.studentsTable.item(row, 0)
        self.ui.studentsTable.editItem(cell)

    def readCsvFile(self, filename):
        self.ui.studentsTable.setRowCount(0)
        with open(filename, "r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for line in reader:
                row = self.ui.studentsTable.rowCount()
                self.ui.studentsTable.insertRow(row)

                self.ui.studentsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(line[0]))
                self.ui.studentsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(line[1]))
                self.ui.studentsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(line[2]))



window = MainWindow()

window.show()

sys.exit(app.exec_())
