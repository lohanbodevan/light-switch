from light_switch import log
from light_switch.functions import (
    describe,
    stop,
    start,
    is_stopped
)


def handler(event, context):
    to_start = None
    to_stop = None

    for reservation in describe():
        to_start = list(filter(lambda i: is_stopped(i), reservation))
        to_stop = list(filter(lambda i: not is_stopped(i), reservation))

    log.info('Instances to Stop {}'.format(to_stop))
    log.info('Instances to Start {}'.format(to_start))

    if to_start:
        start(to_start)

    if to_stop:
        stop(to_stop)
