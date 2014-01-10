#!/usr/bin/env python

import os
import re
import sys
import time
import urllib2
import awsheet

defaults = {
    # each heet object is associated with a single region
    'region' : 'us-east-1',
    # Ubuntu Server 12.04.3 LTS - ami-a73264ce (64-bit) / ami-a53264cc (32-bit)
    'ami' : 'ami-a73264ce',
}

heet = awsheet.AWSHeet(defaults)

# create a security that opens ports 22 and 80 to the entire internet
rules = [
    {'ip_protocol':'tcp', 'from_port':22, 'to_port':22, 'cidr_ip':'0.0.0.0/0'},
    {'ip_protocol':'tcp', 'from_port':80, 'to_port':80, 'cidr_ip':'0.0.0.0/0'},
]
group = awsheet.SecurityGroupHelper(
    heet=heet,
    name='cloudinit-demo',
    description='AWSHeet CloudInit Demo',
    rules=rules
)

# script that installs apache and creates a custom home page
script = """#!/bin/bash
apt-get install -y apache2
cat > /var/www/index.html <<EOF
 Hello, World!
    - AWSHeet
EOF
"""

# create an instance in the new security group and have cloud-init run the script at boot time
instance = awsheet.InstanceHelper(
    heet=heet,
    role='cloudinit-demo',
    user_data=script,
    security_groups=[group.name]
)
url = "http://" + instance.get_instance().public_dns_name

if heet.get_destroy():
    exit(0)

# wait until the new instance responds to http requests and print out the response
while True:
    try:
        response = urllib2.urlopen(url).read()
        # verify the default apache page is replaced with the AWSHeet page
        if re.search('AWSHeet', response):
            print "\n\n", response
            break
        time.sleep(1)
    except:
        heet.logger.debug("waiting for instance to respond to http requests")
        time.sleep(5)
