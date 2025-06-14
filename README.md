
## 📚 Assignments Overview

### 🔹 Assignment 1: **Automated Instance Management**
- Start/Stop EC2 instances based on tags and schedule.
- Uses `boto3.client('ec2')` to manage instances.
- Implements tag-based filtering and status reporting.
➡️ [Details inside `assignment-1/README.md`](./assignment-1/README.md)

---

### 🔹 Assignment 2: **S3 File Upload and Cleanup**
- Upload multiple files to an S3 bucket.
- Clean up files older than a specified age.
- Uses `boto3.client('s3')` and `os` for file filtering.
➡️ [Details inside `assignment-2/README.md`](./assignment-2/README.md)

---

### 🔹 Assignment 3: **Monitor Unencrypted S3 Buckets**
- Detects S3 buckets without server-side encryption.
- Logs unencrypted bucket names for compliance review.
- Uses `boto3.client('s3')` and `get_bucket_encryption`.
➡️ [Details inside `assignment-3/README.md`](./assignment-3/README.md)

---

### 🔹 Assignment 4: **Automatic EBS Snapshot and Cleanup**
- Takes snapshots of specified EBS volumes.
- Deletes snapshots older than 30 days to save cost.
- Uses `boto3.client('ec2')` and date filtering.
➡️ [Details inside `assignment-4/README.md`](./assignment-4/README.md)

---

## ⚙️ Prerequisites

- AWS account with programmatic access (Access Key & Secret).
- IAM Roles created with required permissions.
- AWS Lambda with Python 3.x runtime.
- Boto3 installed (pre-installed in Lambda).
- S3, EC2, EBS setup as per individual assignment instructions.

---

## 📌 Note

Each folder contains:
- ✅ `lambda_function.py` — The Python Lambda function
- ✅ `README.md` — Full setup instructions and explanation

---

## 📬 Feedback / Contributions

Pull requests and suggestions are welcome. Open an issue if you find a bug or want a new feature.

---

## 🔗 Author

**Animesh Anand**  
DevOps Engineer | AWS | Automation | Python  
[GitHub Profile](https://github.com/animesh-anan-d)

