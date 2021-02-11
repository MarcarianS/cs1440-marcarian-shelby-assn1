# args = a list of filenames (strings)
def cat(args):
    """concatenate files and print on the standard output"""
    for fileName in args:
        #open the file
        fileObj = open(fileName)
        #read the contents. dont use readline bc it takes up more memory
        for line in fileObj:
            print(line, end=" ")
        #print it out
        #close the file
        fileObj.close()
    #read what's in the files and print it out


def tac(args):
    """concatenate and print files in reverse"""
    print("TODO: concatenate and print files in reverse")
