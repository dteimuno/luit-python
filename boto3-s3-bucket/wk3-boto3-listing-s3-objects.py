import boto3


s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket='dteimuno-10282024')
for content in response["Contents"]:
    print(content["Key"])