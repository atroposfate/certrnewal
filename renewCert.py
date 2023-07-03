#!/bin/python3
'''When Let's Encypt can autoupdate because of the forced 443, This is using nginx as the proxy for a matrix server and assuming dovecot and postfix is running '''
from subprocess import run
import os

#Script must be run as root
if os.geteuid() != 0:
   print("This script must be run as root please retry with sudo in front")
   quit()

print("/nUpdating certificates and restarting necessary systems")
print("Stopping Nginx")
run(['systemctl','stop','nginx'])
print("done")
print("Renwing Certs")
errorchek = run(['certbot','renew'], capture_output=True)
if errorchek.returncode() != 0:
  print("error on cert renew")
  print("stdout: ", errorchek.stdout.decode())
  quit()
print("done")
print("Restart necessary systems including Nginx")
run(['systemctl','start','nginx'])
run(['systemctl','restart','postfix','dovecot'])
print("Done!, all updates have been completed and should be working")
