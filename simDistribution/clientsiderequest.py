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

import subprocess

IP = "" # IP address of the client
USER = "" # username on the server
HOMEDIR = "" # home directory of the user on the server
PROJECT_DIR = "" # root directory of the project on the server

subprocess.check_call("ssh %(user)s@137.122.93.28 'sh %(home)s/%(project_dir)s/serverside %(ip)s'" %{'ip':IP, 'user':USER, 'home':HOMEDIR, 'project_dir':PROJECT_DIR}, shell=True, executable='/bin/bash')
