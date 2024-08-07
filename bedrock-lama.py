import boto3
import json
import pprint

bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "anthropic.claude-v2"

prompt_data = """
Write about me for a software engineer."""

payload = {
    "prompt": prompt_data,
    "temperature": 0.5,
    "top_p": 1
}

body = json.dumps(payload)
# response = bedrock_client.invoke_model(
#     modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
#     body=body,
#     accept="application/json",
#     contentType="application/json"
# )
response = bedrock_client.invoke_model(
    modelId="anthropic.claude-v2",
    body=body
)

        
        
        
response_body = json.loads(response.get("body").read())
print(type(response_body))
pprint.pprint(response_body)

"""
Below code is for listing all the bedrock models
"""
# import boto3

# bedrock_client = boto3.client("bedrock", region_name="us-east-1")
# response = bedrock_client.list_foundation_models()
# print(response)
#