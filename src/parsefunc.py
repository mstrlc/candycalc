# -*- coding: utf-8 -*-

operators = ["ln", "!", "√", "^", "×", "/", "+", "-"]
precedence = [["ln"], ["!"], ["√" ,"^"], ["×", "/"], ["+", "-"]]

def check_num(str):
    try:
        print(str)
    except:
        exit

def parse_input(input_str):
    for set in precedence:
        for index ,c in enumerate(input_str):
            if c == '(':
                solve_expr(input_str[index:input_str.find(')')])


def solve_expr(expr):
    exit



