def cat(args):
    """concatenate files and print on the standard output"""
    output = ""
    for i in args:
        file = open(i)
        for j in file:
            output += j
    print(output)
    pass


def tac(args):
    """concatenate and print files in reverse"""
    output = ""
    for i in range(len(args)):
        file = open(args[len(args) - 1 -i])
        for j in file:
            output += j
    tempOut = output.split("\n")
    for i in range(len(tempOut)):
        print(tempOut[len(tempOut) - i - 1])

    pass


