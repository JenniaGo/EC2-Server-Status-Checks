import boto3

# Chose a resource \ client
ec2_client = boto3.client("ec2", region_name="us-east-1")

# call check status on instance and system
statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    state = status['InstanceState']
    print(f"Instance ID {status['InstanceId']} is {state['Name'} with instance status {ins_status} and system status is {sys_status}")

# result: Instance ID i-00aaed4174d9b2687 is running with instance status ok and system status is ok Instance ID i-03c226cc16ecdb888 is running with instance status ok and system status is ok
