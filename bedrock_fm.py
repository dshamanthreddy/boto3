import boto3
import botocore.config
import botocore.exceptions
import json
import sys
import pprint
from textwrap import fill

bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

def blog_genai(blogtopic:str) -> str:
    prompt_data = f"""<s>[INST]Human: Write a 300 words blog about {blogtopic}
    Assistant:[/INST]
    """
    body={
        "prompt": prompt_data,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    try:
        response_body = invoke_model(body)
        pprint.pprint(response_body)
        return response_body
    except Exception as e:
        print(f"Error: {e}")

def invoke_model(body):
    response = bedrock_client.invoke_model(
        modelId="meta.llama3-70b-instruct-v1:0",
        body=json.dumps(body)
    )
    response_body = response.get("body").read().decode("utf-8")
    return response_body

# Assuming you have bedrock_client set up correctly
# blog_genai("AI for devops")

def format_blog(response, topic):
    title = f"Blog on {topic}"
    formatted_title = f"{title}\n{'='*len(title)}\n\n"
    formatted_content = fill(response, width=80)
    return formatted_title + formatted_content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <topic>")
        sys.exit(1)

    topic = sys.argv[1]
    blog_genai(topic)    
