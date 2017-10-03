from unittest import TestCase

from moto import mock_ec2

from light_switch import describe_instances


class TestInstancesFuncions(TestCase):
    @mock_ec2
    def test_describe_instances_should_return_a_list():
        instances = describe_instances()
        assert len(instances['Reservations'][0]['Instances']) == 2
