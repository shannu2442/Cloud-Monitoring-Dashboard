# Cloud Monitoring Dashboard
## Name:Kotla Shanmukha Rao
## CodTech Intern ID: CITS812

## Overview

Cloud Monitoring Dashboard is a web-based monitoring system developed using Flask, SQLite, Bootstrap, Chart.js, and AWS CloudWatch. The application provides real-time monitoring of cloud resources, alert generation, historical data tracking, and performance reporting through an interactive dashboard.

This project was developed as part of an internship to demonstrate cloud monitoring concepts and web application development using Python and AWS services.

---

## Features

### Authentication

* Secure Login System
* Session Management
* Logout Functionality

### Dashboard

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* Network Traffic Monitoring
* Resource Usage Visualization using Charts

### Alerts

* Automatic Alert Generation
* CPU Threshold Monitoring
* Memory Threshold Monitoring
* Disk Usage Monitoring
* Alert History Tracking

### Monitoring History

* Store Resource Usage Records
* View Historical Monitoring Data
* Search Monitoring Records
* Delete Records

### Reports

* Average Resource Utilization
* Resource Usage Analysis
* CSV Export Functionality

### AWS Integration

* AWS CloudWatch Connectivity
* EC2 Monitoring
* Real-Time Metric Collection

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Chart.js

### Backend

* Python
* Flask

### Database

* SQLite

### Cloud Services

* AWS EC2
* AWS CloudWatch
* AWS IAM
* Boto3 SDK

---

## Project Structure

```text
CloudMonitoringDashboard/
│
├── app.py
├── config.py
├── database.py
├── cloudwatch.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── history.html
│   ├── alerts.html
│   └── reports.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── charts.js
│   │
│   └── images/
│
└── database.db
```

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/cloud-monitoring-dashboard.git
cd cloud-monitoring-dashboard
```

### Step 2: Install Required Packages

```bash
pip install flask
pip install boto3
pip install pandas
pip install matplotlib
```

Or:

```bash
pip install -r requirements.txt
```

### Step 3: Create Database

```bash
python database.py
```

Expected Output:

```text
Database Created Successfully
```

### Step 4: Configure AWS Credentials

Open `config.py`

```python
SECRET_KEY = "cloud_dashboard_secret"

AWS_REGION = "ap-south-1"

AWS_ACCESS_KEY = "YOUR_ACCESS_KEY"

AWS_SECRET_KEY = "YOUR_SECRET_KEY"

DATABASE = "database.db"
```

Replace:

```text
YOUR_ACCESS_KEY
YOUR_SECRET_KEY
```

with your IAM Access Key and Secret Key.

### Step 5: Run Application

```bash
python app.py
```

### Step 6: Open Browser

```text
http://127.0.0.1:5000
```

---

## Login Credentials

```text
Username : admin
Password : admin123
```

---

## Database Tables

### Users Table

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| password | TEXT    |

### Metrics Table

| Field     | Type     |
| --------- | -------- |
| id        | INTEGER  |
| cpu       | REAL     |
| memory    | REAL     |
| disk      | REAL     |
| network   | REAL     |
| timestamp | DATETIME |

### Alerts Table

| Field      | Type     |
| ---------- | -------- |
| id         | INTEGER  |
| message    | TEXT     |
| severity   | TEXT     |
| created_at | DATETIME |

---

## AWS Configuration

### Services Used

* Amazon EC2
* Amazon CloudWatch
* AWS IAM

### IAM Policy Required

```text
CloudWatchReadOnlyAccess
```

### EC2 Instance

The application monitors an EC2 instance and retrieves performance metrics using AWS CloudWatch APIs.

---

## Screenshots

### Login Page

* User Authentication Interface

### Dashboard

* CPU Monitoring
* Memory Monitoring
* Disk Monitoring
* Network Monitoring

### Alerts Page

* Alert History
* Resource Warning Messages

### History Page

* Monitoring Records
* Search Functionality

### Reports Page

* Resource Utilization Reports
* Average Usage Statistics

---

## Future Enhancements

* Email Notifications
* SMS Alerts
* Docker Monitoring
* Kubernetes Monitoring
* Multi-Cloud Monitoring
* AI-Based Resource Prediction
* PDF Report Generation
* Dark Mode Interface

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* Cloud Computing Fundamentals
* AWS Cloud Services
* AWS CloudWatch Monitoring
* Flask Web Development
* Database Management using SQLite
* Data Visualization using Chart.js
* Cloud Resource Monitoring
* Alert Management Systems

---

## Conclusion

The Cloud Monitoring Dashboard successfully provides a centralized platform for monitoring cloud resources, generating alerts, maintaining historical records, and analyzing system performance. The project demonstrates practical implementation of cloud monitoring concepts using AWS services and Python-based web technologies.

---

## Author

Internship Project

Cloud Monitoring Dashboard Using Flask and AWS CloudWatch

Developed using Python, Flask, SQLite, Bootstrap, Chart.js, and AWS Cloud Services.# Cloud-Monitoring-Dashboard
