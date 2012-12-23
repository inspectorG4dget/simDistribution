import subprocess
import sys
import datetime
import os

DIR1, DIR2, FILENAME, IP = sys.argv[1:]
try:
    subprocess.check_call("sh ~/cisdagp/clientsideexec %(dir1)s %(dir2)s %(filename)s %(ip)s" %{'dir1':, 'dir2':, 'filename':, ip':IP}, shell=True, executable='/bin/bash') # Change code for N in this line

except:
    pass
