from light_switch import log
from light_switch.functions import (
    describe_instances,
    stop_instances,
    start_instances,
    is_stopped
)


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
