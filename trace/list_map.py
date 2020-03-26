import subprocess
import time
IP_LIST = [ 'google.com',
  'yahoo.com',
  'yelp.com',
  'amazon.com',
  'freebase.com',
  'clearink.com',
  'ironport.com' ]
cmd_stub = 'ping -c 5 %s'
def do_ping(addr):
    print (time.asctime(), "DOING PING FOR", addr)
    cmd = cmd_stub % (addr,)
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
from common import IP_LIST, do_ping
import time
z = []
#for i in range(0, len(IP_LIST)):
for ip in IP_LIST:
    p = do_ping(ip)
    z.append((p, ip))
for p, ip in z:
    print (time.asctime(), "WAITING FOR", ip)
    p.wait()
    print (time.asctime(), ip, "RETURNED", p.returncode)
