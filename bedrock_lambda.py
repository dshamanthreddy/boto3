import boto3
import botocore.config
import json

from datetime import datetime



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
        bedrock=boto3.client("bedrock-runtime", region_name="us-east-1", config=botocore.config.Config(read_timeout=300)) # variable to call FM 
        print("Calling Bedrock")
        response=bedrock.invoke_model(body=json.dumps(body), modelId="meta.llama3-70b-instruct-v1:0", accept="application/json", contentType="application/json") # Invoking
        response_content=response.get("body").read().decode("utf-8") # Reading the response
        response_data=json.loads(response_content)
        print (response_data)
        blog_details=response_data["generation"]
        return blog_details
    except Exception as e:
        print(f"Error: {e}")
        return None
def save_blog_to_s3(blog_details, s3_key, s3_bucket):
    s3=boto3.client("s3")
    try:
        s3.put_object(Body=blog_details, Bucket=s3_bucket, Key=s3_key) # saving the blog to s3
        print(f"Blog saved to s3://{s3_bucket}/{s3_key}")
    except Exception as e:
        print(f"Error saving blog to S3: {e}")




def lambda_handler(event, context):
    # TODO implement
    event= json.loads(event['body'])
    blogtopic= event['blog_topic']
    generate_blog= blog_genai(blogtopic=blogtopic)

    if generate_blog:
        current_dateTime= datetime.now().strftime("%H:%M:%S")
        s3_key= f"blog_{current_dateTime}.txt"
        s3_bucket= "awsbedddrockkkfile"
        save_blog_to_s3(generate_blog, s3_key, s3_bucket)
    else:
        print("Failed to generate blog")
    return {
        'statusCode': 200,
        'body': json.dumps('blog is created')

    } 


