import boto3

s3 = boto3.resource('s3')

x = 0
for bucket in s3.buckets.all():
    x += 1
    print(f'{x}. {bucket.name}')