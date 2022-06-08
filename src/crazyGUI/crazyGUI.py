# Importations.
from ui.crazyGUI_mainWindow import *
from ui.crazyGUI_crazyKhoreiaWidget import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import QApplication, QUrl, QDesktopServices
from crazyKhoreia.lightPainting import lightPainting
from crazyKhoreia.multiDronFormation import multiDronFormation

import qdarkstyle
import subprocess
import os
import yaml
import numpy as np
import json
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Main Window class.
    def __init__(self, parent=None):
        # Main Window constructor.
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

        # By default hide tabs.
        self.groupBox_1.hide()
        self.groupBox_2.hide()
        self.groupBox_3.hide()

        self.actionIssues.triggered.connect(self._actionIssues)
        self.actionAbout_CrazyGUI.triggered.connect(self._actionAbout_CrazyGUI)
        self.actionEnable_all_tabs.triggered.connect(
            self._actionEnable_all_tabs)
        self.actionDisable_all_tabs.triggered.connect(
            self._actionDisable_all_tabs)

        # Set signal actions.
        # Main window.
        self.pushButton0_0.clicked.connect(self.clearTerminal)

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
        self.pushButton3_2.clicked.connect(self.openCrazyKhoreiaWidget)
        self.pushButton3_3.clicked.connect(self.fly)

        # self.check_configs()

    def check_configs(self):
        print(sys.executable)
        module_path = os.path.join(os.path.dirname(sys.executable),
                                   'lib', 'cfclient')
        print(module_path)
        file = open(os.path.join("configs/config.json"))
        config = json.load(file)
        print(config)

    def _actionIssues(self):
        url = QUrl("https://github.com/santiagorg2401/crazyGUI/issues")
        QDesktopServices.openUrl(url)

    def _actionAbout_CrazyGUI(self):
        url = QUrl("https://github.com/santiagorg2401/crazyGUI")
        QDesktopServices.openUrl(url)

    def _actionEnable_all_tabs(self):
        self.groupBox_1.show()
        self.action0_0.setChecked(True)
        self.groupBox_1.setEnabled(True)
        self.groupBox_2.show()
        self.action0_1.setChecked(True)
        self.groupBox_2.setEnabled(True)
        self.groupBox_3.show()
        self.action0_2.setChecked(True)
        self.groupBox_3.setEnabled(True)

    def _actionDisable_all_tabs(self):
        self.groupBox_1.hide()
        self.groupBox_1.setEnabled(False)
        self.action0_0.setChecked(False)
        self.groupBox_2.hide()
        self.groupBox_2.setEnabled(False)
        self.action0_1.setChecked(False)
        self.groupBox_3.hide()
        self.action0_2.setChecked(False)
        self.groupBox_3.setEnabled(False)

    def clearTerminal(self):
        # Clear terminal.
        subprocess.run("clear", shell=True)

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
        os.chdir("/home/" + os.getlogin() +
                 "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/")
        subprocess.run("gedit launch/allCrazyflies.yaml", shell=True)
        print("---------------------------------------------")

    def editcrazyflieData(self):
        # Edit the Crazyflies data configuration file.
        os.chdir("/home/" + os.getlogin() +
                 "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/")
        subprocess.run("gedit launch/crazyflieTypes.yaml", shell=True)
        print("---------------------------------------------")

    def editMainLaunchSettings(self):
        # Edit the main launch settings.
        os.chdir("/home/" + os.getlogin() +
                 "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/")
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
        os.chdir("/home/" + os.getlogin() +
                 "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/")
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
        subprocess.run(
            "roslaunch crazyswarm auto_launch.launch preseq:=1 file_path:=" + self.path, shell=True)
        print("---------------------------------------------")

    def selectFlightScript(self):
        # File selection window and get its path.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.path, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if self.path:
            print(self.path)
        pass

    def openCrazyKhoreiaWidget(self):
        self.ckwidget = Form()
        self.ckwidget.show()

    def fly(self):
        # Run the selected script in selectFlightScript.
        if self.action2_1.isChecked():
            os.chdir("/home/" + os.getlogin() +
                     "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/")

            subprocess.run(
                "python3 " + self.path + " --sim --vis vispy", shell=True)
        else:
            subprocess.run(
                "roslaunch crazyswarm auto_launch.launch file_path:=" + self.path, shell=True)
        print("---------------------------------------------")


class Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.ImageSelector.clicked.connect(self.selectImage)
        self.outPathBtn.clicked.connect(self.setOut)
        self.flyLP.clicked.connect(self._flyLP)
        self.selectLPWPS.clicked.connect(self._selectLPWPS)
        self.flyMDF.clicked.connect(self._flyMDF)
        self.selectWPSMDF.clicked.connect(self._selectMDFWPS)
        self.calculateLP.clicked.connect(self._calculateLP)
        self.calculateMDF.clicked.connect(self._calculateMDF)

    def selectImage(self):
        # File selection window and get its path.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.in_path, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if self.in_path:
            print(self.in_path)
        pass

    def setOut(self):
        # File selection window and get its path.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.out_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder') + "/"
        if self.out_path:
            print(self.out_path)
        pass

    def _calculateLP(self):
        # Get values from GUI.
        MAX_WIDTH = self.MAX_WIDTH.value()
        MAX_HEIGHT = self.MAX_HEIGHT.value()
        MIN_WIDTH = self.MIN_WIDTH.value()
        MIN_HEIGHT = self.MIN_HEIGHT.value()

        try:
            in_path = self.in_path
            out_path = self.out_path
        except:
            in_path = None
            out_path = None

        detail = self.detail.value()
        speed = self.speed.value()
        sleepTime = self.sleepTime.value()
        video = self.video.isChecked()
        led = self.led.isChecked()

        if in_path == None:
            print("Please provide an input file.")
        if out_path == None:
            print("Please provide an input folder.")

        if in_path != None and out_path != None:
            print("Calculating your light painting waypoints, please wait ...")

            # Calculate.
            lp = lightPainting(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT,
                               in_path, out_path, detail, speed, sleepTime, video, led)

            print("Done, you may return to GUI.")

        print("---------------------------------------------")

    def _selectLPWPS(self):
        # File selection window and get its path.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.LPWPS_path, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if self.LPWPS_path:
            print("Opened file at: " + self.LPWPS_path)
        pass

        data = np.genfromtxt(self.LPWPS_path, delimiter=',')
        print(
            "Data read succesfully, please place the UAV at the following XY coordinates: " + str(data[0][0:2]))

        x = data[0][0:3]
        x[2] = 0
        node = [{"id": 1, "channel": 80, "initialPosition": x.tolist(),
                 "type": "default"}]
        self.save(node)

    def _flyLP(self):
        if self.LPWPS_path == None:
            print("Please provide a valid file path.")
        else:
            # Run the selected script in selectFlightScript.
            if window.action2_1.isChecked():
                os.chdir("/home/" + os.getlogin() +
                         "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/ras_choreographies/scripts")

                subprocess.run(
                    "python3 auto_lp.py " + self.LPWPS_path + " --sim --vis vispy", shell=True)
            else:
                subprocess.run(
                    "roslaunch crazyswarm auto_launch.launch lp:=1 file_path:=" + self.LPWPS_path, shell=True)
        print("---------------------------------------------")

    def save(self, nodes):
        with open(os.path.join("/home/" + os.getlogin() +
                               "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/launch/", "crazyflies.yaml"), 'w') as outfile:
            yaml.dump({"crazyflies": nodes}, outfile)
        with open(os.path.join("/home/" + os.getlogin() +
                               "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/launch/", "allCrazyflies.yaml"), 'w') as outfile:
            yaml.dump({"crazyflies": nodes}, outfile)

        print("Crazyflies written in configuration files.")
        print("---------------------------------------------")

    def _calculateMDF(self):
        # Get values from GUI.
        MAX_WIDTH = self.MAX_WIDTH.value()
        MAX_HEIGHT = self.MAX_HEIGHT.value()
        MIN_WIDTH = self.MIN_WIDTH.value()
        MIN_HEIGHT = self.MIN_HEIGHT.value()

        try:
            in_path = self.in_path
            out_path = self.out_path
        except:
            in_path = None
            out_path = None

        MIN_DEPTH = self.MIN_DEPTH.value()
        MAX_DEPTH = self.MAX_DEPTH.value()
        boxShape = np.array(
            [self.boxShapeX.value(), self.boxShapeY.value(), self.boxShapeZ.value()])
        nmbr_drones = self.nmbr_drones.value()

        if in_path == None:
            print("Please provide an input file.")
        if out_path == None:
            print("Please provide an input folder.")

        if in_path != None and out_path != None:
            print("Calculating your multi drone formation waypoints, please wait ...")

            # Calculate.
            mdf = multiDronFormation(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT,
                                     MIN_DEPTH, MAX_DEPTH, boxShape, in_path, out_path, nmbr_drones)

            print("Done, you may return to GUI.")
        print("---------------------------------------------")

    def _selectMDFWPS(self):
        # File selection window and get its path.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.MDFWPS_path, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if self.MDFWPS_path:
            print(self.MDFWPS_path)
        pass

        data = np.genfromtxt(self.MDFWPS_path, delimiter=',')
        i = 1
        nodes = []
        for d in data:
            print("Data read succesfully, please place the UAV " +
                  str(i) + " at the following XY coordinates: " + str(d[0:2]))

            x = d[0:3]
            x[2] = 0

            node = {"id": i, "channel": 80,
                    "initialPosition": x.tolist(), "type": "default"}
            nodes.append(node)
            i += 1
        self.save(nodes)

    def _flyMDF(self):
        if self.MDFWPS_path == None:
            print("Please provide a valid file path.")
        else:
            # Run the selected script in selectFlightScript.
            if window.action2_1.isChecked():
                os.chdir("/home/" + os.getlogin() +
                         "/crazyflie/crazyswarm/ros_ws/src/crazyswarm/scripts/ras_choreographies/scripts")

                subprocess.run(
                    "python3 auto_form.py " + self.MDFWPS_path + " --sim --vis vispy", shell=True)
            else:
                subprocess.run(
                    "roslaunch crazyswarm auto_launch.launch mdf:=1 file_path:=" + self.MDFWPS_path, shell=True)
        print("---------------------------------------------")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()

    window.show()
    app.exec_()
