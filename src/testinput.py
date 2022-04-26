import parsefunc

import sys

for line in sys.stdin:
    #print(parsefunc.parse_input(line.rstrip()))
    print(parsefunc.get_result(line.rstrip()))