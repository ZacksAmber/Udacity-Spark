#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

"""
Instructions:

    1. Do not forget to add the --auto-terminate field because EMR clusters are costly. 
    Once you run this script, you’ll be given a unique cluster ID. 
    Check the status of your cluster using `aws emr --cluster-id <cluster_id>`.
    2. We'll be creating an EMR cluster for the exercise.
    3. First, install `awscli` using pip.  You can get instructions for MacOS, Windows, Linux here  on [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).
    4. This will give you access to create an EMR cluster and EC2 cluster. The EC2 cluster shows a status of all the clusters with your keys, etc. It does a ton of things!
    5. Once it's installed, run the script below to launch your cluster. Be sure to include the appropriate file names within the <> in the code.

"""

# Specify your cluster name 
YOUR_CLUSTER_NAME = "spark-udacity"

# Insert your IAM KEYNAME - Remember, your IAM key should saved under .ssh/ directory
YOUR_KEY_NAME = "EMR-CA"

YOUR_SUBNET_ID = "subnet-77db0411"

# Specify your bootstrap file. Please note that this step is optional. It should be an executable (.sh file) in an accessible S3 location. If you aren't going to use the bootstrap file, you can remove the `--bootstrap-actions` tag above.
# This file is provided in the zipped folder titled “Exercise_Creating EMR Cluster” at the bottom of this page.

# In this EMR script, execute using Bootstrap
# The script must be a location in Amazon S3 or a local path starting with 'file:'
YOUR_BOOTSTRAP_FILENAME = "s3://aws-labs-bucket/EMR/spark-udacity/bootstraps/bootstrap_emr.sh"

# Add your cluster name
emr = f"""
aws emr create-cluster \
--name {YOUR_CLUSTER_NAME} \
--release-label emr-6.5.0 \
--applications Name=Hadoop Name=Spark Name=Livy Name=JupyterEnterpriseGateway \
--use-default-roles \
--instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge \
--ec2-attributes "KeyName={YOUR_KEY_NAME}, SubnetId={YOUR_SUBNET_ID}" \
--bootstrap-actions Path={YOUR_BOOTSTRAP_FILENAME} \
"""

# print(emr)
subprocess.run(emr, shell=True)
