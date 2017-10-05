import json
import os
import sys

import boto3
from botocore.exceptions import ClientError

from light_switch import log


def start(instances_id):
    if not instances_id:
        log.error("Error: Instance ID not informed")
        sys.exit(1)

    ec2 = boto3.client('ec2', region_name=os.environ.get('REGION'))

    log.info('Starting instances {}'.format(instances_id))
    try:
        ec2.start_instances(InstanceIds=instances_id, DryRun=False)
        log.info('Instances started')
    except ClientError as e:
        log.error('Fail to stop instance. Error: {}'.format(e))
        sys.exit(1)


def stop(instances_id):
    if not instances_id:
        log.error("Error: Instance ID not informed")
        sys.exit(1)

    ec2 = boto3.client('ec2', region_name=os.environ.get('REGION'))
    log.info('Stopping instances {}'.format(instances_id))
    try:
        ec2.stop_instances(InstanceIds=instances_id, DryRun=False)
        log.info('Instances stopped')
    except ClientError as e:
        log.error('Fail to stop instance. Error: {}'.format(e))
        sys.exit(1)


def describe():
    instances_id = {}
    with open('instances.json') as data:
        instances_id = json.load(data)
    if not instances_id:
        log.error('Error: Instances not informed')
        sys.exit(1)

    ec2 = boto3.client('ec2', region_name=os.environ.get('REGION'))
    try:
        response = ec2.describe_instances(
                InstanceIds=instances_id, DryRun=False)

        return response.get('Reservations', [])
    except ClientError as e:
        log.error('Fail to describe instances. Error: {}'.format(e))
        sys.exit(1)


def is_stopped(instance):
    return instance.get('State').get('Name') == 'stopped'
