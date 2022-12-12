import boto3
import schedule

# Chose a resource \ client
ec2_client = boto3.client("ec2", region_name="us-east-1")

# call check status on instance and system
def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']
        print(f"Instance ID {status['InstanceId']} is {state['Name']} with instance status {ins_status} and system status is {sys_status}")
    print("###################\n")

schedule.every(5).seconds.do(check_instance_status)
# examples: schedule.every().monday.at("12:00") or schedule.every().day.at("1:00") or schedule.every().hour

while True:
    schedule.run_pending()
