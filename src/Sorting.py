import Usage
def sort(args):
    """sort lines of text files"""
    if len(args) == 0:
        Usage.usage("Please provide at least one file", sort)
    else:
        listToSort = []
        for file in args:
            fileObj = open(file)
            for line in fileObj:
                listToSort.append(line)
            fileObj.close()
        listToSort.sort()
        for line in listToSort:
            print(line, end="")
