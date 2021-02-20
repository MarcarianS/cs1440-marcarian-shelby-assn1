# args = a list of filenames (strings)
import Usage
def cat(args):

    """concatenate files and print on the standard output"""

    if len(args) == 0:
        Usage.usage("Too few arguments, please provide at least one file.", 'cat')
    for fileName in args:
        fileObj = open(fileName)
        for line in fileObj:
            print(line, end="")
        fileObj.close()

def tac(args):

    """concatenate and print files in reverse"""

    if len(args) == 0:
        Usage.usage("Too few arguments, please provide at least one file.", 'tac')
    else:
        for file in args:
            listToReverse = []
            fileObj = open(file)
            for line in fileObj:
                listToReverse.append(line)
            fileObj.close()
            listToReverse.reverse()
            for line in listToReverse:
                print(line, end="")

