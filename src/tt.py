#!/usr/bin/env python
import sys
from Usage import usage
import WordCount
import Concatenate
import Partial
import Grep
import Sorting
import CutPaste

if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    sys.argv.remove(sys.argv[0])
    if sys.argv[0] == "cat":
        sys.argv.remove(sys.argv[0])
        Concatenate.cat(sys.argv)
    elif sys.argv[0] == "tac":
        sys.argv.remove(sys.argv[0])
        Concatenate.tac(sys.argv)
    elif sys.argv[0] == "wc":
        sys.argv.remove(sys.argv[0])
        WordCount.wc(sys.argv)
    elif sys.argv[0] == "head":
        sys.argv.remove(sys.argv[0])
        Partial.head(sys.argv)
    elif sys.argv[0] == "tail":
        sys.argv.remove(sys.argv[0])
        Partial.tail(sys.argv)
    elif sys.argv[0] == "grep":
        sys.argv.remove(sys.argv[0])
        Grep.grep(sys.argv)
    elif sys.argv[0] == "sort":
        sys.argv.remove(sys.argv[0])
        Sorting.sort(sys.argv)
    elif sys.argv[0] == "paste":
        sys.argv.remove(sys.argv[0])
        CutPaste.paste(sys.argv)

    #print("TODO: determine which tool the user has invoked")
    #print("TODO: call on that tool, forwarding any remaining arguments to it")
