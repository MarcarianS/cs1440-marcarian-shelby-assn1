import Usage
def cut(args):
    """remove sections from each line of files"""
    print("TODO: remove sections from each line of files")


def paste(args):

    def findLargestFile(listOfFiles):

        maxLength = 0
        for fileObj in listOfFiles:
            fileLength = 0
            for line in fileObj:
                fileLength += 1
            if fileLength > maxLength:
                maxLength = fileLength
        return maxLength


    """merge lines of files"""
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