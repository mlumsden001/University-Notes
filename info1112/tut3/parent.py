import time

print("in the child")
time.sleep(2)

import os
import sys

if os.fork() == 0:
    print("Running child.py")
    os.execl("./child.py", " ")

else:
    print("Continue running parent")
    time.sleep(2)
