# 📦 Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

## 🎯 Objective
Detect S3 buckets that do not have server-side encryption (SSE) enabled using a Lambda function with Boto3.

---

## 🪜 Steps Followed

### ✅ 1. S3 Buckets Created
- `unencrypted-bucket-01` (no SSE)
- `unencrypted-bucket-02` (no SSE)
- `encrypted-bucket-01` (SSE-S3 enabled)

### ✅ 2. IAM Role
- Created `lambda-s3-readonly-role`
- Attached `AmazonS3ReadOnlyAccess` policy

### ✅ 3. Lambda Function
- Runtime: Python 3.x
- Code checks S3 buckets using Boto3
- Prints list of buckets without SSE

### ✅ 4. Testing
- Lambda manually triggered
- Console logs confirm detection of unencrypted buckets

---

## 🧾 Screenshots



![Screenshot 2025-06-14 182457](https://github.com/user-attachments/assets/18cc31bf-c0f1-4452-9538-6740baf0955b)
![Screenshot 2025-06-14 182449](https://github.com/user-attachments/assets/3bd717d5-0cc1-4689-bb41-c42b57a0297e)
![Screenshot 2025-06-14 182429](https://github.com/user-attachments/assets/16f270b6-8091-4d3c-8e3a-542ac838132f)
![Screenshot 2025-06-14 182429](https://github.com/user-attachments/assets/a19b59cc-3e86-4edb-b981-c9f006c0198b)
![Screenshot 2025-06-14 182409](https://github.com/user-attachments/assets/6f49337b-4f22-40be-9192-f990be5f6cd6)
![Screenshot 2025-06-14 182046](https://github.com/user-attachments/assets/f2ec71f0-aedc-447c-ad6c-6c909f76a9bb)
![Screenshot 2025-06-14 181646](https://github.com/user-attachments/assets/250551c9-e7c4-4bef-bf3d-1bc9f5f3c7a6)
