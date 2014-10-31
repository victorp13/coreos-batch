import os
import digitalocean
import requests
import time

# Function that creates the droplets
def createdroplet( number ):
	droplet = digitalocean.Droplet(token=DO_TOKEN,
                               name='coreos-{0}'.format(number),
                               region='ams3',
                               image='coreos-stable',
                               size='512mb',
                               private_networking=True,
							   ssh_keys=[ssh_key.id],
							   user_data=config_file)
	droplet.create()
	time.sleep(5)
	droplet = manager.get_droplet(droplet.id)
	#print "droplet #%s created with public ip address: %t" % (number, droplet.ip_address)
	print "droplet #{0} created with public ip address: {1}".format(number, droplet.ip_address)
	return

# Load environment variables for DO token and SSH Key fingerprint
DO_TOKEN = os.environ.get("DO_TOKEN", None)
DO_FINGERPRINT = os.environ.get("DO_FINGERPRINT", None)

# DO API init
manager = digitalocean.Manager(token=DO_TOKEN)
ssh_key = manager.get_ssh_key(DO_FINGERPRINT)

# Get new etcd discovery uri
discoveryUri = requests.get("https://discovery.etcd.io/new").content

# Load template cloud-config file with discovery uri inserted
with file('cloud-config') as f:
	config_file = f.read().format(discoveryUri)

# Create droplets
createdroplet(1)
createdroplet(2)
createdroplet(3)