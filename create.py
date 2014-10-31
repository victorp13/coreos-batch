import os
import digitalocean
import requests
import time

DO_TOKEN = os.environ.get("DO_TOKEN", None)
DO_FINGERPRINT = os.environ.get("DO_FINGERPRINT", None)

manager = digitalocean.Manager(token=DO_TOKEN)

ssh_key = manager.get_ssh_key(DO_FINGERPRINT)

discoveryUri = requests.get("https://discovery.etcd.io/new").content

with file('cloud-config') as f:
	config_file = f.read().format(discoveryUri)

droplet = digitalocean.Droplet(token=DO_TOKEN,
                               name='coreos-1',
                               region='ams3',
                               image='coreos-stable',
                               size='512mb',
                               private_networking=True,
							   ssh_keys=[ssh_key.id],
							   user_data=config_file)
droplet.create()

time.sleep(5)

droplet = manager.get_droplet(droplet.id)

print "droplet #1 created with public ip address: %s" % droplet.ip_address

droplet = digitalocean.Droplet(token=DO_TOKEN,
                               name='coreos-2',
                               region='ams3',
                               image='coreos-stable',
                               size='512mb',
                               private_networking=True,
							   ssh_keys=[ssh_key.id],
							   user_data=config_file)
droplet.create()

time.sleep(5)

droplet = manager.get_droplet(droplet.id)

print "droplet #2 created with public ip address: %s" % droplet.ip_address

droplet = digitalocean.Droplet(token=DO_TOKEN,
                               name='coreos-3',
                               region='ams3',
                               image='coreos-stable',
                               size='512mb',
                               private_networking=True,
							   ssh_keys=[ssh_key.id],
							   user_data=config_file)
droplet.create()

time.sleep(5)

droplet = manager.get_droplet(droplet.id)

print "droplet #3 created with public ip address: %s" % droplet.ip_address
