import itertools
import stack    # For stack development ()

# Requirement for system to run [Do not change] -------------[3 line]---
def readInfix(filename):
    with open(filename) as f:
        Infix = f.readlines()
    return Infix[0]

# These 2 function for change in order the program to run as requirement ():

def priority (char):
        # Tell the program the priority
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1 # <--- If the operand hit nothing

def isOperand (char):
    return (ord(char) >= ord('A') and ord(char) <= ord('Z') or ord(char) >= ('a'))

def infix_to_postfix(Infix):
    # Same variable for future change
    Postfix=Infix

    stack = []
    # Loop condition: No more comment (Revision)
    for c in Infix:
        if isOperand (char):
            

    return Postfix


def postfix_to_truthtable(Postfix):

    truthtable=Postfix
    return truthtable

def writeTruthtable(table): # End student part
    import sys
    outfile=sys.argv[0]
    outfile=outfile[0:-2]
    outfile+="txt"
    with open(outfile, 'w') as f:
        for lines in table:
            for item in lines:
                f.write("%s\t" % item)
            f.write("\n")
    f.close()


def main():

    Infix=readInfix("logicexpression.txt")
    Postfix=infix_to_postfix(Infix)
    Truthtable=postfix_to_truthtable(Postfix)
    writeTruthtable(truthtable)
    
main()