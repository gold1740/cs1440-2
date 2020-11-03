#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort, uniq
from WordCount import wc
from Usage import usage
import sys


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    choice = sys.argv[1].lower()

args = sys.argv[2:]
if choice == "cat":
    cat(args)
elif choice == "tac":
    tac(args)
elif choice == "cut":
    cut(args)
elif choice == "paste":
    paste(args)
elif choice == "grep":
    grep(args)
elif choice == "head":
    head(args)
elif choice == "tail":
    tail(args)
elif choice == "sort":
     sort(args)
elif choice == "uniq":
    uniq(args)
elif choice == "wc":
    wc(args)
else:
    usage()
