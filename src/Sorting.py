def sort(args):
    """sort lines of text files"""
    lines = open(args).readlines()

    sortedList = lines[:1]
    unsortedList = lines[1:]

    for i in range(len(unsortedList)):
        success = False
        line = unsortedList.pop()
        for j in range(len(sortedList)):
            if line.lower() <= sortedList[j].lower():
                sortedList.insert(j, line)
                success = True
                break
        if not success:
            sortedList.append(line)
    for i in sortedList:
        print(sortedList)


def uniq(args):
    """report or omit repeated lines"""
    flag = ""
    if len(args) == 2:
        flag = args[0]
        args = args[1:]
    print(flag)
    orgList = sort(args[0])
    uniqList = [orgList[0]]
    redundantList = []
    for i in range(len(orgList)):
        uniqe = True
        for j in range(len(uniqList)):
            if orgList[i] == uniqList[j]:
                uniqe = False
                break

        if uniqe:
            uniqList.append(orgList[i])

    countedList = []
    for i in uniqList:
        count = 0
        for j in orgList:
            if i == j:
                count += 1
        if count > 1:
            for k in range(count):
                redundantList.append(i)
        countedList.append(str(count) + " " + i)

    if flag == "-D":
        printList = redundantList
    elif flag == "-c":
        printList = countedList
    else:
        printList = uniqList
    for i in printList:
        print(i)

    pass


