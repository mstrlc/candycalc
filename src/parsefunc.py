# -*- coding: utf-8 -*-
from yaml import parse
import mathlib
import sys

#sys.tracebacklimit=0
parentheses = ["(", ")"] #supported parentheses
operators = ["ln", "!", "√", "^", "×", "/", "+", "-"] #supported operators
precedence = [["(",")"],["ln"], ["!"], ["√" ,"^"], ["×", "/"], ["+", "-"]] #set precendence of operatos

##
# @package parsefunc
# parsefunc is a function input parsing function for Candycalc
#
# To use this module either use:
# parse_input(input) for parsing input to expression
# solve_expr(expr) to solve the expression
# get_result(input) to get a result of 2 functions above
#

#TODO: after merge adjust the funcion for mathlib operations

def solve_expr(expr):
    if len(expr) == 1:
        return expr[0]
    if len(expr) == 0:
        return 0

    for op_set in precedence:
        index = 0
        
        while len(expr) > index:
            token = expr[index]
            if token in op_set:

                if token in '(':
                    
                    help = []
                    if expr[index+1] in "+-":
                        help.append(0)

                    help += expr[index+1:expr.index(')')]
                    print(help)
                    if len(help) == 0:
                        return 0
                    if index != 0 and expr[index-1]=="√":
                        index+=1
                    elif len(help) != 0:
                        expr[index] = solve_expr(help)
                        del expr[index+1:expr.index(')')+1]

                if token in operators:

                    if token == "ln":
                        expr[index] = mathlib.ln(float(expr[index+1]))
                        del expr[index+1]

                    elif token == "!":
                        expr[index] = mathlib.factorial(int(expr[index-1]))
                        del expr[index-1]
                        print(expr)

                    elif token == "√":
                        print("haha")
                        if ',' in expr[index+1:expr.index(')')]:
                            print(expr[index+2])
                            expr[index] = mathlib.nroot(float(expr[index+2]), int(expr[index+4]))
                        else:
                            expr[index] = mathlib.nroot(float(expr[index+2]),2)
                        del expr[index+1:expr.index(')')+1]

                    elif token == "^":
                        expr[index] = mathlib.power(float(expr[index-1]),int(expr[index+1]))
                        del expr[index+1]
                        del expr[index-1]

                    elif token == "×":
                        expr[index] = mathlib.multiply(float(expr[index-1]),float(expr[index+1]))
                        del expr[index+1]
                        del expr[index-1]
                    
                    elif token == "/":
                        expr[index] = mathlib.divide(float(expr[index-1]),float(expr[index+1]))
                        del expr[index+1]
                        del expr[index-1]

                    elif token == "+":
                        expr[index] = mathlib.add(float(expr[index-1]),float(expr[index+1]))
                        del expr[index+1]
                        del expr[index-1]

                    elif token == "-":
                        expr[index] = mathlib.subtract(float(expr[index-1]),float(expr[index+1]))
                        del expr[index+1]
                        del expr[index-1]

            index+=1
    return solve_expr(expr)

def parse_input(input):
    '''
    Parses input into string list

    args:
    ----------  
    string : input
        input string

    returns [string]
        parsed 
    '''

    str = input     # input string
    parsed = []     # already parsed string
    add = ""        # parsing long numbers or with '.'
    flag=False      # detection of "ln"
    
    # string parsing loop
    for i, item in enumerate(str):

        # digit handling 
        if item.isdigit(): 
            add += item
            continue

        # decimal point handling
        elif item == '.':

            # only one '.' per number
            if '.' in add:
                raise SyntaxError()
            # '.' with no preceeding number
            # eg. "".5" -> "0.5"
            elif add == "":
                add += '0'
                add += item
            # '.' with preceeding number
            elif add != "":   
                add += item 
            else:
                raise SyntaxError()

        elif item == ',':
            if add != "":
                parsed.append(add)
                add=""
            parsed.append(item)

        # operator handling
        elif item in operators:
            # add preceeding number to parsed list
            if i!= 0 and add=="":
                if parsed[-1] not in '(!':
                    raise SyntaxError()
            if add != "":
                parsed.append(add)
                add = ""
            parsed.append(item)

        # ln handling
        elif str[i] == 'l' or flag==True:
            # add preceeding number to parsed list
            if add != "":
                parsed.append(add)
                add = ""
            # set the "ln" flag, find of 'l'
            if flag != True:
                flag = True
                continue
            # reseting flag, confirmation of 'n' after
            if str[i] == 'n':
                flag = False
                if parsed[len(parsed)-1].isnumeric():
                    parsed.insert(i,'×')
                parsed.append("ln")
            else:
                raise SyntaxError()

        #parentheses handling
        elif item in parentheses:
            # add preceeding number to parsed list
            if add != "" and item == '(':
                parsed.append(add)
                add = ""
                parsed.append('×')
            elif add != "":
                parsed.append(add)
                add = ""
            parsed.append(item)
        else:
            raise SyntaxError()

    # add leftover number to parsed list    
    if add != "":
        parsed.append(add)
        add = ""
    # check the first item for operators
    if len(parsed):
        if parsed[0] in operators:
            if parsed[0] in "-+":
                parsed.insert(0,"0")
            elif parsed[0] in "√ln":
                if len(parsed) <= 1: 
                    raise SyntaxError()
            else:
                raise SyntaxError()
        if parsed[len(parsed)-1] in operators:
            if parsed[len(parsed)-1] != '!':
                raise SyntaxError()

    open = 0
    close = 0            
    for i, check in enumerate(parsed):
        if check == '(':
            open+=1
        elif check == ')':
            close+=1
        elif check == '!':
            if i!=len(parsed)-1:
                if parsed[i-1].isnumeric() and parsed[i+1].isnumeric():
                    parsed.insert(i+1,'×')
    for i in range(open-close):
        parsed.append(')')
    return parsed
#end of parse_input func


def get_parsed_input(input):
    parsed=parse_input(input)
    string=""
    for i, item in enumerate(parsed):
        if item.isnumeric() and item != '0':
            parsed.insert(i,round(int(item)))
            del parsed[i+1]
        elif item == '(':
            if parsed[i+1] == ')':
                print(parsed[i+1])
                parsed.insert(i,int('0'))
                break
    for item in parsed:
        string+=str(item)
    return string

#simple getr_result func 
def get_result(input):
    #call of input/expr parsing func    
    result = float(solve_expr(parse_input(input)))

    lenght = len(str(int(result)))
    if lenght > 11:
        raise OverflowError()

    if result % 1 == 0:
        return int(result)
    else:
        return round(result, 12-lenght)
