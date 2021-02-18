import Usage
def grep(args):
    """print lines that match patterns"""
    if len(args) == 0:
        Usage.usage("Too few arguments, please provide a pattern and a least one file.", 'grep')
    else:
        if args[0] == "-v":
            pattern = args[1]
            args.remove(args[0])
            args.remove(args[0])
            if len(args) == 0:
                Usage.usage("Too few arguments, argument -v requires a pattern and at least one file.", 'grep')
            else:
                for file in args:
                    fileObj = open(file)
                    for line in fileObj:
                        if pattern not in line:
                            print(line, end="")
                    fileObj.close()

        else:
            pattern = args[0]
            args.remove(args[0])
            if len(args) == 0:
                Usage.usage("Too few arguments, please provide a pattern and at least one file.", 'grep')
            else:
                for file in args:
                    fileObj = open(file)
                    for line in fileObj:
                        if pattern in line:
                            print(line, end="")
                    fileObj.close()
