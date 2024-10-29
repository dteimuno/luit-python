import boto3
bucket = 'dteimuno-10282024'
key = 'test_text.txt'
filename = 'test_text.txt'

s3 = boto3.client('s3')

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)