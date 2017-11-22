# -*- coding: utf-8 -*-
import sys


'''read file and print'''


def readfile(filename): 
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line) 
    f.close()


if len(sys.argv) < 2:
    print("no argument")
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version': 
        print("Version 1.2.3")
    elif option == 'help':
        print("help documention")
    else:
        print("only --version --help can be used")
        sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
