# Importations.
from crazyGUI import *
import subprocess
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Main Window class.
    def __init__(self, parent=None):
        # Main Window constructor.
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # By default hide tabs.
        self.groupBox_1.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()

        # Set signal actions.
        # Main window.
        self.pushButton0_0.clicked.connect(self.clearTerminal)
        self.pushButton0_1.clicked.connect(self.runROSMaster)

        # Tab 1.
        self.action0_0.triggered.connect(self.shTab1)
        self.pushButton1_0.clicked.connect(self.editCrazyfliesList)
        self.pushButton1_1.clicked.connect(self.editcrazyflieData)
        self.pushButton1_2.clicked.connect(self.editMainLaunchSettings)

        # Tab 2.
        self.action0_1.triggered.connect(self.shTab2)
        self.pushButton2_0.clicked.connect(self.openCfclient)
        self.pushButton2_1.clicked.connect(self.openChooser)

        # Tab 3.
        self.action0_2.triggered.connect(self.shTab3)
        self.pushButton3_0.clicked.connect(self.runPreLaunchSequence)
        self.pushButton3_1.clicked.connect(self.selectFlightScript)
        self.pushButton3_2.clicked.connect(self.fly)


    def clearTerminal(self):
        # Clear terminal.
        subprocess.run("clear", shell=True)
    
    def runROSMaster(self):
        # Run ROS master node.
        # TODO run this in a new terminal or ... in the background?.
        subprocess.run("roslaunch crazyswarm hover_swarm.launch", shell=True)
        print("---------------------------------------------")

    def shTab1(self):
        # Toggle tab 1 visualization.
        if self.action0_0.isChecked():
            self.groupBox_1.show()
            self.groupBox_1.setEnabled(True)
        else:
            self.groupBox_1.hide()
            self.groupBox_1.setEnabled(False)

    def editCrazyfliesList(self):
        # Edit the Crazyflies list configuration file.
        os.chdir("/home/" + os.getlogin() + "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/")
        subprocess.run("gedit launch/allCrazyflies.yaml", shell=True)
        print("---------------------------------------------")

    def editcrazyflieData(self):
        # Edit the Crazyflies data configuration file.
        os.chdir("/home/" + os.getlogin() + "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/")
        subprocess.run("gedit launch/crazyflieTypes.yaml", shell=True)
        print("---------------------------------------------")

    def editMainLaunchSettings(self):
        # Edit the main launch settings.
        os.chdir("/home/" + os.getlogin() + "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/")
        subprocess.run("gedit launch/hover_swarm.launch", shell=True)
        print("---------------------------------------------")

    def shTab2(self):
        # Toggle tab 2 visualization.
        if self.action0_1.isChecked():
            self.groupBox_2.show()
            self.groupBox_2.setEnabled(True)
        else:
            self.groupBox_2.hide()
            self.groupBox_2.setEnabled(False)
    
    def openCfclient(self):
        # Open the Cfclient program by Bitcraze.
        p = subprocess.Popen("cfclient", shell=True)
        print("---------------------------------------------")

    def openChooser(self):
        # Open chooser.py.
        os.chdir("/home/" + os.getlogin() + "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/")
        subprocess.run("python3 chooser.py", shell=True)
        print("---------------------------------------------")

    def shTab3(self):
        # Toggle tab 3 visualization.
        if self.action0_2.isChecked():
            self.groupBox_3.show()
            self.groupBox_3.setEnabled(True)
        else:
            self.groupBox_3.hide()
            self.groupBox_3.setEnabled(False)

    def runPreLaunchSequence(self):
        # To run this program you will need https://github.com/santiagorg2401/ras_choreographies
        os.chdir("/home/" + os.getlogin() + "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/ras_choreographies/scripts/")
        subprocess.run("python3 preLaunchSequence.py", shell=True)
        print("---------------------------------------------")

    def selectFlightScript(self):
        # TODO add a file selection window and get its path.
        pass
    
    def fly(self):
        # Run the selected script in selectFlightScript.
        os.chdir("/home/" + os.getlogin() + "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/") # TODO Adjust to fly the selected script instead.

        if self.action2_1.isChecked():
            subprocess.run("python3 niceHover.py --sim --vis vispy", shell=True)
        else:
            subprocess.run("python3 niceHover.py ", shell=True)
        
        print("---------------------------------------------")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()