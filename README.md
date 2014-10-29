coreos-batch
============

Python scripts for batch creation of CoreOS droplets on Digital Ocean

### Environment variables
This script requires two environment variables to be set up:

* DO_TOKEN
* DO_FINGERPRINT

DO_TOKEN is your Digital Ocean API access token, and DO_FINGERPRINT is the fingerprint of your preferred SSH KEY.

You can add these variables via the "export" command temporarily for the session, or on the mac permanently by adding them to ~/.bash_profile

### python-digitalocean
pip install python-digitalocean==1.0.5b