from light_switch import log
from light_switch.functions import (
    describe,
    stop,
    start,
    is_stopped
)


def handler(event, context):
    to_start = []
    to_stop = []

    for reservation in describe():
        stopped = filter(lambda i: is_stopped(i), reservation.get('Instances'))
        to_start += list(map(lambda i: i.get('InstanceId'), stopped))

        started = filter(lambda i: not is_stopped(i), reservation.get('Instances'))
        to_stop += list(map(lambda i: i.get('InstanceId'), started))

    if to_start:
        start(to_start)

    if to_stop:
        stop(to_stop)
