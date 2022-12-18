import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Create a new EC2 instance
response = ec2.run_instances(
    ImageId='ami-12345678',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='my-key-pair',
    SecurityGroups=['my-security-group']
)

# Get the instance ID of the new instance
instance_id = response['Instances'][0]['InstanceId']
print(f'Created instance with ID: {instance_id}')

# Tag the instance
ec2.create_tags(
    Resources=[instance_id],
    Tags=[{'Key': 'Name', 'Value': 'My EC2 instance'}]
)

# Start the instance
ec2.start_instances(InstanceIds=[instance_id])
print(f'Started instance with ID: {instance_id}')
