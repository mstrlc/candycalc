# -*- coding: utf-8 -*-
import mathlib
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
    

    result=[]
    for operator_set in precedence:
        for i ,token in enumerate(expr):
            if token in operator_set:
                if token == '(':
                    close = expr.index(')')
                    result = solve_expr(expr[i+1:close])
                elif token == "+":
                    result = float(expr[i-1])+float(expr[i+1])
                elif token == "-":
                    result = float(expr[i-1])-float(expr[i+1])
    return(result)


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
                raise Exception("Input error")
            # '.' with no preceeding number
            # eg. "".5" -> "0.5"
            elif add == "":
                add += '0'
                add += item
            # '.' with preceeding number
            elif add != "":   
                add += item 
            else:
                raise Exception("Input error")

        # operator handling
        elif item in operators:
            # add preceeding number to parsed list
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
                parsed.append("ln")
            else:
                raise Exception("Input error")

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
            raise Exception("Input error")

    # add leftover number to parsed list    
    if add != "":
        parsed.append(add)
        add = ""
    # check the first item for operators
    if len(parsed):
        if parsed[0] in operators:
            raise Exception("Input error")
    return parsed
#end of parse_input func

#simple getr_result func 
def get_result(input):
    #call of input/expr parsing func
    return solve_expr(parse_input(input))

