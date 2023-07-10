# certrnewal
This is a cert renewal for a let's encrypt email server running a reverse proxy on nginx (that prevents the renewal) and postfix and dovecot need to be restarted

This is a pretty niche use case as I am running a reverse proxy on port 80 on my mailserver for another application and so the certbot doesn't renew properly
When I forgot to do all these steps my fairmail client with throw and error on expired certificates until I restarted the postfix and dovecot
