# [terminal]$: ping 127.0.0.1 -c 4 #1:

import subprocess #13:
import sys #14:

cmd = ['ping', '127.0.0.1', '-c', '4'] #15:
encoding1 = 'utf_8' #16:
sys1 = sys.platform #17:

if sys1 == 'win32': #18:
    cmd = ['ping', '127.0.0.1']
    encoding1 = 'cp850'

# subprocess.run(cmd) #2: #19:
proc = subprocess.run(cmd)
print(proc) #3: #4:

print(proc.args) #5: #20:
print(proc.stderr) #6: #21:
print(proc.stdout) #7: #22:
print(proc.returncode) #8: #9: #23:

proc2 = subprocess.run(cmd, capture_output=True) #24:
print(proc2.stdout.decode(encoding1)) #10: #25:

proc3 = subprocess.run(cmd, capture_output=True, text=True) #26:
print(proc3.stdout) #11:

print(sys.platform) #12: #27:

# Edson Copque | https://linktr.ee/edsoncopque
