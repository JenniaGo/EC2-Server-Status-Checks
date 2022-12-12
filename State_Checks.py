import boto3

# Chose a resource \ client
ec2_client = boto3.client("ec2", region_name="us-east-1")

# list all ec2 instances with ID ssh key name and running state
reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f" Instance {instance['InstanceId']} ({instance['KeyName']}) is {instance['State']['Name']}")

# call check status on instance and system
statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    print(f"Instance ID {status['InstanceId']} status is {ins_status} and system status is {sys_status}")
