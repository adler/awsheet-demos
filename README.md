# AWSHeet Demo

Clone this repository and customize it. Now you can use https://github.com/adler/awsheet

## Requirements
* AWS credentials authoirzed with at least 'Amazon EC2 Full Access' (use [IAM](https://console.aws.amazon.com/iam/home?region=us-east-1) to create a special user)
* EC2 requires a [key pair](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs)

## Getting Started
1. install requirements (AWSHeet )
 
 ````sudo pip install -r requirements.txt````
3. replace CHANGEME with your own values in demo.py and demo.auth (including key_name)
 
 ````
 cp demo.auth.example demo.auth
 $EDITOR demo.auth
 $EDITOR demo.py
 ````
4. run the demo script to create an instance
 
 ````
 $ ./demo.py
 ````
5. run the demo script again to destroy the instance 

 ````
 $ ./demo.py --destroy
 ````

## Notes

to load awsheet from a special directory (e.g. a local checkout) instead of from site-packages
````
env PYTHONPATH=~/work/awsheet/ python ./demo.py
````
