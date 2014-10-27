import os
import digitalocean

DO_TOKEN = os.environ.get("DO_TOKEN", None)

manager = digitalocean.Manager(token=DO_TOKEN)

my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    droplet.destroy()