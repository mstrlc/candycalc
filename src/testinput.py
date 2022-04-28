import parsefunc #parsing function 
import sys
#for each line written to stdin
for line in sys.stdin:
    #prints parsed input as a list
    print(parsefunc.parse_input(line.rstrip()))
    print (parsefunc.get_parsed_input(line.rstrip()))
    #prints the result after solving the expression
    print(parsefunc.get_result(line.rstrip()))