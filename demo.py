#!/usr/bin/env python

import awsheet

defaults = {

    # each heet object is associated with a single region
    #'region' : 'us-east-1',

    # pick a default ami so you don't have to pass it as an argument to every InstanceHelper
    # Ubuntu Server 12.04.3 LTS - ami-a73264ce (64-bit) / ami-a53264cc (32-bit)
    'ami' : 'ami-a73264ce',

    # ec2 requires you must create or upload key pair https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:
    #'key_name' : 'CHANGME',

    # without a subnet_id, EC2 will use default-vpc subnet or ec2-classic
    #'subnet_id' : 'CHANGEME',

    # AWS uses security group *names* for ec2-classic and default-vpc, but uses security group *ids* otherwise
    # bottomline: if you specify the subnet_id, then security groups must be provided as *ids* not *names*

    # base_security_groups will be used for all instances. You can add more per-instance.
    #'base_security_groups' : ['CHANGEME'],

    }

heet = awsheet.AWSHeet(defaults)
awsheet.InstanceHelper(heet=heet, role='demo')
#awsheet.InstanceHelper(heet=heet, role='demo', security_groups=['CHANGEME'])
