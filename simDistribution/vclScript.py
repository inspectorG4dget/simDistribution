import smtplib
import subprocess
import os
import itertools
import commands

LOCAL_HOME = '' # absolute path to the home directory on the client
SERVER_USER = '' # username on the server
SERVER_IP = '' # IP address of the server
PROJECT_DIR = '' # relative path (from the home directory) to the root of the project directory
NETWORK_DEVICE = '' # the device in `ifconfig` through which the network is accessed

SMTP_SERVER = '' # the smtp server through which emails will be sent
SMTP_PORT = None # the port through which emails will be sent on the smtp server
FROM_ADDR = '' # the address from which notification emails will be sent
TO_ADDR = '' # the address to which notification emails will be sent

NUM_CORES = None # the number of simulations to be run on this client
CALL_SIM = '' # how would you normally invoke the simulation from the command line on the client

ALIASES = """
alias site='ssh apanc006@ugate.site.uottawa.ca'

alias athena='ssh ashwin@137.122.91.161'
alias hermit='ssh ashwin@137.122.93.28'
alias medias='ssh ashwin@137.122.91.128'
alias payeur='ssh apanc006@137.122.91.124'
alias fouyadh='ssh apanc006@137.122.91.67'
alias petriu='ssh apanc006@137.122.88.192'

alias que='clear && atq | wc -l && atq | sort -t" " -k1 -n && date'
alias show='at -c'
alias glist='clear && ls ~/cisdagp/cisdagp/scenario2/p5h7t6c9m5/GP*.py | tr -d '.py' | sort -t"P" -k2 -n'
alias socks='ps aux | grep '

alias als='vim ~/.bash_aliases'
alias basher='vim ~/.bashrc'

alias shell='source ~/.bashrc'

alias bye='exit'
"""

# authorize server's key on client
writekey = False
serverkey = "" # rsa public key of the server from ~/.ssh/id_rsa.pub on the server
with open('@(home)s/.ssh/authorized_keys' %{'home':LOCAL_HOME}) as keyfile:
    if serverkey not in keyfile:
        writekey = True

if writekey:
    with open('@(home)s/.ssh/authorized_keys' %{'home':LOCAL_HOME}, 'a') as keyfile:
        keyfile.write(serverkey)

# copy over all simulations
done = False
while not done:
    try:
        subprocess.check_call("scp -r %(user)s@%(host)s:%(home)s/%(projectdir) ./" %{'user':SERVER_USER, 'host':SERVER_IP, 'projectdir':PROJECT_DIR}, shell=True, executable='/bin/bash')
        done = True
    except:
        pass

# put client's IP in clientsiderequest.py
IP = [i for i in commands.getoutput('ifconfig %(NIC)s' %{"NIC":NETWORK_DEVICE}).split() if 'addr:' in i and i!='addr:' and '127.0.0.1' not in i][0].partition(":")[-1]
with open('%(home)/%(projectdir)s/clientsiderequest.py' %{"home":LOCAL_HOME, "projectdir":PROJECT_DIR}) as infile:
    contents = infile.read()

with open('%(home)s/.bash_aliases' %{"home":LOCAL_HOME}, 'a') as outfile:
    outfile.write(ALIASES)

with open('%(home)s/%(projectdir)s/clientsiderequest.py' %{'home':LOCAL_HOME, 'projectdir':PROJECT_DIR}, 'w') as outfile:
    outfile.write(contents.replace('''IP = ""''', '''IP = "%s"''' %IP))

with open('%(home)s/.bashrc' %{'home':LOCAL_HOME}, 'a') as outfile:
    outfile.write('\nsource ~/.bash_aliases\n')

with open('%(home)s/.bash_aliases' %{'home':LOCAL_HOME}, 'w') as outfile:
    outfile.write(ALIASES)

# email notification that client is setup
sm = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
sm.sendmail(FROM_ADDR, TO_ADDR, 'client is setup at IP: %s' %IP)

done = False
while not done:
    try:
        subprocess.check_call("""for i in `seq 1 %(inst)s`; do %(invokeScript)s ; sleep 10 ; done""" %{'inst':NUM_CORES, 'invokeScript':CALL_SIM}, shell=True, executable='/bin/bash')
        done = True
    except:
        pass
