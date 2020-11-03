def head(args):
    """output the first part of files"""
    lines = 10
    if args[0] == "-n":
        if len(args) < 2:
            print("you must enter a number of lines")
            exit(2)
        lines = int(args[1])
        args = args[2:]
    for i in args:
        file = open(i).readlines()
        for j in range(lines):
            print(file[j], end="")
    pass


def tail(args):
    """output the last part of files"""
    lines = 10
    if args[0] == "-n":
        if len(args) < 2:
            print("you must enter a number of lines")
            exit(2)
        lines = int(args[1])
        args = args[2:]
    for i in args:
        file = open(i).readlines()
        for j in range(lines):
            print(file[-j], end="")
    pass

