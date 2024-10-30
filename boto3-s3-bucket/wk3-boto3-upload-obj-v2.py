import boto3
s3 = boto3.client('s3')

s3.upload_file('/Users/dteimuno/Documents/GitHub/luit-python/test_text.txt', 'dteimuno-10282024', 'test_text.txt')