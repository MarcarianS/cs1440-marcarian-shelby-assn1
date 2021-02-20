import Usage
def cut(args):

    """remove sections from each line of files"""

    if len(args) == 0:
        Usage.usage("Please provide at least one file", "cut")
    elif args[0] == "-f":
        if len(args) < 2:
            Usage.usage("A comma separated field specification and file are required.", "cut")
        else:
            #Initialize lists and remove flags from args so you're left with only files
            args.remove(args[0])
            stringOfFlags = args[0]
            args.remove(args[0])
            listOfFlags = (stringOfFlags.split(","))
            flagsAsInts = []
            numberOfFlags = len(listOfFlags)
            for j in range(numberOfFlags):
                flagsAsInts.append(int(listOfFlags[j]))
            flagsAsInts.sort()
            flagsToRemove = 0
            for k in flagsAsInts:
                if k < 1:
                    flagsToRemove += 1
            for m in range(flagsToRemove):
                flagsAsInts.remove(flagsAsInts[0])

            numberOfPosFlags = len(flagsAsInts)

            if len(flagsAsInts) == 0:
                Usage.usage("A comma separated field specification and file are required", "cut")
            else:
                for file in args:
                    fileObj = open(file)

                    for line in fileObj:
                        listOfWords = line.split(",")
                        listToJoin = []
                        for i in range(numberOfPosFlags):
                            indexToPrint = flagsAsInts[i]
                            if len(listOfWords) < indexToPrint - 1:
                                listToJoin.append("")
                            else:
                                listToJoin.append((listOfWords[indexToPrint - 1]).strip())
                        joinedList = ",".join(listToJoin)
                        print(joinedList)
                    fileObj.close()
    else: #if no flag present
        for file in args:
            fileObj = open(file)
            for line in fileObj:
                listOfWords = line.split(",")
                print(listOfWords[0])
            fileObj.close()


def paste(args):

    """merge lines of files"""

    def findLargestFile(listOfFiles):

        maxLength = 0
        for fileObj in listOfFiles:
            fileLength = 0
            for line in fileObj:
                fileLength += 1
            if fileLength > maxLength:
                maxLength = fileLength
        return maxLength


    if len(args) == 0:
        Usage.usage("Please provide at least one file", "paste")
    else:
        listOfFiles = []
        numberOfFiles = 0
        for file in args:
            numberOfFiles += 1
            fileObj = open(file)
            listOfFiles.append(fileObj)
        maxFileLength = findLargestFile(listOfFiles)
        for fileObj in listOfFiles:
            fileObj.seek(0)
        for i in range(maxFileLength):
            listToJoin = []
            for fileObj in listOfFiles:
                listToJoin.append((fileObj.readline()).strip())

            print(",".join(listToJoin))
        for fileObj in listOfFiles:
            fileObj.close()