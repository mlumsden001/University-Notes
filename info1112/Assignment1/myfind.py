#!/usr/bin/env python3

import sys
import os

USAGE = "Usage: myfind [--regex=pattern | --name=filename] directory [command]"

# You can change this function signature if desired
def find(directory, regex=None, name=None, command=None):
    #sys.argv.split(" ")
    for (root, dirs, files) in os.walk(directory, name or regex):

        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
# "ls -l {}"

if __name__ == "__main__":
    if len(sys.argv < 2):
        print(USAGE)
        sys.exit(0)
    inputs = []
    i = 1
    for i in range(0, len(sys.argv)):
        if "--regex=" in sys.argv[i]:
            regex = sys.argv[i]
        else if "--name=" in sys.argv[i]:
            name = sys.argv[i]
        else if
    ##while i < len(sys.argv):
        if sys.argv[i][0] == "-":
            sys.argv[i].split("=")
            filename = sys.argv[i][1]
            inputs.append(filename)
        inputs.append(sys.argv[i])

    find(*sys.argv)
