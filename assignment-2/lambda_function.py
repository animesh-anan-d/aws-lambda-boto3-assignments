import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'my-s3-cleanup-demo'  
    days_threshold = 30

    # Calculate the threshold date
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_threshold)

    # List objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("No objects found in the bucket.")
        return

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']

        if last_modified < cutoff_date:
            print(f"Deleting {key} (LastModified: {last_modified})")
            s3.delete_object(Bucket=bucket_name, Key=key)
        else:
            print(f"Keeping {key} (LastModified: {last_modified})")
