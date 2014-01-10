#!/usr/bin/env python

import os
import awsheet

defaults = {

    # each heet object is associated with a single region
    'region' : 'us-east-1',

    # pick a default ami so you don't have to pass it as an argument to every InstanceHelper
    # Ubuntu Server 12.04.3 LTS - ami-a73264ce (64-bit) / ami-a53264cc (32-bit)
    'ami' : 'ami-a73264ce',

    # ec2 requires you must create or upload key pair https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:
    'key_name' : 'CHANGEME',

    }

heet = awsheet.AWSHeet(defaults)

cf = awsheet.CloudFormationHelper(
    heet, stack_base_name='cf-demo-vpc',
    # downloaded from https://s3.amazonaws.com/cloudformation-templates-us-east-1/vpc_single_instance_in_subnet.template
    template_file_name=os.path.dirname(os.path.realpath(__file__)) + '/vpc_single_instance_in_subnet.template',
    # use same key pair as in defaults hash - pass in as CloudFormation parameter
    parameters={'KeyName' : defaults['key_name']}
    )

subnet_id = cf.get_resource('Subnet')
security_group = cf.get_resource('InstanceSecurityGroup')

awsheet.InstanceHelper(heet=heet, role='cf-demo', subnet_id=subnet_id, security_groups=[security_group])
