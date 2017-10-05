import os
from unittest import TestCase
from unittest.mock import Mock, mock_open, patch

from botocore.exceptions import ClientError
from moto import mock_ec2

from light_switch.functions import start


class TestStartFuncion(TestCase):
    def test_start_function_should_exit_when_instances_empty(self):
        with self.assertRaises(SystemExit) as cm:
            instances = start([])

        self.assertEqual(cm.exception.code, 1)

    @patch('light_switch.functions.boto3.client')
    def test_start_function_should_exit_when_cloud_fails(self, client_mock):
        ec2_mock = Mock()
        ec2_mock.start_instances.side_effect = ClientError({'Error': {'Code': 'ClientError'}}, 'error')
        client_mock.return_value = ec2_mock

        with self.assertRaises(SystemExit) as cm:
            instances = start(['i-12345'])

        self.assertEqual(cm.exception.code, 1)

    @patch('light_switch.functions.boto3.client')
    def test_start_function_should_call_start_instances(self, client_mock):
        ec2_mock = Mock()
        ec2_mock.start_instances.return_value = True
        client_mock.return_value = ec2_mock

        start(['i-12345', 'i-54321'])

        ec2_mock.start_instances.assert_called_with(InstanceIds=['i-12345', 'i-54321'], DryRun=False)
