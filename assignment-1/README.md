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



![Screenshot 2025-06-13 204459](https://github.com/user-attachments/assets/6f0a6bec-438d-4e9e-aeaf-5068e87ad49d)

### 4. Output

Stopped Instances: ['i-0123456789abcdef0']
Started Instances: ['i-0abcdef0123456789']



### 5. Screenshots
![Screenshot 2025-06-13 205118](https://github.com/user-attachments/assets/3d47861f-16f7-4fb0-8b6d-a0df27ae43b7)

![Screenshot 2025-06-13 211805](https://github.com/user-attachments/assets/41fe0728-e16b-4199-b2d8-8a3cf424e0eb)
![Screenshot 2025-06-13 204904](https![Uploading Screenshot 2025-06-13 211805.png…]()
://github.com/user-attachments/assets/cf710c4e-1ef4-4a2f-bd27-a96b4ecb3b63)
![Screenshot 2025-06-13 210725](https://github.com/user-attachments/assets/8af2f6f2-1906-412e-9608-1d370d114230)
