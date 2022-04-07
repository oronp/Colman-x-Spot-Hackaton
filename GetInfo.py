from datetime import datetime, timedelta

import boto3


def getInsType():
    client = boto3.client('ec2')
    Myec2 = client.describe_instances()
    for pythonins in Myec2['Reservations']:
        for printout in pythonins['Instances']:
            return printout['InstanceType']

def checkIfGP2():
    client = boto3.client('ec2', region_name="us-east-1")
    response = client.describe_volumes()

    if response["Volumes"][0]['VolumeType'] == 'gp2':
        userChoice = input(
            "You can save up to 20% on EBS costs with moving to gp3, would you like to switch now to gp3? Y / N")
        if userChoice == 'Y':
            client.modify_volume(VolumeId='vol-05865009ece0ecd71', VolumeType='gp3')
            print("Changed Successfully")
    else:
        print('Your EBS cost is already optimized')


# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name="us-east-1")


def getCpuUtilizationAverages():
    dict = {}
    response2 = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-0c1109f3a47d5f5b6'
            },
        ],
        StartTime=datetime(2022, 4, 2) - timedelta(seconds=600),
        EndTime=datetime(2022, 4, 4),
        Period=1800,
        Statistics=[
            'Average'
        ]
    )

    for i in range(len(response2['Datapoints'])):
        dict.update({response2['Datapoints'][i]['Timestamp'].strftime('%Y/%m/%d %H:%M:%S'): response2['Datapoints'][i][
            'Average']})

    return dict


def getCpuUtilizationMax():
    dict = {}
    response2 = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-0c1109f3a47d5f5b6'
            },
        ],
        StartTime=datetime(2022, 4, 2) - timedelta(seconds=600),
        EndTime=datetime(2022, 4, 4),
        Period=1800,
        Statistics=[
            'Maximum'
        ]
    )

    for i in range(len(response2['Datapoints'])):
        dict.update({response2['Datapoints'][i]['Timestamp'].strftime('%Y/%m/%d %H:%M:%S'): response2['Datapoints'][i][
            'Maximum']})

    return dict


def getMemUtilizationMax():
    dict = {}
    response2 = cloudwatch.get_metric_statistics(
        Namespace='CWAgent',
        MetricName='mem_used_percent',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-0c1109f3a47d5f5b6'
            },
        ],
        StartTime=datetime(2022, 4, 2) - timedelta(seconds=600),
        EndTime=datetime(2022, 4, 4),
        Period=1800,
        Statistics=[
            'Maximum'
        ]
    )

    for i in range(len(response2['Datapoints'])):
        dict.update({response2['Datapoints'][i]['Timestamp'].strftime('%Y/%m/%d %H:%M:%S'): response2['Datapoints'][i][
            'Maximum']})

    return dict


def getMemUtilizationAverages():
    dict = {}
    response2 = cloudwatch.get_metric_statistics(
        Namespace='CWAgent',
        MetricName='mem_used_percent',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-0c1109f3a47d5f5b6'
            },
        ],
        StartTime=datetime(2022, 4, 2) - timedelta(seconds=600),
        EndTime=datetime(2022, 4, 4),
        Period=1800,
        Statistics=[
            'Average'
        ]
    )

    for i in range(len(response2['Datapoints'])):
        dict.update({response2['Datapoints'][i]['Timestamp'].strftime('%Y/%m/%d %H:%M:%S'): response2['Datapoints'][i][
            'Average']})

    return dict


def getNetworkUtilizationMax():
    dict = {}
    response2 = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='NetworkOut',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-0c1109f3a47d5f5b6'
            },
        ],
        StartTime=datetime(2022, 4, 2) - timedelta(seconds=600),
        EndTime=datetime(2022, 4, 4),
        Period=1800,
        Statistics=[
            'Maximum'
        ]
    )

    for i in range(len(response2['Datapoints'])):
        dict.update({response2['Datapoints'][i]['Timestamp'].strftime('%Y/%m/%d %H:%M:%S'): response2['Datapoints'][i][
            'Maximum']})

    return dict


def getNetworkUtilizationAverages():
    dict = {}
    response2 = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='NetworkOut',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-0c1109f3a47d5f5b6'
            },
        ],
        StartTime=datetime(2022, 4, 2) - timedelta(seconds=600),
        EndTime=datetime(2022, 4, 4),
        Period=1800,
        Statistics=[
            'Average'
        ]
    )

    for i in range(len(response2['Datapoints'])):
        dict.update({response2['Datapoints'][i]['Timestamp'].strftime('%Y/%m/%d %H:%M:%S'): response2['Datapoints'][i][
            'Average']})

    return dict


averageCpuUtilizationDict = getCpuUtilizationAverages()
maxCpuUtilizationDict = getCpuUtilizationMax()
maxMemUtilizationDict = getMemUtilizationMax()
averageMemUtilizationDict = getMemUtilizationAverages()
maxNetworkUtilizationDict = getNetworkUtilizationMax()
averageNetworkUtilizationDict = getNetworkUtilizationAverages()
