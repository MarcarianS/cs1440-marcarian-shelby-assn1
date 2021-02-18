#!/usr/bin/env python
import sys
from Usage import usage
import WordCount


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    sys.argv.remove(sys.argv[0])
    sys.argv.remove(sys.argv[0])
    WordCount.wc(sys.argv)
    print("TODO: determine which tool the user has invoked")
    print("TODO: call on that tool, forwarding any remaining arguments to it")
