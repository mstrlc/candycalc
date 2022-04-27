from signal import signal
import string
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip import main
from ui import Ui_mainWindow

class mainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons to functions
        # Digit buttons
        self.pushButton0.clicked.connect(lambda:self.addDigit("0"))
        self.pushButton1.clicked.connect(lambda:self.addDigit("1"))
        self.pushButton2.clicked.connect(lambda:self.addDigit("2"))
        self.pushButton3.clicked.connect(lambda:self.addDigit("3"))
        self.pushButton4.clicked.connect(lambda:self.addDigit("4"))
        self.pushButton5.clicked.connect(lambda:self.addDigit("5"))
        self.pushButton6.clicked.connect(lambda:self.addDigit("6"))
        self.pushButton7.clicked.connect(lambda:self.addDigit("7"))
        self.pushButton8.clicked.connect(lambda:self.addDigit("8"))
        self.pushButton9.clicked.connect(lambda:self.addDigit("9"))

        # Decimal point button
        self.pushButtonDec.clicked.connect(self.addDecimal)

        # Bracket buttons
        self.pushButtonLBrac.clicked.connect(lambda:self.addBracket("("))
        self.pushButtonRBrac.clicked.connect(lambda:self.addBracket(")"))

        # Function buttons
        self.pushButtonLn.clicked.connect(lambda:self.addFunction("ln("))
        self.pushButtonFact.clicked.connect(lambda:self.addFunction("!"))
        self.pushButtonRoot.clicked.connect(lambda:self.addFunction("√("))
        self.pushButtonExp.clicked.connect(lambda:self.addFunction("^"))
        self.pushButtonDiv.clicked.connect(lambda:self.addFunction("/"))
        self.pushButtonMul.clicked.connect(lambda:self.addFunction("×"))
        self.pushButtonMin.clicked.connect(lambda:self.addFunction("-"))
        self.pushButtonPlus.clicked.connect(lambda:self.addFunction("+"))

        # Other buttons
        self.pushButtonDel.clicked.connect(self.deleteDigit)
        self.pushButtonCE.clicked.connect(self.clearAll)
        self.pushButtonEq.clicked.connect(self.finishCalculation)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_0:
            self.addDigit("0")
        elif e.key() == Qt.Key_1:
            self.addDigit("1")
        elif e.key() == Qt.Key_2:
            self.addDigit("2")
        elif e.key() == Qt.Key_3:
            self.addDigit("3")
        elif e.key() == Qt.Key_4:
            self.addDigit("4")
        elif e.key() == Qt.Key_5:
            self.addDigit("5")
        elif e.key() == Qt.Key_6:
            self.addDigit("6")
        elif e.key() == Qt.Key_7:
            self.addDigit("7")
        elif e.key() == Qt.Key_8:
            self.addDigit("8")
        elif e.key() == Qt.Key_9:
            self.addDigit("9")
        elif e.key() == Qt.Key_Backspace or e.key() == Qt.Key_Delete:
            self.deleteDigit()
        elif e.key() == Qt.Key_Plus:
            self.addFunction("+")
        elif e.key() == Qt.Key_Minus:
            self.addFunction("-")
        elif e.key() == Qt.Key_Asterisk or e.key() == Qt.Key_X:
            self.addFunction("×")
        elif e.key() == Qt.Key_Slash:
            self.addFunction("/")
        elif e.key() == Qt.Key_L:
            self.addFunction("ln(")
        elif e.key() == Qt.Key_R:
            self.addFunction("√(")
        elif e.key() == Qt.Key_Period or e.key() == Qt.Key_Comma:
            self.addDecimal()
        elif e.key() == Qt.Key_Equal or e.key() == Qt.Key_Enter:
            self.finishCalculation()
        elif e.key() == Qt.Key_ParenLeft:
            self.addBracket("(")
        elif e.key() == Qt.Key_ParenRight:
            self.addBracket(")")
        elif e.key() == Qt.Key_Escape:
            self.clearAll()
        
    def addDigit(self, digit): # Add digit to the display
        self.labelMain.setText(self.labelMain.text() + digit)

    def addDecimal(self): # Add decimal point to the display, only if the last character is a digit
        if(self.labelMain.text()[-1].isdigit()):
            self.labelMain.setText(self.labelMain.text() + ".")

    def addBracket(self, bracket): # Add a bracket to the display
        if(bracket == "("): # Add opening bracket only if the the previous bracket was closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")")):
                self.labelMain.setText(self.labelMain.text() + bracket)
        elif(bracket == ")"): # Add closing bracket if the previous bracket is open, not closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")") + 1):
                self.labelMain.setText(self.labelMain.text() + bracket)

    def addFunction(self, function): # Add a function to the display
        if(len(self.labelMain.text()) == 0 or ( self.labelMain.text()[-1].isdigit() or self.labelMain.text()[-1] == ")")): # If previous character is a digit or a closing bracket
            self.labelMain.setText(self.labelMain.text() + function)

    def deleteDigit(self): # Delete the last character
        self.labelMain.setText(self.labelMain.text()[:-1])

    def clearAll(self): # Clear everything
        self.labelSecond.setText("")
        self.labelMain.setText("")

    def finishCalculation(self): # Calculate the expression
        self.labelSecond.setText(self.labelMain.text()) # Copy the expression to the second display
        self.labelMain.setText(str(eval(self.labelMain.text()))) # Calculate the expression and display the result TODO send to our own math parse function

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
