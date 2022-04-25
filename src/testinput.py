import parsefunc

import sys

for line in sys.stdin:
    print(parsefunc.solve_parentheses(line.rstrip()))