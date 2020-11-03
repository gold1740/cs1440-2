def wc(files):
    """print newline, word, and byte counts for each file"""
    lines = []
    words = []
    bytes = []

    for file in files:
        file = open(file)
        lines.append(len(file.readlines()))
        file.close()
    for file in files:
        file_words = 0
        file = open(file).readlines()
        for i in file:
            i = i.split()
            file_words += len(i)
        words.append(file_words)
    for file in files:
        file = open(file)
        bytes.append(len(file.read()))
        file.close()
    output = []
    for i in range(len(files)):
        print((str(lines[i]) + " " + str(words[i]) + " " + str(bytes[i]) + " " + str(files[i])))

