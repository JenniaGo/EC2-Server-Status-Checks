import boto3

# Task: our company have production instances in Paris and development instances in Seoul
# My code will add tag prod or dev to the right instances by regions

# Paris client and resource
ec2_client_paris = boto3.client("ec2", region_name="eu-west-3")
ec2_resource_paris = boto3.resource('ec2', region_name="eu-west-3")

# Seoul client and resource
ec2_client_Seoul = boto3.client("ec2", region_name="ap-northeast-2")
ec2_resource_Seoul = boto3.resource('ec2', region_name="ap-northeast-2")

# Collect instances in Paris to a list
instances_ids_paris = []
reservations_paris = ec2_client_paris.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instances_ids_paris.append(ins['InstanceId'])

# Add prod tag to the Paris instances list
response = ec2_resource_paris.create_tags(
    Resources=instances_ids_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        }
    ]
)

# Collect instances in Seoul to a list
instances_ids_Seoul = []
reservations_paris = ec2_client_Seoul.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    for ins in instances:
        instances_ids_Seoul.append(ins['InstanceId'])

# Add dev tag to the instances in Seoul list
response = ec2_resource_paris.create_tags(
    Resources=instances_ids_Seoul,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        }
    ]
)
