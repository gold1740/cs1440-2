def grep(args):
    """print lines of files matching a pattern"""
    condition = True
    if args[0] == "-v":
        condition = False
        args = args[1:]
    string = args[0]
    args = args[1:]
    files = []
    for i in args:
        files.append(open(i).readlines())
    for i in files:
        for j in i:
            if string in j:
                if condition:
                    print(j, end="")
            else:
                if not condition:
                    print(j, end="")
    pass


