from UserInterface.Windows.MainWindow import MainWindow
from UserInterface.Dialogs.AddEmployeeDialog import AddEmployeeDialog
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication
from PyQt5 import QtCore
from DataAccessLayer.Datebase import Datebase
from DataAccessLayer.FileOperation import FileOperation
from BusinessAccessLayer.CSP import CSP
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QTransform

from PyQt5.QtWidgets import *

class UserInterfaceController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # -------------------------------
        self.startStep = 0
        self.allSteps  = 0
        self.monday3rdShiftForSteps = []
        self.monday1stShiftForSteps = []
        self.monday2ndShiftForSteps = []
        self.tuesday3rdShiftForSteps = []
        self.tuesday2ndShiftForSteps = []
        self.tuesday1stShiftForSteps = []
        self.wednesday3rdShiftForSteps = []
        self.wednesday2ndShiftForSteps = []
        self.wednesday1stShiftForSteps = []
        self.thursday3rdShiftForSteps = []
        self.thursday2ndShiftForSteps = []
        self.thursday1stShiftForSteps = []
        self.friday3rdShiftForSteps = []
        self.friday2ndShiftForSteps = []
        self.friday1stShiftForSteps = []
        self.funFindSolutionUsed = False
        self.funFindSteps = False

        # -------------------------------
        self.dateBase = Datebase()
        self.file = FileOperation()
        self.employees = []
        self.csp = CSP(self.employees)

        # -------------------------------
        self.mainWindow = MainWindow()
        self.mainWindow.setupUI(self)

        self.addEmployeeDialog = AddEmployeeDialog()
        self.dialogAE = QDialog(self)
        self.addEmployeeDialog.setupUI(self.dialogAE)

        # reakcja przycisków
        self.mainWindow.pushButton.clicked.connect(self.AddEmployee)
        self.mainWindow.pushButton_8.clicked.connect(self.FindASolution)
        self.mainWindow.pushButton_7.clicked.connect(self.Steps)

        # action
        self.mainWindow.actionLoad_from_a_file.triggered.connect(self.LoadDatabaseFromFile)
        self.mainWindow.actionSave_a_file.triggered.connect(self.SaveDatabaseToFile)
        self.mainWindow.actionLoad_example_datebase.triggered.connect(self.LoadExampleDateBase)

    # ----------------------------------------------------------------------------
    def AddEmployee(self):
        self.addEmployeeDialog.buttonBox.accepted.connect(self.SaveDataToDateBaseFromDialog)
        self.dialogAE.exec_()

    def LoadDatabaseFromFile(self):
        fileDialog = QFileDialog(self)
        fileDialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        fileDialog.setWindowTitle('Load database from a file')
        fileDialog.setNameFilter("Weka (*.arff)")
        if fileDialog.exec_():
            filenames = fileDialog.selectedFiles()
            if len(filenames) != 1:
                QMessageBox.critical(fileDialog, "Error", "Too many files selected", QMessageBox.Close)
            else:
                try:
                    if len(self.csp.employees) > 0:
                        label1.deleteLater()
                        label2.deleteLater()
                        label3.deleteLater()
                        label4.deleteLater()
                        label5.deleteLater()
                        label6.deleteLater()
                        label7.deleteLater()
                        label8.deleteLater()
                        label9.deleteLater()
                        label10.deleteLater()
                        label11.deleteLater()
                        label12.deleteLater()
                        label13.deleteLater()
                        label14.deleteLater()
                        label15.deleteLater()
                        self.mainWindow.textBrowser.clear()
                        self.startStep = 0
                        self.allSteps  = 0
                        self.monday3rdShiftForSteps = []
                        self.monday1stShiftForSteps = []
                        self.monday2ndShiftForSteps = []
                        self.tuesday3rdShiftForSteps = []
                        self.tuesday2ndShiftForSteps = []
                        self.tuesday1stShiftForSteps = []
                        self.wednesday3rdShiftForSteps = []
                        self.wednesday2ndShiftForSteps = []
                        self.wednesday1stShiftForSteps = []
                        self.thursday3rdShiftForSteps = []
                        self.thursday2ndShiftForSteps = []
                        self.thursday1stShiftForSteps = []
                        self.friday3rdShiftForSteps = []
                        self.friday2ndShiftForSteps = []
                        self.friday1stShiftForSteps = []
                        self.funFindSolutionUsed = False
                    self.file.ReadFrom(filenames[0], self.csp.employees)
                    QMessageBox.information(fileDialog, "Load datbase from a file", "Data has been loaded", QMessageBox.Ok)
                    self.LoadGraph()
                except Exception as error:
                    QMessageBox.critical(fileDialog, "Error", "Error reading from file: " + str(error), QMessageBox.Close)

    def SaveDatabaseToFile(self):
        fileDialog = QFileDialog(self)
        fileDialog.setFileMode(QFileDialog.FileMode.AnyFile)
        filename, extension = fileDialog.getSaveFileName(self, "Save database", '', "Weka (*.arff)")
        if filename:
            try:
                self.file.SaveTo(str(filename), self.csp.employees)
                QMessageBox.information(fileDialog, "Save database", "Database has been saved", QMessageBox.Ok)
            except Exception as error:
                 QMessageBox.critical(fileDialog, "Error", "Error writing to file: " + str(error), QMessageBox.Close)

    # ----------------------------------------------------------------------------
    def SaveDataToDateBaseFromDialog(self):
        length = len(self.addEmployeeDialog.lineEdit.text().split(";"))
        name = self.addEmployeeDialog.lineEdit.text().split(";")
        preferredWorkingDays = self.addEmployeeDialog.lineEdit_2.text().split(";")
        jobPosition = self.addEmployeeDialog.lineEdit_3.text().split(";")
        workshift = self.addEmployeeDialog.lineEdit_4.text()

        if ("1" in workshift or "2" in workshift or "3" in workshift) and  ("1" in preferredWorkingDays or "2" in preferredWorkingDays or "3" in preferredWorkingDays or "4" in preferredWorkingDays or "5" in preferredWorkingDays):
            QMessageBox.critical(None, "Error", "Bad value: Database has not been saved", QMessageBox.Ok)
        else:
            try:
                self.dateBase.SaveDataToDataBase(length, name, jobPosition, preferredWorkingDays, workshift, self.csp.employees)
                QMessageBox.information(None, "Save database", "Database has been saved", QMessageBox.Ok)
                if self.funFindSolutionUsed == True or self.funFindSteps == True:
                    label1.setText("Monday - 3rd shift")
                    label2.setText("Monday - 2nd shift")
                    label3.setText("Monday - 1st shift")
                    label4.setText("Tuesday - 1st shift")
                    label5.setText("Tuesday - 2nd shift")
                    label6.setText("Tuesday - 3rd shift")
                    label7.setText("Wednesday - 1st shift")
                    label8.setText("Wednesday - 2nd shift")
                    label9.setText("Wednesday - 3rd shift")
                    self.startStep = 0
                    self.allSteps  = 0
                    self.monday3rdShiftForSteps.clear()
                    self.mainWindow.textBrowser.clear()
                    self.funFindSteps = False
                    self.funFindSolutionUsed = False
                else:
                    self.LoadGraph()
            except Exception as error:
                    QMessageBox.critical(None, "Error", "Data writing error: " + str(error), QMessageBox.Close)
            
    def LoadExampleDateBase(self):
        try:
            if len(self.csp.employees) > 0:
                label1.deleteLater()
                label2.deleteLater()
                label3.deleteLater()
                label4.deleteLater()
                label5.deleteLater()
                label6.deleteLater()
                label7.deleteLater()
                label8.deleteLater()
                label9.deleteLater()
                label10.deleteLater()
                label11.deleteLater()
                label12.deleteLater()
                label13.deleteLater()
                label14.deleteLater()
                label15.deleteLater()
                self.mainWindow.textBrowser.clear()
                self.startStep = 0
                self.allSteps  = 0
                self.monday3rdShiftForSteps = []
                self.monday1stShiftForSteps = []
                self.monday2ndShiftForSteps = []
                self.tuesday3rdShiftForSteps = []
                self.tuesday2ndShiftForSteps = []
                self.tuesday1stShiftForSteps = []
                self.wednesday3rdShiftForSteps = []
                self.wednesday2ndShiftForSteps = []
                self.wednesday1stShiftForSteps = []
                self.thursday3rdShiftForSteps = []
                self.thursday2ndShiftForSteps = []
                self.thursday1stShiftForSteps = []
                self.friday3rdShiftForSteps = []
                self.friday2ndShiftForSteps = []
                self.friday1stShiftForSteps = []
                self.funFindSolutionUsed = False
                self.funFindSteps = False
            self.dateBase.LoadExampleDataBase(self.csp.employees)
            QMessageBox.information(None, "Load example datbase", "Example database has been loaded", QMessageBox.Ok)
            self.LoadGraph()
        except Exception as error:
                 QMessageBox.critical(None, "Error", "Data loading error: " + str(error), QMessageBox.Close)
        

    # --------------------------------------------------------------------------------

    def LoadGraph(self):
        if len(self.csp.employees) > 0:
            global label1
            global label2
            global label3
            global label4
            global label5
            global label6
            global label7
            global label8
            global label9
            global label10
            global label11
            global label12
            global label13
            global label14
            global label15
            label1 = QLabel("Monday - 3rd shift", self)
            label2 = QLabel("Monday - 2nd shift", self)
            label3 = QLabel("Monday - 1st shift", self)
            label4 = QLabel("Tuesday - 1st shift", self)
            label5 = QLabel("Tuesday - 2nd shift", self)
            label6 = QLabel("Tuesday - 3rd shift", self)
            label7 = QLabel("Wednesday - 1st shift", self)
            label8 = QLabel("Wednesday - 2nd shift", self)
            label9 = QLabel("Wednesday - 3rd shift", self)
            label10 = QLabel("Thursday - 1st shift", self)
            label11 = QLabel("Thursday - 2nd shift", self)
            label12 = QLabel("Thursday - 3rd shift", self)
            label13 = QLabel("Friday - 1st shift", self)
            label14 = QLabel("Friday - 2nd shift", self)
            label15 = QLabel("Friday - 3rd shift", self)
            label1.setFixedSize(200, 200)
            label2.setFixedSize(200, 200)
            label3.setFixedSize(200, 200)
            label4.setFixedSize(200, 200)
            label5.setFixedSize(200, 200)
            label6.setFixedSize(200, 200)
            label7.setFixedSize(200, 200)
            label8.setFixedSize(200, 200) 
            label9.setFixedSize(200, 200)
            label10.setFixedSize(200, 200)
            label11.setFixedSize(200, 200)
            label12.setFixedSize(200, 200)
            label13.setFixedSize(200, 200)
            label14.setFixedSize(200, 200)
            label15.setFixedSize(200, 200)
            label1.setAlignment(QtCore.Qt.AlignCenter)
            label2.setAlignment(QtCore.Qt.AlignCenter)
            label3.setAlignment(QtCore.Qt.AlignCenter)
            label4.setAlignment(QtCore.Qt.AlignCenter)
            label5.setAlignment(QtCore.Qt.AlignCenter)
            label6.setAlignment(QtCore.Qt.AlignCenter)
            label7.setAlignment(QtCore.Qt.AlignCenter)
            label8.setAlignment(QtCore.Qt.AlignCenter)
            label9.setAlignment(QtCore.Qt.AlignCenter)
            label10.setAlignment(QtCore.Qt.AlignCenter)
            label11.setAlignment(QtCore.Qt.AlignCenter)
            label12.setAlignment(QtCore.Qt.AlignCenter)
            label13.setAlignment(QtCore.Qt.AlignCenter)
            label14.setAlignment(QtCore.Qt.AlignCenter)
            label15.setAlignment(QtCore.Qt.AlignCenter)
            label1.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label2.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label3.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label4.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label5.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label6.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label7.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label8.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label9.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label10.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label11.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label12.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label13.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label14.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            label15.setStyleSheet("border: 1.5px solid black; border-radius: 100px;")
            areaScroll = QWidget()
            layoutScroll = QGridLayout(areaScroll)
            layoutScroll.addWidget(label1, 0, 2)
            layoutScroll.addWidget(label2, 0, 1)
            layoutScroll.addWidget(label3, 0, 0)
            layoutScroll.addWidget(label4, 1, 0)
            layoutScroll.addWidget(label5, 1, 1)
            layoutScroll.addWidget(label6, 1, 2)
            layoutScroll.addWidget(label7, 2, 0)
            layoutScroll.addWidget(label8, 2, 1)
            layoutScroll.addWidget(label9, 2, 2)
            layoutScroll.addWidget(label10, 3, 0)
            layoutScroll.addWidget(label11, 3, 1)
            layoutScroll.addWidget(label12, 3, 2)
            layoutScroll.addWidget(label13, 4, 0)
            layoutScroll.addWidget(label14, 4, 1)
            layoutScroll.addWidget(label15, 4, 2)
            styleLine = "border: 3px solid black;"
            line1 = QLabel()
            line1.setFixedSize(184,2)
            line1.setStyleSheet(styleLine)
            line1.setGeometry(383,120,400,400)
            line15 = QLabel()
            line15.setFixedSize(184,2)
            line15.setStyleSheet(styleLine)
            line15.setGeometry(763,320,400,400)
            line2 = QLabel()
            line2.setFixedSize(184,2)
            line2.setStyleSheet(styleLine)
            line2.setGeometry(383,320,400,400)
            line11 = QLabel()
            line11.setFixedSize(184,2)
            line11.setStyleSheet(styleLine)
            line11.setGeometry(383,320,400,400)
            line4 = QLabel()
            line4.setFixedSize(184,2)
            line4.setStyleSheet(styleLine)
            line4.setGeometry(383,520,400,400)
            line3 = QLabel()
            line3.setFixedSize(184,2)
            line3.setStyleSheet(styleLine)
            line3.setGeometry(383,730,400,400)
            line5 = QLabel()
            line5.setFixedSize(184,2)
            line5.setStyleSheet(styleLine)
            line5.setGeometry(383,939,400,400)
            line6 = QLabel()
            line6.setFixedSize(184,2)
            line6.setStyleSheet(styleLine)
            line6.setGeometry(763,120,400,400)
            line8 = QLabel()
            line8.setFixedSize(184,2)
            line8.setStyleSheet(styleLine)
            line8.setGeometry(763,520,400,400)
            line9 = QLabel()
            line9.setFixedSize(184,2)
            line9.setStyleSheet(styleLine)
            line9.setGeometry(763,730,400,400)
            line10 = QLabel()
            line10.setFixedSize(184,2)
            line10.setStyleSheet(styleLine)
            line10.setGeometry(763,939,400,400)
            line12 = QLabel()
            line12.setFixedSize(2,13)
            line12.setStyleSheet(styleLine)
            line12.setGeometry(286,210,400,400)
            line7 = QLabel()
            line7.setFixedSize(2,13)
            line7.setStyleSheet(styleLine)
            line7.setGeometry(286,420,400,400)
            line13 = QLabel()
            line13.setFixedSize(2,13)
            line13.setStyleSheet(styleLine)
            line13.setGeometry(286,630,400,400)
            line14 = QLabel()
            line14.setFixedSize(2,12)
            line14.setStyleSheet(styleLine)
            line14.setGeometry(286,840,400,400)
            line16 = QLabel()
            line16.setFixedSize(2,12)
            line16.setStyleSheet(styleLine)
            line16.setGeometry(666,840,400,400)
            line17 = QLabel()
            line17.setFixedSize(2,13)
            line17.setStyleSheet(styleLine)
            line17.setGeometry(666,210,400,400)
            line18 = QLabel()
            line18.setFixedSize(2,13)
            line18.setStyleSheet(styleLine)
            line18.setGeometry(666,420,400,400)
            line19 = QLabel()
            line19.setFixedSize(2,13)
            line19.setStyleSheet(styleLine)
            line19.setGeometry(666,630,400,400)
            line20 = QLabel()
            line20.setFixedSize(2,12)
            line20.setStyleSheet(styleLine)
            line20.setGeometry(1049,840,400,400)
            line21 = QLabel()
            line21.setFixedSize(2,13)
            line21.setStyleSheet(styleLine)
            line21.setGeometry(1049,210,400,400)
            line22 = QLabel()
            line22.setFixedSize(2,13)
            line22.setStyleSheet(styleLine)
            line22.setGeometry(1049,420,400,400)
            line23 = QLabel()
            line23.setFixedSize(2,13)
            line23.setStyleSheet(styleLine)
            line23.setGeometry(1049,630,400,400)
            layoutScroll.addChildWidget(line1)
            layoutScroll.addChildWidget(line2)
            layoutScroll.addChildWidget(line3)
            layoutScroll.addChildWidget(line4)
            layoutScroll.addChildWidget(line5)
            layoutScroll.addChildWidget(line6)
            layoutScroll.addChildWidget(line7)
            layoutScroll.addChildWidget(line8)
            layoutScroll.addChildWidget(line9)
            layoutScroll.addChildWidget(line10)
            layoutScroll.addChildWidget(line11)
            layoutScroll.addChildWidget(line12)
            layoutScroll.addChildWidget(line13)
            layoutScroll.addChildWidget(line14)
            layoutScroll.addChildWidget(line15)
            layoutScroll.addChildWidget(line16)
            layoutScroll.addChildWidget(line17)
            layoutScroll.addChildWidget(line18)
            layoutScroll.addChildWidget(line19)
            layoutScroll.addChildWidget(line20)
            layoutScroll.addChildWidget(line21)
            layoutScroll.addChildWidget(line22)
            layoutScroll.addChildWidget(line23)
            self.mainWindow.scrollArea_2.setWidget(areaScroll)
            label1.show()
            label2.show()
            label3.show()
            label4.show()
            label5.show()
            label6.show()
            label7.show()
            label8.show()
            label9.show()
            label10.show()
            label11.show()
            label12.show()
            label13.show()
            label14.show()
            label15.show()

    def UpdateGraphForSteps(self, day, id, workshift):
        if day == 'Monday' and workshift == 3:
                self.monday3rdShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.monday3rdShiftForSteps:
                    if j + 1 == len(self.monday3rdShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label1.setText('Monday - 3rd shift\n{' + text + "}")
        elif day == 'Monday' and workshift == 2:
                self.monday2ndShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.monday2ndShiftForSteps:
                    if j + 1 == len(self.monday2ndShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label2.setText('Monday - 2nd shift\n{' + text + "}")
        elif day == 'Monday' and workshift == 1:
                self.monday1stShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.monday1stShiftForSteps:
                    if j + 1 == len(self.monday1stShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label3.setText('Monday - 1st shift\n{' + text + "}") 

        elif day == 'Tuesday' and workshift == 3:
                self.tuesday3rdShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.tuesday3rdShiftForSteps:
                    if j + 1 == len(self.tuesday3rdShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label6.setText('Tuesday - 3rd shift\n{' + text + "}")
        elif day == 'Tuesday' and workshift == 2:
                self.tuesday2ndShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.tuesday2ndShiftForSteps:
                    if j + 1 == len(self.tuesday2ndShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label5.setText('Tuesday - 2nd shift\n{' + text + "}")
        elif day == 'Tuesday' and workshift == 1:
                self.tuesday1stShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.tuesday1stShiftForSteps:
                    if j + 1 == len(self.tuesday1stShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label4.setText('Tuesday - 1st shift\n{' + text + "}")

        elif day == 'Wednesday' and workshift == 1:
                self.wednesday1stShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.wednesday1stShiftForSteps:
                    if j + 1 == len(self.wednesday1stShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label7.setText('Wednesday - 1st shift\n{' + text + "}")
        elif day == 'Wednesday' and workshift == 2:
                self.wednesday2ndShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.wednesday2ndShiftForSteps:
                    if j + 1 == len(self.wednesday2ndShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label8.setText('Wednesday - 2nd shift\n{' + text + "}")
        elif day == 'Wednesday' and workshift == 3:
                self.wednesday3rdShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.wednesday3rdShiftForSteps:
                    if j + 1 == len(self.wednesday3rdShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label9.setText('Wednesday - 3rd shift\n{' + text + "}")

        elif day == 'Thursday' and workshift == 1:
                self.thursday1stShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.thursday1stShiftForSteps:
                    if j + 1 == len(self.thursday1stShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label10.setText('Thursday - 1st shift\n{' + text + "}")
        elif day == 'Thursday' and workshift == 2:
                self.thursday2ndShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.thursday2ndShiftForSteps:
                    if j + 1 == len(self.thursday2ndShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label11.setText('Thursday - 2nd shift\n{' + text + "}")
        elif day == 'Thursday' and workshift == 3:
                self.thursday3rdShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.thursday3rdShiftForSteps:
                    if j + 1 == len(self.thursday3rdShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label12.setText('Thursday - 3rd shift\n{' + text + "}")

        elif day == 'Friday' and workshift == 1:
                self.friday1stShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.friday1stShiftForSteps:
                    if j + 1 == len(self.friday1stShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label13.setText('Friday - 1st shift\n{' + text + "}")
        elif day == 'Friday' and workshift == 2:
                self.friday2ndShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.friday2ndShiftForSteps:
                    if j + 1 == len(self.friday2ndShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label14.setText('Friday - 2nd shift\n{' + text + "}")
        elif day == 'Friday' and workshift == 3:
                self.friday3rdShiftForSteps.append(id)
                text = ""
                j = 0
                for number in self.friday3rdShiftForSteps:
                    if j + 1 == len(self.friday3rdShiftForSteps):
                        text = text + str(number)
                    else:
                        text = text + str(number) + ", "
                    j = j + 1
                label15.setText('Friday - 3rd shift\n{' + text + "}")
        QApplication.processEvents()      
        QThread.msleep(1000) 

    def FindASolution(self):
        csp2 = CSP(self.csp.employees)
        obj = csp2.GenerateWorkschedule()
        if obj == 'There is no data in the database':
                QMessageBox.information(None, "Steps", "There is no data in the database", QMessageBox.Ok)
        else:
            if self.funFindSolutionUsed == True and self.allSteps >= len(csp2.saveStepsDays):
                message = "solution found after " + str(len(csp2.saveStepsDays)) + " step(s)"
                QMessageBox.information(None, "Find a solution", message, QMessageBox.Ok)
            else:
                if self.funFindSteps == True:
                    self.monday3rdShiftForSteps = []
                    self.monday1stShiftForSteps = []
                    self.monday2ndShiftForSteps = []
                    self.tuesday3rdShiftForSteps = []
                    self.tuesday2ndShiftForSteps = []
                    self.tuesday1stShiftForSteps = []
                    self.wednesday3rdShiftForSteps = []
                    self.wednesday2ndShiftForSteps = []
                    self.wednesday1stShiftForSteps = []
                    self.thursday3rdShiftForSteps = []
                    self.thursday2ndShiftForSteps = []
                    self.thursday1stShiftForSteps = []
                    self.friday3rdShiftForSteps = []
                    self.friday2ndShiftForSteps = []
                    self.friday1stShiftForSteps = []
                    self.funFindSteps = False
                self.mainWindow.textBrowser.clear()
                self.funFindSolutionUsed = True
                self.allSteps = len(csp2.saveStepsDays)
                for i in range(0, self.allSteps, 1):
                    self.UpdateGraphForSteps(csp2.saveStepsDays[i], csp2.saveStepsID[i], csp2.saveStepsWorkshift[i])
                    line = "Day(" + str(csp2.saveStepsDays[i]) + ") -> id_employee(" + str(csp2.saveStepsID[i]) + ") -> work-shift(" + str(csp2.saveStepsWorkshift[i]) + ")"
                    self.mainWindow.textBrowser.append(line)
                message = "solution found after " + str(len(csp2.saveStepsDays)) + " step(s)"
                QMessageBox.information(None, "Find a solution", message, QMessageBox.Ok)
                self.mainWindow.textBrowser.clear()
                for line in csp2.PrintWorkschedule():
                    self.mainWindow.textBrowser.append(line)

    def Steps(self):
        valueStep = self.mainWindow.lineEdit.text()
        if not (valueStep.isdigit() and int(valueStep) > 0):
            QMessageBox.critical(None, "Error", "Bad value", QMessageBox.Ok)
        else:
            self.funFindSteps = True
            csp2 = CSP(self.csp.employees)
            obj = csp2.GenerateWorkschedule()
            if obj == 'There is no data in the database':
                 QMessageBox.information(None, "Steps", "There is no data in the database", QMessageBox.Ok)
            else:
                if self.funFindSolutionUsed == True and self.allSteps >= len(csp2.saveStepsDays):
                    message = "solution found after " + str(len(csp2.saveStepsDays)) + " step(s)"
                    QMessageBox.information(None, "Find a solution", message, QMessageBox.Ok)
                else:
                    if self.allSteps <= len(csp2.saveStepsDays):
                        if self.allSteps + int(valueStep) >= len(csp2.saveStepsDays):
                            self.allSteps = len(csp2.saveStepsDays)
                        else:
                            self.allSteps = self.allSteps + int(valueStep)
                        for i in range(self.startStep, self.allSteps, 1):
                            self.UpdateGraphForSteps(csp2.saveStepsDays[i], csp2.saveStepsID[i], csp2.saveStepsWorkshift[i])
                            line = "Day(" + str(csp2.saveStepsDays[i]) + ") -> id_employee(" + str(csp2.saveStepsID[i]) + ") -> work-shift(" + str(csp2.saveStepsWorkshift[i]) + ")"
                            self.mainWindow.textBrowser.append(line)
                            self.startStep = i + 1
                        if self.allSteps >= len(csp2.saveStepsDays):
                            message = "solution found after " + str(len(csp2.saveStepsDays)) + " step(s)"
                            QMessageBox.information(None, "Find a solution", message, QMessageBox.Ok)
                            self.mainWindow.textBrowser.clear()
                            for line in csp2.PrintWorkschedule():
                                self.mainWindow.textBrowser.append(line)
                    else:
                        message = "solution found after " + str(len(csp2.saveStepsDays)) + " step(s)"
                        QMessageBox.information(None, "Find a solution", message, QMessageBox.Ok)
                