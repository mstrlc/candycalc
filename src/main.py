import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_mainWindow

class mainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons to functions

        # Digit buttons
        self.pushButton0.clicked.connect(self.addDigit)
        self.pushButton1.clicked.connect(self.addDigit)
        self.pushButton2.clicked.connect(self.addDigit)
        self.pushButton3.clicked.connect(self.addDigit)
        self.pushButton4.clicked.connect(self.addDigit)
        self.pushButton5.clicked.connect(self.addDigit)
        self.pushButton6.clicked.connect(self.addDigit)
        self.pushButton7.clicked.connect(self.addDigit)
        self.pushButton8.clicked.connect(self.addDigit)
        self.pushButton9.clicked.connect(self.addDigit)

        # Decimal point button
        self.pushButtonDec.clicked.connect(self.addDecimal)

        # Bracket buttons
        self.pushButtonLBrac.clicked.connect(self.addBracket)
        self.pushButtonRBrac.clicked.connect(self.addBracket)

        # Function buttons
        self.pushButtonLn.clicked.connect(self.addFunction)
        self.pushButtonFact.clicked.connect(self.addFunction)
        self.pushButtonRoot.clicked.connect(self.addFunction)
        self.pushButtonExp.clicked.connect(self.addFunction)
        self.pushButtonDiv.clicked.connect(self.addFunction)
        self.pushButtonMul.clicked.connect(self.addFunction)
        self.pushButtonMin.clicked.connect(self.addFunction)
        self.pushButtonPlus.clicked.connect(self.addFunction)

        # Other buttons
        self.pushButtonDel.clicked.connect(self.deleteDigit)
        self.pushButtonCE.clicked.connect(self.clearAll)
        self.pushButtonEq.clicked.connect(self.finishCalculation)

    def addDigit(self): # Add digit to the display
        self.labelMain.setText(self.labelMain.text() + self.sender().text())

    def addDecimal(self): # Add decimal point to the display, only if the last character is a digit
        if(self.labelMain.text()[-1].isdigit()):
            self.labelMain.setText(self.labelMain.text() + ".")

    def addBracket(self): # Add a bracket to the display
        if(self.sender().text() == "("): # Add opening bracket only if the the previous bracket was closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")")):
                self.labelMain.setText(self.labelMain.text() + self.sender().text())
        elif(self.sender().text() == ")"): # Add closing bracket if the previous bracket is open, not closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")") + 1):
                self.labelMain.setText(self.labelMain.text() + self.sender().text())

    def addFunction(self): # Add a function to the display
        if(self.labelMain.text()[-1].isdigit() or self.labelMain.text()[-1] == ")"): # If previous character is a digit or a closing bracket
            self.labelMain.setText(self.labelMain.text() + self.sender().text())

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
