from crazyGUI import *
import subprocess

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.groupBox_1.hide()
        self.groupBox_2.hide()

        # Set signal actions.
        # Main window.
        self.pushButton0_0.clicked.connect(self.clearTerminal)
        self.pushButton0_1.clicked.connect(self.runROSMaster)
        # Tab 1.
        self.action_1.triggered.connect(self.shTab1)
        self.pushButton1_0.clicked.connect(self.editCrazyfliesList)
        self.pushButton1_1.clicked.connect(self.editcrazyflieData)
        self.pushButton1_2.clicked.connect(self.editMainLaunchSettings)

        # Tab 2.
        self.action_2.triggered.connect(self.shTab2)
        self.pushButton2_0.clicked.connect(self.openCfclient)
        self.pushButton2_1.clicked.connect(self.openChooser)

    def clearTerminal(self):
        subprocess.run("clear", shell=True)
    
    def runROSMaster(self):
        subprocess.run("roslaunch crazyswarm hover_swarm.launch", shell=True)

    def shTab1(self):
        if self.action_1.isChecked():
            self.groupBox_1.show()
            self.groupBox_1.setEnabled(True)
        else:
            self.groupBox_1.hide()
            self.groupBox_1.setEnabled(False)

    def editCrazyfliesList(self):
        subprocess.run("cd ..", shell=True)
        subprocess.run("gedit launch/allCrazyflies.yaml", shell=True)

    def editcrazyflieData(self):
        subprocess.run("cd ..", shell=True)
        subprocess.run("gedit launch/crazyflieTypes.yaml", shell=True)

    def editMainLaunchSettings(self):
        subprocess.run("cd ..", shell=True)
        subprocess.run("gedit launch/hover_swarm.launch", shell=True)

    def shTab2(self):
        if self.action_2.isChecked():
            self.groupBox_2.show()
            self.groupBox_2.setEnabled(True)
        else:
            self.groupBox_2.hide()
            self.groupBox_2.setEnabled(False)
    
    def openCfclient(self):
        p = subprocess.Popen("cfclient", shell=True)

    def openChooser(self):
        subprocess.run("cd ..", shell=True)
        subprocess.run("python3 scripts/chooser.py", shell=True)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()