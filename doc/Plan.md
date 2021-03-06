# 0.  From Problem Analysis to Data Definitions

This program will accept 0 or one option and 1 or more files.
Input is taken by the program as a list of strings.
If no files are given, a usage menu will be displayed
cat() will print the file to the user
tac() will print the file with lines reversed to the user
cut() removes sections of lines from files
paste() merges lines from files
grep() Prints lines of files matching a pattern
head()output the first part of files
tail()output the last part of files
sort() Sort lines of text files
wc() print newline, word, and byte counts for each file

# 1.  System Analysis

Menu:
-There is no menu, options and file paths are given as arguments of the program when it is calles (python src/tt.py TOOL [OPTIONS] FILENAMES...
-If too few arguments are given to the program (no src/tt.py or filename) a usage menu will print

tt.py()
-will import all the text tool classes
-ignore the 0th index of the list sys.argv. First index should be TOOL. If it begins with "-", call usage.
-Use if to determine which TOOL was called. If it doesn't match any of them, call usage().
-Call the appropriate tool, strip off the 0th and 1st entries and send the rest to the tool as arguments

#cat()
*Input
-Comes to this function as a list of strings representing paths to a file. 
-If the string begins with "-", assumes it was given an option and ignore this argument.
	Examples:
		data/msg1.txt
		-a
		src/tt.py
**Internal Data:
-Import Usage()
-For file in args, check if the string begins with "-"
-if it does, ignore it and move on to the next.
-Open the file. If the file doesn't exist, let it crash on its own.
-for line in file, print the line without the automatic newline.
-Close the file
-If the only arguments given are OPTIONS, tell the user they can only give cat() files and call usage()

**Output:
-Print files out to user
-Return nothing

**Function Stub:
def cat(args)
	import usage()
	for file in args
		if file startswith(-)
			continue
		else
			open file
			for line in file
				print line end=""
			close file

#wc()
**Input:
-Takes a list of strings of file names. no OPTIONS
	Examples:
		data/num2 data/words200
		-n (ignored)
		let3
		msg.txt

**internal Data:
-If OPTION is given, ignore it
-if too few (0) arguments given, call usage("Not enough ergs", wc)
-Open the files one at a time. For line in file, append line to lineList
-lineCount = lineList length
-for line in linelist, charCount += length linelist[line] 
-count(" ") (still in for loop above), add one to get wordCount for that line. 
-I want a list of lines. (sep on newline), then a list of words (sep on whitespace), then list of bytes
-print lineCount, wordCount, charCount and fileName
-add each number to it's own list so you can use it outside the loop
-if args list length is 1, done
-else, sum each list of counts, print out and print total instead of fileName.
-close file

**Output:
-prints number of lines, words, and characters with which file it is describing.
-Prints totals if there are more than one files.
-Make sure all columns are formatted in some consistent way.

**Function stub:
def wc(args)
		if args lenght = 0
	for filename in args
		usage("need at least one file", wc)
		else for file in args open file
			for line in fileObj,
				linecount+= 1
				charcount += length of line
				wordCount += count(",") +1
		print lineCount, wordCount, charCount, fileName
		append values to linecountlist, wordcountlist, charcount list
		close file
	if argslwngth = 1
		return
	else sum values in countlists, print lineTotal, etc, Total

#head() 
**Input:
-List of one optional argument to determine number of lines to print and file paths as strings
	Examles:
		-n data/names10
		data/let3
		-n data/numbers data/names
		-n

**Internal Data:
-Check for length changer
-Set variable to convert length changer to an integer and remove it from the list of args
-If no length changer is given, set it to 10
-for file in args open the file
-for line in fileObj append line to lineList
-if one file was given, proceed like normal
-If multiple files given, preceed contents with name of file
-if lineList length is <= length changer copy code from cat (don't call cat, file would try to open again)
-If there was a length changer, print line from fileObj in range(length changer)
-close file

**Output:
-first lines of the given file(s) printed.

**Function Stub:
head(args)	
	If args[0] == -n
		numberOfLines = int(args[1])
		remove args[0,1]
	elif args[0] !startswith("-")
		 numberOfLines = 10
	else usage("Not a valid argument to head, head)
	if given one file
	for file in args open file
		for line in fileObj append line to lineList
		find lineList length
		if length <= number of lines, reuse code from cat
		else 
		for i in range length, print lineList[i]
		close file
	if given multiple files
	for file in args open file
                for line in fileObj append line to lineList
                print file name banner
		find lineList length
                if length <= number of lines, reuse code from c>
                else
                for i in range length, print lineList[i]
                close file

 
#grep
**Input: Takes a pattern and file paths as strings, optionally takes -v to invert the pattern.

**Internal Data:
-Look for -v, if it's not there then index 0 is the pattern
-Remove index 0 from args
-for file in args, open file
-for line in fileObj, if pattern is in line, print line. Else continue
-close file
-if it is there, index 1 is the pattern
-remove index 0 and 1 from args
-for file in args, open file
-for line in fileObj, if patter is not in line, print line
-close file

**Output:
-string of the lines containing the pattern key
-If argument -v is present, string of lines not containing the pattern key

**Function Stub:
def grep(args)
	if args length = 0 or length = 1
		usage("Please provde a pattern and at least one file, grep)
	if args[0] == -v
		pattern = (str)args[1]
		remove args[0,1] from args
		for file in args open file
			if pattern !in line, print(line)
			close file
	if args [0] != -v
		pattern = string args[0]
		remove args index 0
		for file in args
			for line in fileObj
			if pattern in line, print line
			close file
#tail

**Input: 
-Takes a list of file names and optional -n to define number of lines printed.

**Internal Data:
-Check for -n, if it's there numberLines = -n, remove args[0]
-if args length = 0, call usage()
-If n not present, number lines = 10
-for file in args, open file
-for i in range(length of fileObj - numberLines, length of fO) 
-with i = (length of fileObj - numberLines)
-find the index of fileObj that is -n away from the end and print from there
-close file

**Output:
-The last lines of a file, with a header if there are multiple files given.

**Function Stub:
def tail(args)
	if args[0] startswith "-"
		numberOfLines = args[1]
		remove args[0] and args[1]
	else numberOfLines = 10
	for file in args
		open file
		fileLength = 0
		for line in fileObj fileLengh += 1
		fileLength - numberOfLines = startingLine
		currentLine = 0
		for line in fileObj
			currentLine += 1
			if current line is >= startingLine, print line
		close file
#sort
**Input:
-list of files

**Internal Data:
-open files, put contents into list and close file
-take list of lines and use list.sort() to sort all files together
-for i in list, print i

**Output:
-All contents from all files given, sorted with each other. 

**Function Stub:
def sort(args)
	if len.args == 0, call usage(not enough arguments)
	for file in args, open file
		for line in file, append line to listToSort
		close file
	listToSort.sort()
	for line in listToSort
		print line
#tac
**Input:
-list of files

**Internal Data:
-If no files are given, call usage
-for file in args, open file
-append each line into a blank list
-reverse the file with array.reverse()
-for line in list, print the line
-close file

**Output:
-reversed contents of file, printed line by line.

**Function Stub:
def tac(args)
	if args length is 0, call usage
	for file in args, open file
		for line in fileObj, append to list
		list.reverse()
		for line in list, print line
		close file

#paste
**Input:
-list of files

**Internal Data:
-If no files given, call usage for too few args
-for file in args open file
-append fileObj into list
-for obj in list, print first line with comma instead of a newline
-for fileObj in list, close file

**Ouput:
-line i of each file printed together on same line

**Function Stub:
def findLargestFile(listOfFiles)
	fileLength = 0
	maxLength = 0
	for fileObj in list of files
		for line in file
			fileLength += 1
		if fileLength > maxLength
			maxLength = fileLength
	return maxLength

def atEOF(fileObj): 
	if fileObj.read() = None:
		return true
	else
		return false
def paste(args)
	if args length = 0, call usage(too few arguments)
	else
		for file in args open file
		append open file to listOfFIles
		numberOfFiles = len(listOfFiles)
		for i in range(findLargestFile(listOFFiles)
			currentFile = 0
		for fileObj in listOfFIles
			listToJoin = []
			currentFile += 1
			if atEOF(fileObj)
				ListToJoin.append("")
			else:
				for position, line in enumerate(fileObj):
					if position == currentLine
					listToJoin.append(line)
			listToJoin.join(",")
			print(listToJoin, \n)	
		for fileObj in listOfFiles
			fileObj.close()				 
#cut
**Input:
-list of files

**Internal data:
-check for and remove flag if present
-open the files one at a time
-read the lines one at time
-use .split() to make each line a list of strings
-print entry 1 (default) of the list
-if one flag is present, print that entry of the list
-if multiple flags are present, split them on the comma
-for length of flagList
-print line entry corresponding to flag

**Output:
-specified entry from each line of a file

**Function Stub:
def cut(args)
	if len(args) == 0 usage(toofew  arguments)
	elif args[0] == -f
		listofflags = []
		remove -f
		args[0] = string of flags
		args[0].remove
		listof flags = ",".split(stringofflags)
		for file in args
			open file
				for line in fileObj
					",".split(line) = listofWords
					listToJoin = []
					for i in range(len(listofflags))
						find min of flags
						remove min of flags
						if len(list of words) < minOfFlag - 1
							listtojoin.append("")
						else
							listtoJoin.append(listOfWords[minOfFlag - 1]
					join listtoJoin and print
	else
		for file in args open file
			for line in fileObj
				split on the comma into list of words
				print(listofwords[0]
	
# 2.  Functional Examples
def head()	
	If args[0] == -n 
		if args[1].isnumeric()
                	numberOfLines = int(args[1])
                	remove args[0,1]
		else: 
			usage(number of lines is required with -n)
        elif len(args) == 0
		usage(too few argumentsm, please provide at least one file)
	else 
                 numberOfLines = 10
        if args.len == 1
        for file in args open file
		lineCount = 0
                for line in fileObj 
			lineCount += 1
			print(line)
			if lineCount == numberOfLines
				break
                close file
        elif len(args) > 1
        for file in args open file
		print(f"=====>{fileName}<=====", fileName)
		lineCount = 0
                for line in fileObj
                        lineCount += 1
                        print(line)
                        if lineCount == numberOfLines
                                break
		close(fileObj)


def tail(args)
	if args[0] startswith "-n"
		if args[1].isnumeric()
	                numberOfLines = int(args[1])
        	        remove args[0] and args[1]
			for file in args
				open file
				fileLength = 0
				for line in fileObj
					fileLength += 1
				fileLength - numberOfLines = startingLine
				currentLine = 0
				for line in fileObj 
					currentLine += 1
					if currentLine >= startingLine
						print(line)
		else
			usage(number of lines required)        
	else numberOfLines = 10
        for file in args
                open file
                fileLength = 0
                for line in fileObj fileLengh += 1
                fileLength - numberOfLines = startingLine
                currentLine = 0
                for line in fileObj
                        currentLine += 1
                        if current line is >= startingLine, print line
                close file

def sort(args)
	if len.args == 0
		usage(not enough arguments)
	else
		listToSort = []
        	for file in args
			fileObj = open file
                		for line in fileObj
					listToSort.append(line)
                close file
        listToSort.sort()
        for line in listToSort
                print line

def tac(args)
	if len(args) == 0
		usage(too feew arguments)
	else:
        	listToReverse = []
		for file in args
			fileObj = open file
	                for line in fileObj
				listToReserve.append(line)
                listToReverse.reverse()
                for line in list, print line
                close file

def paste(args)
	if args length = 0
		usage(too few arguments)
        else
		listOfFile = []
                for file in args
			fileObj = open(file)
	                listOfFile.append(fileObj)
                numberOfFiles = len(listOfFiles)
                for i in range(findLargestFile(listOFFiles) - 1)
                        currentFile = 0
                	for fileObj in listOfFIles
                        	listToJoin = []
                        	currentFile += 1
                        	if atEOF(fileObj)
                                	ListToJoin.append("")
                        	else:
                                	for position, line in enumerate(fileObj):
                                        	if position == currentLine
                                        	listToJoin.append(line)
                        	listToJoin.join(",")
                        	print(listToJoin, \n)
                	for fileObj in listOfFiles
                        	fileObj.close()

def cut(args)
	if len(args) == 0 
		usage(toofew  arguments)
        elif args[0] == "-f"
                listofflags = []
                args.remove(args[0])
                strOfFlags = args[0]
                args[0].remove
                listof flags = ",".split(stringofflags)
                for file in args
                        open file
                                for line in fileObj
                                        ",".split(line) = listofWords
                                        listToJoin = []
					numberOfFlags = len(listOfFlags)
                                        for i in range(numberOfFlags - 1)
                                                min(listOfFlags)
                                                listOFFlags.remove(min)
                                                if len(list of words) < minOfFlag - 1
                                                        listtojoin.append("")
                                                else
                                                        listtoJoin.append(listOfWords[minOfFlag - 1]
                                        joinedList = ",".join(listToJoin)
					print(joinedList)
			close file
        else
                for file in args open file
                        for line in fileObj
                                split on the comma into list of words
                                print(listofwords[0]
		closeFile

# 3.  Function Template

**Combine the function stubs written in step #1 with pseudocode from step #2.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises???and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
