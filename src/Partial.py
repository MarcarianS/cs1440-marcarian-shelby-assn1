import Usage


def head(args):

    """output the first part of files"""

    def oneFileHead(args, numberOfLines):
        for file in args:
            lineCount = 0
            fileObj = open(file)
            for line in fileObj:
                lineCount += 1
                print(line, end="")
                if lineCount == numberOfLines:
                    break
            fileObj.close()

    def severalFilesHead(args, numberOfLines):
        for file in args:
            lineCount = 0
            print(f"=====> {file} <=====")
            fileObj = open(file)
            for line in fileObj:
                lineCount += 1
                print(line, end="")
                if lineCount == numberOfLines:
                    break
            fileObj.close()

    if len(args) == 0:
        Usage.usage("Too few arguments, please provide at least one file.", 'head')

    else:
        # Check for flag if args has something in it
        if args[0] == "-n":
            if len(args) == 1:
                Usage.usage("Number of lines is required with argument -n", "head")
            else:
                if args[1].isnumeric():
                    numberOfLines = int(args[1])
                    args.remove(args[0])
                    args.remove(args[0])
                    if len(args) == 0:
                        Usage.usage("Too few arguments, please provide at least one file.", 'head')
                    elif len(args) == 1:
                        oneFileHead(args, numberOfLines)
                    elif len(args) > 1:
                        severalFilesHead(args, numberOfLines)
                else:
                    Usage.usage("Number of lines is required with argument -n", "head")
        # If removing -n and the number took all files out, report error
        else:
            if len(args) == 1:
                numberOfLines = 10
                oneFileHead(args, numberOfLines)
            elif len(args) > 1:
                numberOfLines = 10
                severalFilesHead(args, numberOfLines)





def tail(args):

    """output the last part of files"""

    def oneFileTail(args, numberOfLines):
        for file in args:
            fileObj = open(file)
            fileLength = 1
            for line in fileObj:
                fileLength += 1
            startingLine = fileLength - numberOfLines
            currentLine = 0
            fileObj.seek(0)
            for line in fileObj:
                currentLine += 1
                if currentLine >= startingLine:
                    print(line, end="")
            fileObj.close()

    def severalFilesTail(args, numberOfLines):
        for file in args:
            print(f"=====> {file} <=====")
            fileObj = open(file)
            fileLength = 1
            for line in fileObj:
                fileLength += 1
            startingLine = fileLength - numberOfLines
            currentLine = 0
            fileObj.seek(0)
            for line in fileObj:
                currentLine += 1
                if currentLine >= startingLine:
                    print(line, end="")
            fileObj.close()

    if len(args) == 0:
        Usage.usage("Too few arguments, please provide at least one file.", 'tail')

    else:
        # Check for flag if args has something in it
        if args[0] == "-n":
            if len(args) == 1:
                Usage.usage("Number of lines is required with argument -n", 'tail')
            else:
                if args[1].isnumeric():
                    numberOfLines = int(args[1])
                    args.remove(args[0])
                    args.remove(args[0])
                    if len(args) == 0:
                        Usage.usage("Too few arguments, please provide at least one file.", 'tail')
                    elif len(args) == 1:
                        oneFileTail(args, numberOfLines)
                    elif len(args) > 1:
                        severalFilesTail(args, numberOfLines)
                else:
                    Usage.usage("Number of lines is required with argument -n", "tail")
        # If removing -n and the number took all files out, report error
        else:
            if len(args) == 1:
                numberOfLines = 10
                oneFileTail(args, numberOfLines)
            elif len(args) > 1:
                numberOfLines = 10
                severalFilesTail(args, numberOfLines)
