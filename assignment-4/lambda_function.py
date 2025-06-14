import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volume_id = 'vol-0123456789abcdef0'  # 🔁 Replace with your own

    # 1️⃣ Create snapshot
    snap = ec2.create_snapshot(
        VolumeId=volume_id,
        Description='Automated snapshot via Lambda'
    )
    snap_id = snap['SnapshotId']
    print(f"Created snapshot: {snap_id}")

    # 2️⃣ Delete old snapshots older than 30 days
    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    snaps = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    for s in snaps:
        if s['VolumeId'] == volume_id and s['StartTime'] < cutoff:
            old_snap_id = s['SnapshotId']
            ec2.delete_snapshot(SnapshotId=old_snap_id)
            print(f"Deleted old snapshot: {old_snap_id}")

    return {'created': snap_id}
#vd