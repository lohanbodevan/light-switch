from light_switch import log
from light_switch.functions import (
    describe_ec2,
    stop_ec2,
    start_ec2,
    is_stopped,
    describe_rds,
    stop_rds,
    start_rds,
    is_rds_stopped
)


def handler(event, context):
    ec2_to_start = []
    ec2_to_stop = []

    for reservation in describe_ec2():
        stopped = filter(lambda i: is_stopped(i), reservation.get('Instances'))
        ec2_to_start += list(map(lambda i: i.get('InstanceId'), stopped))

        started = filter(lambda i: not is_stopped(i), reservation.get('Instances'))
        ec2_to_stop += list(map(lambda i: i.get('InstanceId'), started))

    if ec2_to_start:
        start_ec2(ec2_to_start)

    if ec2_to_stop:
        stop_ec2(ec2_to_stop)

    rds_to_start = []
    rds_to_stop = []

    for reservation in describe_rds():
        if is_rds_stopped(reservation):
            rds_to_start.append(reservation.get('DBInstanceIdentifier'))
        else:
            rds_to_stop.append(reservation.get('DBInstanceIdentifier'))

    if rds_to_start:
        start_rds(rds_to_start)

    if rds_to_stop:
        stop_rds(rds_to_stop)


if __name__ == '__main__':
    handler(None, None)
