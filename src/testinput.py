import parsefunc

import sys

for line in sys.stdin:
    print(parsefunc.balanced_parentheses(line.rstrip()))