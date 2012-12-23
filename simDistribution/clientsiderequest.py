import subprocess

IP = "" # IP address of the client
USER = "" # username on the server
HOMEDIR = "" # home directory of the user on the server
PROJECT_DIR = "" # root directory of the project on the server

subprocess.check_call("ssh %(user)s@137.122.93.28 'sh %(home)s/%(project_dir)s/serverside %(ip)s'" %{'ip':IP, 'user':USER, 'home':HOMEDIR, 'project_dir':PROJECT_DIR}, shell=True, executable='/bin/bash')
