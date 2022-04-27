# -*- coding: utf-8 -*-

parentheses = ["(", ")"]
operators = ["ln", "!", "√", "^", "×", "/", "+", "-"]
precedence = [["(",")"],["ln"], ["!"], ["√" ,"^"], ["×", "/"], ["+", "-"]]

def solve_expr(expr):
    result=[]
    for operator_set in precedence:
        for i ,token in enumerate(expr):
            if token in operator_set:
                if token == '(':
                    close = expr.index(')')
                    result = solve_expr(expr[i+1:close])
                elif token == "+":
                    result = int(expr[i-1])+int(expr[i+1])
                elif token == "-":
                    result = int(expr[i-1])-int(expr[i+1])
    return(result)


def parse_input(input):
    str = input
    parsed = []
    add = ""
    flag=False
    for i, item in enumerate(str):
        if item.isdigit():
            add += item
            continue
        
        elif item == '.':
            if '.' in add:
                raise Exception("Input error")
            elif add == "":
                add += '0'
                add += item
            elif add != "":   
                add += item 
            else:
                raise Exception("Input error")

        elif item in operators:
            if add != "":
                parsed.append(add)
                add = ""
            parsed.append(item)

        elif str[i] == 'l' or flag==True:
            if add != "":
                parsed.append(add)
                add = ""
            if flag != True:
                flag = True
                continue
            if str[i] == 'n':
                parsed.append("ln")
                flag = False
            else:
                raise Exception("Input error")

        elif item in parentheses:
            if add != "":
                parsed.append(add)
                add = ""
            parsed.append(item)

        else:
            raise Exception("Input error")
        
    if add != "":
        parsed.append(add)
        add = ""
    return parsed

def get_result(input):
    return solve_expr(parse_input(input))

