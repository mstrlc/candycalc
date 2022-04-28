# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        mainWindow.resize(420, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(420, 550))
        mainWindow.setMaximumSize(QtCore.QSize(420, 550))
        palette = QtGui.QPalette()
        mainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("QLabel#labelMain {\n"
"    font: 36pt;\n"
"    font-weight: 700;\n"
"    color: #1D1D1D;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"\n"
"QLabel#labelSecond {\n"
"    font: 20pt;\n"
"    font-weight: 500;\n"
"    color: #374F9A;\n"
"    padding-top: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 20pt;\n"
"    color: #FFFFFF;\n"
"    font-weight: 500;\n"
"    background-color: #2B3452;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #364166;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #22283A;\n"
"}\n"
"QFrame {\n"
"    background-color: #F5F5F5;\n"
"}\n"
"")
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        mainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.labelSecond = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSecond.sizePolicy().hasHeightForWidth())
        self.labelSecond.setSizePolicy(sizePolicy)
        self.labelSecond.setText("")
        self.labelSecond.setTextFormat(QtCore.Qt.PlainText)
        self.labelSecond.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSecond.setIndent(20)
        self.labelSecond.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSecond.setObjectName("labelSecond")
        self.verticalLayout.addWidget(self.labelSecond)
        self.labelMain = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMain.sizePolicy().hasHeightForWidth())
        self.labelMain.setSizePolicy(sizePolicy)
        self.labelMain.setLineWidth(0)
        self.labelMain.setText("")
        self.labelMain.setTextFormat(QtCore.Qt.PlainText)
        self.labelMain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMain.setIndent(20)
        self.labelMain.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelMain.setObjectName("labelMain")
        self.verticalLayout.addWidget(self.labelMain)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonFact = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonFact.sizePolicy().hasHeightForWidth())
        self.pushButtonFact.setSizePolicy(sizePolicy)
        self.pushButtonFact.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonFact.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonFact.setAcceptDrops(False)
        self.pushButtonFact.setAutoFillBackground(False)
        self.pushButtonFact.setStyleSheet("")
        self.pushButtonFact.setFlat(False)
        self.pushButtonFact.setObjectName("pushButtonFact")
        self.buttonsNum = QtWidgets.QButtonGroup(mainWindow)
        self.buttonsNum.setObjectName("buttonsNum")
        self.buttonsNum.setExclusive(False)
        self.buttonsNum.addButton(self.pushButtonFact)
        self.gridLayout.addWidget(self.pushButtonFact, 3, 4, 1, 1)
        self.pushButtonRBrac = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRBrac.sizePolicy().hasHeightForWidth())
        self.pushButtonRBrac.setSizePolicy(sizePolicy)
        self.pushButtonRBrac.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRBrac.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonRBrac.setAcceptDrops(False)
        self.pushButtonRBrac.setAutoFillBackground(False)
        self.pushButtonRBrac.setStyleSheet("")
        self.pushButtonRBrac.setFlat(False)
        self.pushButtonRBrac.setObjectName("pushButtonRBrac")
        self.buttonsNum.addButton(self.pushButtonRBrac)
        self.gridLayout.addWidget(self.pushButtonRBrac, 1, 4, 1, 1)
        self.pushButtonEq = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEq.sizePolicy().hasHeightForWidth())
        self.pushButtonEq.setSizePolicy(sizePolicy)
        self.pushButtonEq.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonEq.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonEq.setAcceptDrops(False)
        self.pushButtonEq.setAutoFillBackground(False)
        self.pushButtonEq.setStyleSheet("QPushButton {\n"
"    background-color: #A33C7E;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #954177;\n"
"}\n"
"")
        self.pushButtonEq.setDefault(False)
        self.pushButtonEq.setFlat(False)
        self.pushButtonEq.setObjectName("pushButtonEq")
        self.gridLayout.addWidget(self.pushButtonEq, 5, 5, 1, 1)
        self.pushButtonCE = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCE.sizePolicy().hasHeightForWidth())
        self.pushButtonCE.setSizePolicy(sizePolicy)
        self.pushButtonCE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonCE.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonCE.setAcceptDrops(False)
        self.pushButtonCE.setAutoFillBackground(False)
        self.pushButtonCE.setStyleSheet("")
        self.pushButtonCE.setFlat(False)
        self.pushButtonCE.setObjectName("pushButtonCE")
        self.buttonsNum.addButton(self.pushButtonCE)
        self.gridLayout.addWidget(self.pushButtonCE, 1, 1, 1, 1)
        self.pushButtonDel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDel.sizePolicy().hasHeightForWidth())
        self.pushButtonDel.setSizePolicy(sizePolicy)
        self.pushButtonDel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonDel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonDel.setAcceptDrops(False)
        self.pushButtonDel.setAutoFillBackground(False)
        self.pushButtonDel.setStyleSheet("")
        self.pushButtonDel.setFlat(False)
        self.pushButtonDel.setObjectName("pushButtonDel")
        self.buttonsNum.addButton(self.pushButtonDel)
        self.gridLayout.addWidget(self.pushButtonDel, 1, 2, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3.sizePolicy().hasHeightForWidth())
        self.pushButton3.setSizePolicy(sizePolicy)
        self.pushButton3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton3.setAcceptDrops(False)
        self.pushButton3.setAutoFillBackground(False)
        self.pushButton3.setStyleSheet("")
        self.pushButton3.setFlat(False)
        self.pushButton3.setObjectName("pushButton3")
        self.buttonsNum.addButton(self.pushButton3)
        self.gridLayout.addWidget(self.pushButton3, 4, 3, 1, 1)
        self.pushButtonLBrac = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLBrac.sizePolicy().hasHeightForWidth())
        self.pushButtonLBrac.setSizePolicy(sizePolicy)
        self.pushButtonLBrac.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonLBrac.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonLBrac.setAcceptDrops(False)
        self.pushButtonLBrac.setAutoFillBackground(False)
        self.pushButtonLBrac.setStyleSheet("")
        self.pushButtonLBrac.setFlat(False)
        self.pushButtonLBrac.setObjectName("pushButtonLBrac")
        self.buttonsNum.addButton(self.pushButtonLBrac)
        self.gridLayout.addWidget(self.pushButtonLBrac, 1, 3, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1.sizePolicy().hasHeightForWidth())
        self.pushButton1.setSizePolicy(sizePolicy)
        self.pushButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton1.setAcceptDrops(False)
        self.pushButton1.setAutoFillBackground(False)
        self.pushButton1.setStyleSheet("")
        self.pushButton1.setFlat(False)
        self.pushButton1.setObjectName("pushButton1")
        self.buttonsNum.addButton(self.pushButton1)
        self.gridLayout.addWidget(self.pushButton1, 4, 1, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton0.sizePolicy().hasHeightForWidth())
        self.pushButton0.setSizePolicy(sizePolicy)
        self.pushButton0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton0.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton0.setAcceptDrops(False)
        self.pushButton0.setAutoFillBackground(False)
        self.pushButton0.setStyleSheet("")
        self.pushButton0.setFlat(False)
        self.pushButton0.setObjectName("pushButton0")
        self.buttonsNum.addButton(self.pushButton0)
        self.gridLayout.addWidget(self.pushButton0, 5, 1, 1, 2)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton2.setAcceptDrops(False)
        self.pushButton2.setAutoFillBackground(False)
        self.pushButton2.setStyleSheet("")
        self.pushButton2.setFlat(False)
        self.pushButton2.setObjectName("pushButton2")
        self.buttonsNum.addButton(self.pushButton2)
        self.gridLayout.addWidget(self.pushButton2, 4, 2, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton7.sizePolicy().hasHeightForWidth())
        self.pushButton7.setSizePolicy(sizePolicy)
        self.pushButton7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton7.setAcceptDrops(False)
        self.pushButton7.setAutoFillBackground(False)
        self.pushButton7.setStyleSheet("")
        self.pushButton7.setFlat(False)
        self.pushButton7.setObjectName("pushButton7")
        self.buttonsNum.addButton(self.pushButton7)
        self.gridLayout.addWidget(self.pushButton7, 2, 1, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton8.sizePolicy().hasHeightForWidth())
        self.pushButton8.setSizePolicy(sizePolicy)
        self.pushButton8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton8.setAcceptDrops(False)
        self.pushButton8.setAutoFillBackground(False)
        self.pushButton8.setStyleSheet("")
        self.pushButton8.setFlat(False)
        self.pushButton8.setObjectName("pushButton8")
        self.buttonsNum.addButton(self.pushButton8)
        self.gridLayout.addWidget(self.pushButton8, 2, 2, 1, 1)
        self.pushButtonPlus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPlus.sizePolicy().hasHeightForWidth())
        self.pushButtonPlus.setSizePolicy(sizePolicy)
        self.pushButtonPlus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonPlus.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonPlus.setAcceptDrops(False)
        self.pushButtonPlus.setAutoFillBackground(False)
        self.pushButtonPlus.setStyleSheet("QPushButton {\n"
"    background-color: #374F9A;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #33447B;\n"
"}")
        self.pushButtonPlus.setFlat(False)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.buttonsOper = QtWidgets.QButtonGroup(mainWindow)
        self.buttonsOper.setObjectName("buttonsOper")
        self.buttonsOper.setExclusive(False)
        self.buttonsOper.addButton(self.pushButtonPlus)
        self.gridLayout.addWidget(self.pushButtonPlus, 4, 5, 1, 1)
        self.pushButtonDec = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDec.sizePolicy().hasHeightForWidth())
        self.pushButtonDec.setSizePolicy(sizePolicy)
        self.pushButtonDec.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonDec.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonDec.setAcceptDrops(False)
        self.pushButtonDec.setAutoFillBackground(False)
        self.pushButtonDec.setStyleSheet("")
        self.pushButtonDec.setFlat(False)
        self.pushButtonDec.setObjectName("pushButtonDec")
        self.buttonsNum.addButton(self.pushButtonDec)
        self.gridLayout.addWidget(self.pushButtonDec, 5, 3, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton4.sizePolicy().hasHeightForWidth())
        self.pushButton4.setSizePolicy(sizePolicy)
        self.pushButton4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton4.setAcceptDrops(False)
        self.pushButton4.setAutoFillBackground(False)
        self.pushButton4.setStyleSheet("")
        self.pushButton4.setFlat(False)
        self.pushButton4.setObjectName("pushButton4")
        self.buttonsNum.addButton(self.pushButton4)
        self.gridLayout.addWidget(self.pushButton4, 3, 1, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton9.sizePolicy().hasHeightForWidth())
        self.pushButton9.setSizePolicy(sizePolicy)
        self.pushButton9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton9.setAcceptDrops(False)
        self.pushButton9.setAutoFillBackground(False)
        self.pushButton9.setStyleSheet("")
        self.pushButton9.setFlat(False)
        self.pushButton9.setObjectName("pushButton9")
        self.buttonsNum.addButton(self.pushButton9)
        self.gridLayout.addWidget(self.pushButton9, 2, 3, 1, 1)
        self.pushButtonRoot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRoot.sizePolicy().hasHeightForWidth())
        self.pushButtonRoot.setSizePolicy(sizePolicy)
        self.pushButtonRoot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonRoot.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonRoot.setAcceptDrops(False)
        self.pushButtonRoot.setAutoFillBackground(False)
        self.pushButtonRoot.setStyleSheet("")
        self.pushButtonRoot.setFlat(False)
        self.pushButtonRoot.setObjectName("pushButtonRoot")
        self.buttonsNum.addButton(self.pushButtonRoot)
        self.gridLayout.addWidget(self.pushButtonRoot, 4, 4, 1, 1)
        self.pushButtonDiv = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDiv.sizePolicy().hasHeightForWidth())
        self.pushButtonDiv.setSizePolicy(sizePolicy)
        self.pushButtonDiv.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonDiv.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonDiv.setAcceptDrops(False)
        self.pushButtonDiv.setAutoFillBackground(False)
        self.pushButtonDiv.setStyleSheet("QPushButton {\n"
"    background-color: #374F9A;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #33447B;\n"
"}")
        self.pushButtonDiv.setFlat(False)
        self.pushButtonDiv.setObjectName("pushButtonDiv")
        self.buttonsOper.addButton(self.pushButtonDiv)
        self.gridLayout.addWidget(self.pushButtonDiv, 1, 5, 1, 1)
        self.pushButtonMin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMin.sizePolicy().hasHeightForWidth())
        self.pushButtonMin.setSizePolicy(sizePolicy)
        self.pushButtonMin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonMin.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonMin.setAcceptDrops(False)
        self.pushButtonMin.setAutoFillBackground(False)
        self.pushButtonMin.setStyleSheet("QPushButton {\n"
"    background-color: #374F9A;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #33447B;\n"
"}")
        self.pushButtonMin.setFlat(False)
        self.pushButtonMin.setObjectName("pushButtonMin")
        self.buttonsOper.addButton(self.pushButtonMin)
        self.gridLayout.addWidget(self.pushButtonMin, 3, 5, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton6.sizePolicy().hasHeightForWidth())
        self.pushButton6.setSizePolicy(sizePolicy)
        self.pushButton6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton6.setAcceptDrops(False)
        self.pushButton6.setAutoFillBackground(False)
        self.pushButton6.setStyleSheet("")
        self.pushButton6.setFlat(False)
        self.pushButton6.setObjectName("pushButton6")
        self.buttonsNum.addButton(self.pushButton6)
        self.gridLayout.addWidget(self.pushButton6, 3, 3, 1, 1)
        self.pushButtonExp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonExp.sizePolicy().hasHeightForWidth())
        self.pushButtonExp.setSizePolicy(sizePolicy)
        self.pushButtonExp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonExp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonExp.setAcceptDrops(False)
        self.pushButtonExp.setAutoFillBackground(False)
        self.pushButtonExp.setStyleSheet("")
        self.pushButtonExp.setAutoDefault(False)
        self.pushButtonExp.setDefault(False)
        self.pushButtonExp.setFlat(False)
        self.pushButtonExp.setObjectName("pushButtonExp")
        self.buttonsNum.addButton(self.pushButtonExp)
        self.gridLayout.addWidget(self.pushButtonExp, 5, 4, 1, 1)
        self.pushButtonMul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMul.sizePolicy().hasHeightForWidth())
        self.pushButtonMul.setSizePolicy(sizePolicy)
        self.pushButtonMul.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonMul.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonMul.setAcceptDrops(False)
        self.pushButtonMul.setAutoFillBackground(False)
        self.pushButtonMul.setStyleSheet("QPushButton {\n"
"    background-color: #374F9A;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #33447B;\n"
"}")
        self.pushButtonMul.setFlat(False)
        self.pushButtonMul.setObjectName("pushButtonMul")
        self.buttonsOper.addButton(self.pushButtonMul)
        self.gridLayout.addWidget(self.pushButtonMul, 2, 5, 1, 1)
        self.pushButtonLn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLn.sizePolicy().hasHeightForWidth())
        self.pushButtonLn.setSizePolicy(sizePolicy)
        self.pushButtonLn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonLn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonLn.setAcceptDrops(False)
        self.pushButtonLn.setAutoFillBackground(False)
        self.pushButtonLn.setStyleSheet("")
        self.pushButtonLn.setFlat(False)
        self.pushButtonLn.setObjectName("pushButtonLn")
        self.buttonsNum.addButton(self.pushButtonLn)
        self.gridLayout.addWidget(self.pushButtonLn, 2, 4, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton5.sizePolicy().hasHeightForWidth())
        self.pushButton5.setSizePolicy(sizePolicy)
        self.pushButton5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton5.setAcceptDrops(False)
        self.pushButton5.setAutoFillBackground(False)
        self.pushButton5.setStyleSheet("")
        self.pushButton5.setFlat(False)
        self.pushButton5.setObjectName("pushButton5")
        self.buttonsNum.addButton(self.pushButton5)
        self.gridLayout.addWidget(self.pushButton5, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 420, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menuBar)
        self.actionOpen_user_guide = QtWidgets.QAction(mainWindow)
        self.actionOpen_user_guide.setObjectName("actionOpen_user_guide")
        self.actionQuit = QtWidgets.QAction(mainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit_2 = QtWidgets.QAction(mainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionOpen_user_guide_2 = QtWidgets.QAction(mainWindow)
        self.actionOpen_user_guide_2.setObjectName("actionOpen_user_guide_2")
        self.menuFile.addAction(self.actionQuit_2)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "candyCalc"))
        self.pushButtonFact.setText(_translate("mainWindow", "x!"))
        self.pushButtonRBrac.setText(_translate("mainWindow", ")"))
        self.pushButtonEq.setText(_translate("mainWindow", "="))
        self.pushButtonCE.setText(_translate("mainWindow", "CLR"))
        self.pushButtonDel.setText(_translate("mainWindow", "DEL"))
        self.pushButton3.setText(_translate("mainWindow", "3"))
        self.pushButtonLBrac.setText(_translate("mainWindow", "("))
        self.pushButton1.setText(_translate("mainWindow", "1"))
        self.pushButton0.setText(_translate("mainWindow", "0"))
        self.pushButton2.setText(_translate("mainWindow", "2"))
        self.pushButton7.setText(_translate("mainWindow", "7"))
        self.pushButton8.setText(_translate("mainWindow", "8"))
        self.pushButtonPlus.setText(_translate("mainWindow", "+"))
        self.pushButtonDec.setText(_translate("mainWindow", "."))
        self.pushButton4.setText(_translate("mainWindow", "4"))
        self.pushButton9.setText(_translate("mainWindow", "9"))
        self.pushButtonRoot.setText(_translate("mainWindow", "√x"))
        self.pushButtonDiv.setText(_translate("mainWindow", "/"))
        self.pushButtonMin.setText(_translate("mainWindow", "–"))
        self.pushButton6.setText(_translate("mainWindow", "6"))
        self.pushButtonExp.setText(_translate("mainWindow", "x^n"))
        self.pushButtonMul.setText(_translate("mainWindow", "×"))
        self.pushButtonLn.setText(_translate("mainWindow", "ln(x)"))
        self.pushButton5.setText(_translate("mainWindow", "5"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionOpen_user_guide.setText(_translate("mainWindow", "Open user guide"))
        self.actionQuit.setText(_translate("mainWindow", "Quit"))
        self.actionQuit_2.setText(_translate("mainWindow", "Quit"))
        self.actionOpen_user_guide_2.setText(_translate("mainWindow", "Open user guide"))
