from light_switch import log
from light_switch.functions import (
    describe_instances,
    stop_instances,
    start_instances,
    is_stopped
)


def handler(event, context):
    for reservation in response.get('Reservations'):
        to_start = list(filter(lambda i: is_stopped(i), reservation))
        to_stop = list(filter(lambda i: not is_stopped(i), reservation))

    log.info('Instances to Stop {}'.format(to_stop))
    log.info('Instances to Start {}'.format(to_start))

    if to_start:
        start_instances(to_start)

    if to_stop:
        stop_instances(to_stop)
