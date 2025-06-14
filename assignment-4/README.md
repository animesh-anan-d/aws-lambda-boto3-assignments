# Assignment 4: Automatic EBS Snapshot and Cleanup using Lambda & Boto3

## 🎯 Objective
Automate snapshot creation and cleanup (older than 30 days) for a specified EBS volume.

---

## 🚩 Setup Steps

### 1. EBS Volume
- Use volume `vol-0123456789abcdef0` (example).
- Located in the same region as Lambda.

### 2. IAM Role
- Created `lambda-ec2-snapshot-role` with `AmazonEC2FullAccess`.

### 3. Lambda Function
- Named `ebs-snapshot-cleaner`
- Runtime: Python 3.x
- Key code functionality:
  - Creates a new snapshot
  - Deletes stale snapshots (older than 30 days)

![Screenshot 2025-06-14 184048](https://github.com/user-attachments/assets/591cc695-9d93-4a49-b2ff-558839acc5c8)

###  Screenshots

![Screenshot 2025-06-14 184048](https://github.com/user-attachments/assets/24ec86d2-a930-4776-ad89-ae2708ebade8)
![Screenshot 2025-06-14 184048](https://github.com/user-attachments/assets/95bcfe7b-ca7e-4342-b3ae-8774e50d758f)
![Screenshot 2025-06-14 184125](https://github.com/user-attachments/assets/0cda8120-3c05-473e-ab57-f4120935f3f6)
![Uploading Screenshot 2025-06-14 183908.png…]()
![Uploading Screenshot 2025-06-14 183828.png…]()

![Screenshot 2025-06-14![Screenshot 2025-06-14 183908](https://github.com/user-attachments/assets/84197d1d-9917-42e6-a40e-159a152d3fa5)
![Screenshot 2025-06-14 184125](https://github.com/user-attachments/assets/cd1adc1e-9c22-4662-abb6-ce5e05d9338c)
![Screenshot 2025-06-14 183828](https://github.com/user-attachments/assets/871b4418-5a7e-4a0e-abcb-52c10bc0fcfc)
 184125](https://github.com/user-attachments/assets/b281c47b-8b2f-44a6-9422-15596492ec19)
![Screenshot 2025-06-14 183828](https://github.com/user-attachments/assets/6ba9c1d1-62be-488b-8187-9287f99ee392)
