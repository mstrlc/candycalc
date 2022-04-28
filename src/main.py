from signal import signal
import string
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from pip import main
from ui import Ui_mainWindow
import parsefunc

## @package candyCalc
#  @brief   Main GUI window of the application
class mainWindow(QMainWindow, Ui_mainWindow):

    ## @brief   Main window constructor
    #
    # Create the main window and show it, then connect the signals
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.connectButtons()

    ## @brief Connects the GUI buttons to function calls
    # 
    # Call the correct method for each button pressed
    def connectButtons(self):
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

    ## @brief Handle the keyboard input and connect it to the GUI buttons
    # 
    # Call the correct method for each key pressed
    def keyPressEvent(self, e):
        # Digit buttons
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

        # Decimal point button
        elif e.key() == Qt.Key_Period or e.key() == Qt.Key_Comma:
            self.addDecimal()
        
        # Bracket buttons
        elif e.key() == Qt.Key_ParenLeft:
            self.addBracket("(")
        elif e.key() == Qt.Key_ParenRight:
            self.addBracket(")")

        # Function buttons
        elif e.key() == Qt.Key_L:
            self.addFunction("ln(")
        elif e.key() == Qt.Key_Exclam:
            self.addFunction("!")
        elif e.key() == Qt.Key_R:
            self.addFunction("√(")
        elif e.key() == Qt.Key_AsciiCircum:
            self.addFunction("^")
        elif e.key() == Qt.Key_Slash:
            self.addFunction("/")
        elif e.key() == Qt.Key_Asterisk or e.key() == Qt.Key_X:
            self.addFunction("×")
        elif e.key() == Qt.Key_Minus:
            self.addFunction("-")
        elif e.key() == Qt.Key_Plus:
            self.addFunction("+")

        # Other buttons
        elif e.key() == Qt.Key_Backspace or e.key() == Qt.Key_Delete:
            self.deleteDigit()
        elif e.key() == Qt.Key_Equal or e.key() == Qt.Key_Enter:
            self.finishCalculation()
        elif e.key() == Qt.Key_Escape:
            self.clearAll()
    
    ## @brief Add a digit to the display
    #
    # @param digit Digit to be added to the display
    def addDigit(self, digit): # Add digit to the display
        self.labelMain.setText(self.labelMain.text() + digit)

    ## @brief Add a decimal point to the display
    # 
    # A decimal point can only be added after a digit
    #
    # @todo Check if a decimal point is already present in the current number
    def addDecimal(self): # Add decimal point to the display, only if the last character is a digit
        if(self.labelMain.text()[-1].isdigit()):
            self.labelMain.setText(self.labelMain.text() + ".")

    ## @brief Add a bracket to the display
    #
    # It's possible to only have one level of brackets, therefore if a bracket was opened, it must be closed
    # If user tries to open another bracket, the character is not added
    # Also, change the root function to the default value if closing a bracket
    #
    # @param bracket Bracket to be added (either "(" or ")")
    def addBracket(self, bracket): # Add a bracket to the display
        if(bracket == "("): # Add opening bracket only if the the previous bracket was closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")")):
                self.labelMain.setText(self.labelMain.text() + bracket)
        elif(bracket == ")"): # Add closing bracket if the previous bracket is open, not closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")") + 1):
                self.labelMain.setText(self.labelMain.text() + bracket)
            self.pushButtonRoot.setText("√x")

    ## @brief Add a function character to the display
    #
    # If the last entered character was also a fucntion character, replace it with the currently pressed one, so there can't be two function characters in a row
    # If the function is root, change the text on the button to "n√x" to better indicate the function
    #
    # @param function Function character to be added
    def addFunction(self, function):
        if(len(self.labelMain.text()) > 0 and ( self.labelMain.text()[-1] == "+" or self.labelMain.text()[-1] == "-" or self.labelMain.text()[-1] == "/" or self.labelMain.text()[-1] == "×" or self.labelMain.text()[-1] == "^")):
            self.deleteDigit()
            self.labelMain.setText(self.labelMain.text() + function)
        if(function != "√(" and ( len(self.labelMain.text()) == 0 or ( self.labelMain.text()[-1].isdigit() or self.labelMain.text()[-1] == ")"))): # If previous character is a digit or a closing bracket
            self.labelMain.setText(self.labelMain.text() + function)
        elif(function == "√("):
            if(self.pushButtonRoot.text() == "√x"):
                self.labelMain.setText(self.labelMain.text() + "√(")
                self.pushButtonRoot.setText("ⁿ√x")
            elif(self.pushButtonRoot.text() == "ⁿ√x"):
                self.labelMain.setText(self.labelMain.text() + ",")
                self.pushButtonRoot.setText("√x")

    ## @brief Delete the last digit from the display
    #
    # If the deleted character was root, the root button is reset to its default value
    def deleteDigit(self):
        if(self.labelMain.text()[-1] == "√"):
            self.pushButtonRoot.setText("√x")
        self.labelMain.setText(self.labelMain.text()[:-1])

    ## @brief Clear the display
    #
    # Remove all text from main and secondary labels
    # Set the root button text to the default
    def clearAll(self):
        self.pushButtonRoot.setText("√x")
        self.labelSecond.setText("")
        self.labelMain.setText("")

    ## @brief Finish the calculation
    #
    # Calculate the result using our parse function and math library
    # Set the result to be the text of main label
    # Set the calculation to be the text of the secondary label
    def finishCalculation(self): # Calculate the expression
        self.labelSecond.setText(self.labelMain.text()) # Copy the expression to the second display
        self.labelMain.setText(str(parsefunc.get_result(self.labelMain.text()))) # Calculate the expression and display the result TODO send to our own math parse function

## @brief Main function
#
# Handle creating and closing the main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
