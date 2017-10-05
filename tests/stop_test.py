import os
from unittest import TestCase
from unittest.mock import Mock, mock_open, patch

from botocore.exceptions import ClientError
from moto import mock_ec2

from light_switch.functions import stop, is_stopped


class TestStopFuncion(TestCase):
    def test_stop_function_should_exit_when_instances_empty(self):
        with self.assertRaises(SystemExit) as cm:
            instances = stop([])

        self.assertEqual(cm.exception.code, 1)

    @patch('light_switch.functions.boto3.client')
    def test_stop_function_should_exit_when_cloud_fails(self, client_mock):
        ec2_mock = Mock()
        ec2_mock.stop_instances.side_effect = ClientError({'Error': {'Code': 'ClientError'}}, 'error')
        client_mock.return_value = ec2_mock

        with self.assertRaises(SystemExit) as cm:
            instances = stop(['i-12345'])

        self.assertEqual(cm.exception.code, 1)

    @patch('light_switch.functions.boto3.client')
    def test_stop_function_should_call_stop_instances(self, client_mock):
        ec2_mock = Mock()
        ec2_mock.stop_instances.return_value = True
        client_mock.return_value = ec2_mock

        stop(['i-12345', 'i-54321'])

        ec2_mock.stop_instances.assert_called_with(InstanceIds=['i-12345', 'i-54321'], DryRun=False)

    def test_is_stopped_function_should_return_false_when_instance_is_running(self):
        instance = {
            'State': {
                'Name': 'running'
            }
        }

        assert is_stopped(instance) == False

    def test_is_stopped_function_should_return_true_when_instance_is_stopped(self):
        instance = {
            'State': {
                'Name': 'stopped'
            }
        }

        assert is_stopped(instance) == True
