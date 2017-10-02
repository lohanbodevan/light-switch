import json
import os
import sys

import boto3
from botocore.exceptions import ClientError

from light_switch import log


def start_instances(instances_id):
    if not instances_id:
        log.error("Error: Instance ID not informed")
        sys.exit(1)

    log.info('Starting instances {}'.format(instances_id))
    try:
        ec2 = boto3.client(
                'ec2',
                aws_access_key_id=os.environ.get('ACCESS_KEY'),
                aws_secret_access_key=os.environ.get('ACCESS_SECRET'),
                region_name=os.environ.get('REGION'))
        ec2.start_instances(InstanceIds=instances_id, DryRun=False)
        log.info('Instances started')
    except ClientError as e:
        log.error('Fail to stop instance. Error: '.format(e))
        sys.exit(1)


def stop_instances(instances_id):
    if not instances_id:
        print("Error: Instance ID not informed")
        sys.exit(1)

    log.info('Stopping instances {}'.format(instances_id))
    try:
        ec2 = boto3.client(
                'ec2',
                aws_access_key_id=os.environ.get('ACCESS_KEY'),
                aws_secret_access_key=os.environ.get('ACCESS_SECRET'),
                region_name=os.environ.get('REGION'))
        ec2.stop_instances(InstanceIds=instances_id, DryRun=False)
        log.info('Instances stopped')
    except ClientError as e:
        log.error('Fail to stop instance. Error: '.format(e))
        sys.exit(1)


def describe_instances():
    instances_id = {}
    with open('instances.json') as data:
        instances_id = json.load(data)
    if not instances_id:
        log.error('Error: Instances not informed')
        sys.exit(1)

    try:
        ec2 = boto3.client(
                'ec2',
                aws_access_key_id=os.environ.get('ACCESS_KEY'),
                aws_secret_access_key=os.environ.get('ACCESS_SECRET'),
                region_name=os.environ.get('REGION'))
        return ec2.describe_instances(InstanceIds=instances_id, DryRun=False)
    except ClientError as e:
        log.error('Fail to describe instances. Error: '.format(e))
        sys.exit(1)


def is_stopped(instance):
    return instance.get('State').get('Name') == 'stopped'


if __name__ == "__main__":
    response = describe_instances()
    for res in response.get('Reservations'):
        to_start = [i.get('InstanceId') for i in res.get('Instances') if is_stopped(i)]
        to_stop = [i.get('InstanceId') for i in res.get('Instances') if not is_stopped(i)]

    log.info('Instances to Stop {}'.format(to_stop))
    log.info('Instances to Start {}'.format(to_start))

    if to_start:
        start_instances(to_start)

    if to_stop:
        stop_instances(to_stop)
