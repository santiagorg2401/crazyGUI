# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crazyGUI/crazyGUI_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 480)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setEnabled(False)
        self.groupBox_1.setObjectName("groupBox_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.groupBox_1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton1_1 = QtWidgets.QPushButton(self.splitter)
        self.pushButton1_1.setObjectName("pushButton1_1")
        self.pushButton1_0 = QtWidgets.QPushButton(self.splitter)
        self.pushButton1_0.setObjectName("pushButton1_0")
        self.pushButton1_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton1_2.setObjectName("pushButton1_2")
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout_3.addWidget(self.groupBox_1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton2_0 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton2_0.setObjectName("pushButton2_0")
        self.pushButton2_1 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton2_1.setObjectName("pushButton2_1")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.pushButton3_0 = QtWidgets.QPushButton(self.splitter_4)
        self.pushButton3_0.setObjectName("pushButton3_0")
        self.pushButton3_1 = QtWidgets.QPushButton(self.splitter_4)
        self.pushButton3_1.setObjectName("pushButton3_1")
        self.pushButton3_2 = QtWidgets.QPushButton(self.splitter_4)
        self.pushButton3_2.setObjectName("pushButton3_2")
        self.verticalLayout_4.addWidget(self.splitter_4)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pushButton0_1 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton0_1.setObjectName("pushButton0_1")
        self.pushButton0_0 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton0_0.setObjectName("pushButton0_0")
        self.verticalLayout_3.addWidget(self.splitter_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("image: url(:/icons/crazyflie.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 22))
        self.menubar.setObjectName("menubar")
        self.menuedir = QtWidgets.QMenu(self.menubar)
        self.menuedir.setObjectName("menuedir")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSelect_language = QtWidgets.QMenu(self.menuEdit)
        self.menuSelect_language.setObjectName("menuSelect_language")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action0_0 = QtWidgets.QAction(MainWindow)
        self.action0_0.setCheckable(True)
        self.action0_0.setShortcut("")
        self.action0_0.setObjectName("action0_0")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionSpanish = QtWidgets.QAction(MainWindow)
        self.actionSpanish.setCheckable(True)
        self.actionSpanish.setObjectName("actionSpanish")
        self.action0_1 = QtWidgets.QAction(MainWindow)
        self.action0_1.setCheckable(True)
        self.action0_1.setObjectName("action0_1")
        self.actionIssues = QtWidgets.QAction(MainWindow)
        self.actionIssues.setObjectName("actionIssues")
        self.actionAbout_CrazyGUI = QtWidgets.QAction(MainWindow)
        self.actionAbout_CrazyGUI.setObjectName("actionAbout_CrazyGUI")
        self.action0_2 = QtWidgets.QAction(MainWindow)
        self.action0_2.setCheckable(True)
        self.action0_2.setObjectName("action0_2")
        self.action2_1 = QtWidgets.QAction(MainWindow)
        self.action2_1.setCheckable(True)
        self.action2_1.setObjectName("action2_1")
        self.menuedir.addAction(self.action0_0)
        self.menuedir.addAction(self.action0_1)
        self.menuedir.addAction(self.action0_2)
        self.menuSelect_language.addAction(self.actionEnglish)
        self.menuSelect_language.addAction(self.actionSpanish)
        self.menuEdit.addAction(self.menuSelect_language.menuAction())
        self.menuEdit.addAction(self.action2_1)
        self.menuHelp.addAction(self.actionIssues)
        self.menuHelp.addAction(self.actionAbout_CrazyGUI)
        self.menubar.addAction(self.menuedir.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CrazyGUI"))
        self.groupBox_1.setTitle(_translate("MainWindow", "1. Adjust configuration files."))
        self.pushButton1_1.setText(_translate("MainWindow", "Edit crazyflie data."))
        self.pushButton1_0.setText(_translate("MainWindow", "Edit crazyflies list."))
        self.pushButton1_2.setText(_translate("MainWindow", "Edit main launch settings."))
        self.groupBox_2.setTitle(_translate("MainWindow", "2. Tools."))
        self.pushButton2_0.setText(_translate("MainWindow", "Open cfclient."))
        self.pushButton2_1.setText(_translate("MainWindow", "Open chooser.py"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3. Flight."))
        self.pushButton3_0.setText(_translate("MainWindow", "Run pre-launch sequence."))
        self.pushButton3_1.setText(_translate("MainWindow", "Select flight script."))
        self.pushButton3_2.setText(_translate("MainWindow", "Fly."))
        self.pushButton0_1.setText(_translate("MainWindow", "Run ROS master."))
        self.pushButton0_0.setText(_translate("MainWindow", "Clear terminal."))
        self.menuedir.setTitle(_translate("MainWindow", "Tabs"))
        self.menuEdit.setTitle(_translate("MainWindow", "Settings"))
        self.menuSelect_language.setTitle(_translate("MainWindow", "Select language"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.action0_0.setText(_translate("MainWindow", "Adjust configuration files."))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionSpanish.setText(_translate("MainWindow", "Spanish"))
        self.action0_1.setText(_translate("MainWindow", "Tools"))
        self.actionIssues.setText(_translate("MainWindow", "Issues"))
        self.actionAbout_CrazyGUI.setText(_translate("MainWindow", "About CrazyGUI"))
        self.action0_2.setText(_translate("MainWindow", "Flight"))
        self.action2_1.setText(_translate("MainWindow", "Enable simulation."))
import crazyflie_rc
