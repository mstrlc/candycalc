import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_mainWindow

class mainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton0.clicked.connect(self.addCharacter)
        self.pushButton1.clicked.connect(self.addCharacter)
        self.pushButton2.clicked.connect(self.addCharacter)
        self.pushButton3.clicked.connect(self.addCharacter)
        self.pushButton4.clicked.connect(self.addCharacter)
        self.pushButton5.clicked.connect(self.addCharacter)
        self.pushButton6.clicked.connect(self.addCharacter)
        self.pushButton7.clicked.connect(self.addCharacter)
        self.pushButton8.clicked.connect(self.addCharacter)
        self.pushButton9.clicked.connect(self.addCharacter)
        self.pushButtonDec.clicked.connect(self.addCharacter)
        self.pushButtonLBrac.clicked.connect(self.addCharacter)
        self.pushButtonRBrac.clicked.connect(self.addCharacter)
        self.pushButtonLn.clicked.connect(self.addCharacter)
        self.pushButtonFact.clicked.connect(self.addCharacter)
        self.pushButtonRoot.clicked.connect(self.addCharacter)
        self.pushButtonExp.clicked.connect(self.addCharacter)
        self.pushButtonDiv.clicked.connect(self.addCharacter)
        self.pushButtonMul.clicked.connect(self.addCharacter)
        self.pushButtonMin.clicked.connect(self.addCharacter)
        self.pushButtonPlus.clicked.connect(self.addCharacter)
        self.pushButtonDel.clicked.connect(self.deleteDigit)
        self.pushButtonCE.clicked.connect(self.clearAll)
        self.pushButtonEq.clicked.connect(self.finishCalculation)

    def addCharacter(self):
        self.labelMain.setText(self.labelMain.text() + self.sender().text())

    def deleteDigit(self):
        self.labelMain.setText(self.labelMain.text()[:-1])

    def clearAll(self):
        self.labelSecond.setText("")
        self.labelMain.setText("")

    def finishCalculation(self):
        self.labelSecond.setText(self.labelMain.text())
        self.labelMain.setText(str(eval(self.labelMain.text())))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
