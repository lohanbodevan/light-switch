import json
import os
import sys

import boto3
from botocore.exceptions import ClientError

from light_switch import log


def start_ec2(instances_id):
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


def stop_ec2(instances_id):
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


def describe_ec2():
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


def start_rds(instances_id):
    if not instances_id:
        log.error("Error: RDS instances not informed")
        sys.exit(1)

    rds = boto3.client('rds', region_name=os.environ.get('REGION'))

    log.info('Starting RDS instances {}'.format(instances_id))
    for id in instances_id:
        try:
            rds.start_db_instance(DBInstanceIdentifier=id)
            log.info('RDS Instances started')
        except ClientError as e:
            print('Fail to stop RDS instance. Error: {}'.format(e))
            sys.exit(1)


def is_stopped(instance):
    return instance.get('State').get('Name') == 'stopped'


def stop_rds(instances_id):
    if not instances_id:
        log.error("Error: RDS Instance ID not informed")
        sys.exit(1)

    rds = boto3.client('rds', region_name=os.environ.get('REGION'))
    log.info('Stopping rds instances {}'.format(instances_id))

    for id in instances_id:
        try:
            rds.stop_db_instance(DBInstanceIdentifier=id)
            log.info('RDS Instances stopped')
        except ClientError as e:
            print('RDS Fail to stop instance. Error: {}'.format(e))
            sys.exit(1)


def describe_rds():
    instances_id = {}
    with open('rds_instances.json') as data:
        instances_id = json.load(data)
    if not instances_id:
        log.error('Error: RDS Instance ID not informed')
        sys.exit(1)

    rds = boto3.client('rds', region_name=os.environ.get('REGION'))
    instances = []
    for id in instances_id:
        try:
            response = rds.describe_db_instances(
                    DBInstanceIdentifier=id)
            instances.append(response.get('DBInstances')[0])
        except ClientError as e:
            print('Fail to describe RDS instances. Error: {}'.format(e))
            sys.exit(1)

    return instances


def is_rds_stopped(instance):
    return instance.get('DBInstanceStatus') == 'stopped'
