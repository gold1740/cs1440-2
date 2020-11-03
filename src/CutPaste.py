from Concatenate import cat


def cut(args):
    if len(args < 2):
        column = 1
    else:
        column = args[1]

    csv = open(args[0])
    while True:
        line = [csv.readline()]
        if line == "":
            break
        else:
            print(line[column])
    pass


def paste(args):
    if len(args) == 1:
        cat(args)
        exit()

    files = []
    for i in args:
        file = open(i)
        files.append(file.readlines())
    max_length = 0
    for i in files:
        if len(i) > max_length:
            max_length = len(i)
    for i in range(max_length):
        line = ""
        for k in range(len(files)):
            if k < len(files):
                line += files[k][i]
                line = line[:-1]
            line += ","
        if line == ".":
            break
        line = line[:-1]
        print(line)
    pass



