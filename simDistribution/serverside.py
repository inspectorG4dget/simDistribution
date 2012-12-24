'''
Copyright 2012 Ashwin Panchapakesan

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

import sys
import time
import smtplib
import subprocess
import os
import itertools

IP = sys.argv[1].strip()
PROJECT_DIR = "" # relative path (relative to the home directory) to the root directory of the project, which contains all subdirs containing simulation files

USERS = { # keys are IPs of the clients, values are user names on those clients
        }

HOMES = { # keys are the IPs of clients, values are the absolute paths to the home directories on these clients for the usernames on these clients  identified in USERS
        }
HOME = None # absolute path to the home directory on the server

SMTP_SERVER = ""
SMTP_PORT = None
FROM_ADDR = None # the email address from which notification emails will be sent
TO_ADDR = None # the email address to which notification emails will be sent

def get_next_simulation():
    """ This function returns a list. 
        The list contains N>0 elements.
        Each of the first N-1 elements are names of directories (not paths), which when joined together form a relative path (relative from PROJECT_DIR).
        The Nth element is the name of the file - the simulation to be run.
        Before the end user implements this function, it is assumed that N=3.
        Once this function has been implemented, if N!=3, change the code in the lines annotated with "Change code for N in this line"
             Also look for this annotation in clientside.py and clientsideexec """

    pass

done = False
DIR1, DIR2, FILENAME = get_next_simulation() # Change code for N in this line

while not done:
    try:
        subprocess.check_call("""ssh %(user)s@%(host)s 'sh %(home)s/%(project)/clientside %(dir1)s %(dir2)s %(filename)s %(host)s' """ %{'user':USER, 'host':IP, 'home':HOME[IP], 'project':PRJECT_DIR, 'dir1':DIR1, 'dir2':DIR2, 'filename':FILENAME}, shell=True) # Change code for N in this line
        done = True

        os.remove("%(home)s/%(project)/%(dir1)s/%(dir2)s/%(filename)s" %{'home':HOME, 'project':PROJECT_DIR, 'dir1':DIR1, 'dir2':DIR2, 'filename':FILENAME}) # Change code for N in this line

        sm = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        sm.sendmail(FROM_ADDR, TO_ADDR, "running %(project)s/%(dir1)s/%(dir2)s/%(filename)s on %(host)s" %{'project':PROJECT_DIR, 'dir1':DIR1, 'dir2':DIR2, 'filename':FILENAME, 'host':IP}) # Change code for N in this line
    except:
        pass
