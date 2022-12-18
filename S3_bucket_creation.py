import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create a new S3 bucket
response = s3.create_bucket(
    Bucket='my-new-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    }
)

print(f'Created bucket with name: {response["Location"]}')
