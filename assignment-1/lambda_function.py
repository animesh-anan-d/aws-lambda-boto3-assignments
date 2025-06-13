import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all instances
    instances = ec2.describe_instances()
    
    # Containers for instance IDs
    to_stop = []
    to_start = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            tags = instance.get('Tags', [])
            for tag in tags:
                if tag['Key'] == 'Action':
                    if tag['Value'] == 'Auto-Stop':
                        to_stop.append(instance_id)
                    elif tag['Value'] == 'Auto-Start':
                        to_start.append(instance_id)
    
    # Stop instances
    if to_stop:
        ec2.stop_instances(InstanceIds=to_stop)
        print(f"Stopped: {to_stop}")

    # Start instances
    if to_start:
        ec2.start_instances(InstanceIds=to_start)
        print(f"Started: {to_start}")
