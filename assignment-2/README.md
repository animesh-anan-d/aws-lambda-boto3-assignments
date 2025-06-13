# Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## 📌 Objective
To gain hands-on experience with AWS Lambda and Boto3 by creating a Python-based Lambda function that automatically deletes files older than 30 days from an S3 bucket.

---

## 🛠️ Tech Stack
- **AWS Lambda** (Python 3.x runtime)
- **Amazon S3**
- **IAM Roles & Policies**
- **Boto3** (AWS SDK for Python)

---

## 📁 Use Case
Automatically clean up old files from an S3 bucket to:
- Save storage costs
- Maintain hygiene in file storage
- Automate lifecycle management without manual intervention

---

## 📋 Task Overview

- ✅ Create an S3 bucket
- ✅ Upload multiple files (simulating old & new uploads)
- ✅ Create IAM Role with `AmazonS3FullAccess` policy
- ✅ Write a Lambda function in Python using Boto3
- ✅ Manually trigger the function to test deletion logic
- ✅ Print deleted object names for logging

---

## 🧾 Step-by-Step Guide

### 1️⃣ S3 Bucket Setup

- Go to AWS Console > **S3**
- Create a new bucket (e.g., `s3-cleanup-assignment2`)
- Upload multiple files into the bucket  
  - (You can simulate "old" files by changing the system date before upload or using versioning)

---

### 2️⃣ IAM Role for Lambda

- Go to **IAM > Roles > Create role**
- Choose **Lambda** as trusted entity
- Attach policy: ✅ `AmazonS3FullAccess`
- Give a role name: e.g., `lambda-s3-cleanup-role`
- Finish creation

---

### 3️⃣ Lambda Function Setup

- Go to **AWS Lambda > Create function**
- Runtime: **Python 3.x**
- Assign the IAM role created above
- Paste the following code: