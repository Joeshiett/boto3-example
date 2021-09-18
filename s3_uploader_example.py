import boto3

# We will be using the S3 resource
s3 = boto3.resource('s3')

# We will be displaying available buckets
x = 0
for bucket in s3.buckets.all():
    x += 1
    print(f'{x}. {bucket.name}')

# We will be uploading cloud.jpg to the joeshiett-bucket2
data = open('cloud.jpg', 'rb')
s3.Bucket('joeshiett-bucket2').put_object(Key='cloud.jpg', Body=data)
print('done...')