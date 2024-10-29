import boto3

s3 = boto3.client('s3')


response = s3.create_bucket(
    Bucket='dteimuno-10282024'
)

print(response)