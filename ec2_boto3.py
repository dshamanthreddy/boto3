
import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')

response = ec2_client.describe_instances()['Reservations']  
for instance in response:
    for value in instance['Instances']:
        pprint(value['InstanceId'])
    
    # pprint(instance)

# #!/usr/bin/env python3
# import boto3
# # Create an EC2 resource
# ec2 = boto3.resource('ec2')

# # Get all instances
# instances = ec2.instances.all()

# # Print the instance IDs
# for instance in instances:
#     print(f"Instance ID: {instance.id}")    