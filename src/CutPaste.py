import Usage
def cut(args):
    """remove sections from each line of files"""
    print("TODO: remove sections from each line of files")


def paste(args):

    def findLargestFile(listOfFiles):
        fileLength = 0
        maxLength = 0
        for fileObj in listOfFiles:
            for line in fileObj:
                fileLength += 1
            if fileLength > maxLength:
                maxLength = fileLength
        return maxLength

    def atEOF(fileObj):
        if fileObj.read() is None:
            return True
        else:
            return False
    """merge lines of files"""
    if len(args) == 0:
        Usage.usage("Please provide at least one file", "paste")
    else:
        listOfFiles = []
        for file in args:
            fileObj = open(file)
            listOfFiles.append(fileObj)
        # numberOfFiles = len(listOfFiles)
        for i in range(findLargestFile(listOfFiles) - 1):
            # currentFile = 0
            listToJoin = []
            for fileObj in listOfFiles:
                # currentFile += 1
                if atEOF(fileObj):
                    listToJoin.append("")
                else:
                    for position, line in enumerate(fileObj):
                        if position == i:
                            listToJoin.append(line)
            for fileObj in listOfFiles:
                fileObj.seek(0)
            print(",".join(listToJoin))
        for fileObj in listOfFiles:
            fileObj.close()