from signal import signal
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from pip import main
from ui import Ui_mainWindow
import parsefunc

currentDirectory = os.path.dirname(os.path.realpath(__file__))

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'candycalc.1.0.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

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
        self.setupFonts()
        self.connectButtons()

    ## @brief Set the default font
    #
    # Add the custom font to font database
    # Set the font for every GUI element
    # Initialize the labels' text so the GUI resizes appropriately for text sizes
    def setupFonts(self):
        QFontDatabase.addApplicationFont(os.path.join(currentDirectory, "fonts/FiraCode-Bold.ttf"))
        QFontDatabase.addApplicationFont(os.path.join(currentDirectory, "fonts/FiraCode-Medium.ttf"))
        self.labelMain.setFont(QFont("Fira Code"))
        self.labelSecond.setFont(QFont("Fira Code"))
        self.pushButton0.setFont(QFont("Fira Code"))
        self.pushButton1.setFont(QFont("Fira Code"))
        self.pushButton2.setFont(QFont("Fira Code"))
        self.pushButton3.setFont(QFont("Fira Code"))
        self.pushButton4.setFont(QFont("Fira Code"))
        self.pushButton5.setFont(QFont("Fira Code"))
        self.pushButton6.setFont(QFont("Fira Code"))
        self.pushButton7.setFont(QFont("Fira Code"))
        self.pushButton8.setFont(QFont("Fira Code"))
        self.pushButton9.setFont(QFont("Fira Code"))
        self.pushButtonDec.setFont(QFont("Fira Code"))
        self.pushButtonLBrac.setFont(QFont("Fira Code"))
        self.pushButtonRBrac.setFont(QFont("Fira Code"))
        self.pushButtonLn.setFont(QFont("Fira Code"))
        self.pushButtonFact.setFont(QFont("Fira Code"))
        self.pushButtonRoot.setFont(QFont("Fira Code"))
        self.pushButtonExp.setFont(QFont("Fira Code"))
        self.pushButtonDiv.setFont(QFont("Fira Code"))
        self.pushButtonMul.setFont(QFont("Fira Code"))
        self.pushButtonMin.setFont(QFont("Fira Code"))
        self.pushButtonPlus.setFont(QFont("Fira Code"))
        self.pushButtonDel.setFont(QFont("Fira Code"))
        self.pushButtonCE.setFont(QFont("Fira Code"))
        self.pushButtonEq.setFont(QFont("Fira Code"))
        self.labelMain.setText("Initialize")
        self.labelSecond.setText("Initialize")
        self.labelMain.setText("")
        self.labelSecond.setText("")

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
        
        # Menu bar items
        self.menuFile.triggered.connect(sys.exit(app.exec_()))

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
        elif e.key() == Qt.Key_Equal or e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.finishCalculation()
        elif e.key() == Qt.Key_Escape:
            self.clearAll()

    ## @brief Check if display contains error and handle it
    #
    # If user tries to input something while an error is on the display, the display is cleared before the new input
    def handleError(self):
        if("error" in self.labelMain.text().lower() or "Num too big" in self.labelMain.text()):
            self.labelMain.setText("")

    ## @brief Add a digit to the display
    #
    # @param digit Digit to be added to the display
    def addDigit(self, digit): # Add digit to the display
        self.handleError()
        self.labelMain.setText(self.labelMain.text() + digit)

    ## @brief Add a decimal point to the display
    # 
    # A decimal point can only be added after a digit
    #
    # @todo Check if a decimal point is already present in the current number
    def addDecimal(self): # Add decimal point to the display, only if the last character is a digit
        self.handleError()
        if(len(self.labelMain.text()) == 0):
            self.labelMain.setText(".")
        elif(self.labelMain.text()[-1].isdigit()):
            self.labelMain.setText(self.labelMain.text() + ".")

    ## @brief Add a bracket to the display
    #
    # It's possible to only have one level of brackets, therefore if a bracket was opened, it must be closed
    # If user tries to open another bracket, the character is not added
    # Also, change the root function to the default value if closing a bracket
    #
    # @param bracket Bracket to be added (either "(" or ")")
    def addBracket(self, bracket): # Add a bracket to the display
        self.handleError()
        if(bracket == "("): # Add opening bracket only if the the previous bracket was closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")")):
                self.labelMain.setText(self.labelMain.text() + bracket)
        elif(bracket == ")"): # Add closing bracket if the previous bracket is open, not closed
            if(self.labelMain.text().count("(") == self.labelMain.text().count(")") + 1):
                self.labelMain.setText(self.labelMain.text() + bracket)
            self.pushButtonRoot.setText("√x")

    ## @brief Add a function character to the display
    #
    # If the function is root, change the text on the button to "n√x" to better indicate the function
    #
    # @todo Check if a function character is already present in the display and replace it (commented out code was trying to acomplish this), now handled by parser
    # @param function Function character to be added
    def addFunction(self, function):
        self.handleError()
        if(function != "√("):
            self.labelMain.setText(self.labelMain.text() + function)
        elif(function == "√("):
            if(self.pushButtonRoot.text() == "√x"):
                self.labelMain.setText(self.labelMain.text() + "√(")
                self.pushButtonRoot.setText("ⁿ√x")
            elif(self.pushButtonRoot.text() == "ⁿ√x"):
                self.labelMain.setText(self.labelMain.text() + ",")
                self.pushButtonRoot.setText("√x")
        # if(len(self.labelMain.text()) > 0 and ( self.labelMain.text()[-1] == "+" or self.labelMain.text()[-1] == "-" or self.labelMain.text()[-1] == "/" or self.labelMain.text()[-1] == "×" or self.labelMain.text()[-1] == "^")):
        #     self.deleteDigit()
        #     self.labelMain.setText(self.labelMain.text() + function)
        # elif(function != "√(" and ( len(self.labelMain.text()) == 0 or ( self.labelMain.text()[-1].isdigit() or self.labelMain.text()[-1] == ")"))): # If previous character is a digit or a closing bracket
        #     self.labelMain.setText(self.labelMain.text() + function)

    ## @brief Delete the last digit from the display
    #
    # If the deleted character was root, the root button is reset to its default value
    def deleteDigit(self):
        self.handleError()
        if(len(self.labelMain.text()) > 0):
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
        try:
            self.labelSecond.setText(parsefunc.get_parsed_input(self.labelMain.text())) # Copy the expression to the second display
            self.labelMain.setText(str(parsefunc.get_result(self.labelMain.text()))) # Calculate the expression and display the result TODO send to our own math parse function
        except ValueError:
            self.labelMain.setText("Error")
        except ZeroDivisionError:
            self.labelMain.setText("Math error")
        except OverflowError:
            self.labelMain.setText("Num too big")
        except SyntaxError:
            self.labelMain.setText("Syntax error")
        except:
            self.labelMain.setText("Error")


## @brief Main function
#
# Handle creating and closing the main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(currentDirectory, 'icon.ico')))
    window = mainWindow()
    sys.exit(app.exec_())
