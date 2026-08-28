"""Direct AWS Bedrock invocation."""
import json
import boto3

# FAKE placeholder credentials - not valid, present only for scanner detection.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def invoke(prompt: str, model_id: str = "anthropic.claude-3-5-sonnet-20241022-v2:0") -> str:
    resp = client.invoke_model(
        modelId=model_id,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}],
        }),
    )
    return json.loads(resp["body"].read())["content"][0]["text"]
