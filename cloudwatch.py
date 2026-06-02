import boto3
from datetime import datetime, timedelta
from config import *

INSTANCE_ID = "i-0d66701ed9275ebef"

cloudwatch = boto3.client(
    'cloudwatch',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def get_cpu_utilization():

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=30)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',

        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': INSTANCE_ID
            }
        ],

        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )

    datapoints = response['Datapoints']

    if datapoints:
        return round(datapoints[-1]['Average'], 2)

    return 0


def get_metrics():

    cpu = get_cpu_utilization()

    return {
        "cpu": cpu,
        "memory": 60,
        "disk": 40,
        "network": 120
    }