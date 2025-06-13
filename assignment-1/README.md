# Assignment 1: Automated EC2 Instance Start/Stop Using AWS Lambda & Boto3

## 📌 Objective

Automatically **start or stop EC2 instances** based on their **tag values** using AWS Lambda and the Boto3 Python SDK.

---

## 🧠 Problem Statement

You are required to write a Lambda function that:

- Finds all EC2 instances with the tag `Action=Auto-Stop` and **stops** them.
- Finds all EC2 instances with the tag `Action=Auto-Start` and **starts** them.

---

## 🔧 Setup Instructions

### 1. EC2 Instance Setup

- Go to the **EC2 Dashboard** and create **two EC2 instances** (e.g., `t2.micro`).
- While creating the instances, add the following tags:

| Key    | Value       | Purpose              |
|--------|-------------|----------------------|
| Action | Auto-Stop   | To stop the instance |
| Action | Auto-Start  | To start the instance |

---

### 2. IAM Role for Lambda

- Navigate to **IAM > Roles**.
- Create a new role for **AWS Lambda**.
- Attach the **AmazonEC2FullAccess** policy.
  > 🔒 *Note: In real-world production, use least privilege permissions.*

---

### 3. Lambda Function Setup

- Go to **AWS Lambda Console**.
- Click **Create Function** > Author from scratch.
- Name: `ec2-auto-start-stop`
- Runtime: **Python 3.x**
- Execution Role: Choose the IAM role created above.
- Click **Create Function**.




### 4. Output

Stopped Instances: ['i-0123456789abcdef0']
Started Instances: ['i-0abcdef0123456789']



### 5. Screenshots

![Screenshot 2025-06-13 204459](https://github.com/user-attachments/assets/1f6d6e50-6470-41c2-9450-52e8![Screenshot 2025-06-13 204904](https://github.com/user-attachments/assets/0548fdf5-3559-4e38-8397-8a623f2a6007)
e045693e)
![Screenshot 2025-06-13 205118](https://github.com/user-attachments/assets/a041f433-cc0e-4788-9622-87857dc90c9![Screenshot 2025-06-13 205325](https://github.com/user-attachments/assets/42f80ce8-f0d6-4e70-9652-f16e8e63f9c1)
0)
![Screenshot 2025-06-13 210725](https://github.com/user-attachments/assets/56ea5e9b-9c5a-4e76-abc0-e569ce4fa985)

![Screenshot 2025-06-13 211130](https://github.com/user-attachments/assets/2463693f-4d25-4845-bce5-d905f2c7b76a)
![Screenshot 2025-06-13 211805](https://github.com/user-attachments/assets/b7c50f8a-49b4-4585-a5a6-562968a077af)
