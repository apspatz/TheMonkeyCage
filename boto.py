import sys
import boto3
from botocore import UNSIGNED
from botocore.client import Config 

s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
filePath = sys.argv[1]
fileName = sys.argv[2]
bucketName = sys.argv[3]

print(filePath, fileName)
with open(filePath, 'rb') as f:
    s3_client.upload_fileobj(f, bucketName, fileName)