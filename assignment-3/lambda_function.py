import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    try:
        buckets = s3.list_buckets()['Buckets']
        print("Checking buckets for encryption...")
        
        for bucket in buckets:
            bucket_name = bucket['Name']
            try:
                enc = s3.get_bucket_encryption(Bucket=bucket_name)
                rules = enc['ServerSideEncryptionConfiguration']['Rules']
                print(f"✅ {bucket_name} is encrypted with: {rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']}")
            except ClientError as e:
                if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                    print(f"❌ {bucket_name} is NOT encrypted")
                else:
                    print(f"⚠️ Error checking {bucket_name}: {e}")
    
    except Exception as e:
        print("❗ Unexpected error:", e)
