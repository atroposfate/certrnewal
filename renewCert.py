#!/bin/python3

from subprocess import run
import os

#Script must be run as root
if os.geteuid() != 0:
   print("This script must be run as root please retry with sudo in front")
   quit()

print("/nUpdating certificates and restarting necessary systems")
print("Stopping Nginx")
subprocess.run(['systemctl','stop','nginx'])
print("done")
print("Renwing Certs")
errorchek = subprocess.run(['certbot','renew'], capture_output=True)
if errorchek.returncode() != 0:
  print("error on cert renew")
  print("stdout: ", errorchek.stdout.decode())
  quit()
print("done")
print("Restart necessary systems including Nginx")
subprocess.run(['systemctl','start','nginx'])
subprocess.run(['systemctl','restart','postfix','dovecot'])
print("Done!, all updates have been completed and should be working")
