import Usage

def wc(files):
    lineCountList = []
    wordCountList = []
    charCountList = []
    if len(files) == 0:
        Usage.usage("Too few arguments, please provide at least one file.", 'wc')
    else:
        for file in files:
            fileObj = open(file)
            lineCount = 0
            charCount = 0
            wordCount = 0
            for line in fileObj:
                lineCount += 1
                charCount += len(line)
                wordCount += line.count(",") + 1
            lineCountList.append(lineCount)
            wordCountList.append(wordCount)
            charCountList.append(charCount)
            fileObj.close()
        #If only given one file, print the counts out like normal
        for i in range(len(files)):
            print('{:>5}'.format(str(lineCountList[i])) + '{:>5}'.format(str(wordCountList[i])) +
                  '{:>5}'.format(str(charCountList[i])) + '{:>10}'.format(files[i]) + "\n")
        if len(files) == 1:
            return
        else:
            lineSum = 0
            wordSum = 0
            charSum = 0
            for value in lineCountList:
                lineSum += value
            for value in wordCountList:
                wordSum += value
            for value in charCountList:
                charSum += value
            print('{:>5}'.format(str(lineSum)) + '{:>5}'.format(str(wordSum)) + '{:>5}'.format(str(charSum)) +
                  '{:>10}'.format("Total") + "\n")



