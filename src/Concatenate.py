# args = a list of filenames (strings)
import Usage
def cat(args):
    """concatenate files and print on the standard output"""
    if len(args) == 0:
        Usage.usage("Too few arguments, please provide at least one file.", 'cat')
    for fileName in args:
        #open the file
        fileObj = open(fileName)
        #read the contents. dont use readline bc it takes up more memory
        for line in fileObj:
            print(line, end="")
        #print it out
        #close the file
        fileObj.close()
    #read what's in the files and print it out


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

