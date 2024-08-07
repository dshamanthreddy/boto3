import boto3
from pprint import pprint

s3_client = boto3.client('s3')

response = s3_client.list_buckets()['Buckets']
for bucket in response:
    print(bucket['Name'])

# for bucket in response['Buckets']:
#     pprint(bucket['Name'])

# pprint(response)



"""
below code is to create s3 bucket if it does not exist
"""


# import boto3

# s3 = boto3.resource('s3')
# bucket_name = 'abd-boto3-test'

# all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
# if bucket_name not in all_my_buckets:
#     print(f"Bucket {bucket_name} does not exist")
#     s3.create_bucket(Bucket=bucket_name)
#     print(f"Bucket {bucket_name} created successfully")
# else:
#     print(f"Bucket {bucket_name} already exists")