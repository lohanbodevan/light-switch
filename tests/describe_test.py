import os
from unittest import TestCase
from unittest.mock import Mock, mock_open, patch

from botocore.exceptions import ClientError
from moto import mock_ec2

from light_switch.functions import describe


class TestDescribeFuncion(TestCase):
    def setUp(self):
        os.environ['REGION'] = 'us-east-2'

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open())
    @patch('light_switch.functions.boto3.client')
    def test_describe_function_should_call_open_function(self, client_mock, file_mock, json_mock):
        instances = describe()

        file_mock.assert_called_with('instances.json')

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open())
    @patch('light_switch.functions.boto3.client')
    def test_describe_function_should_call_json_load_to_convert_file(self, client_mock, file_mock, json_mock):
        instances = describe()

        json_mock.assert_called_with(file_mock.return_value.__enter__.return_value)

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open())
    @patch('light_switch.functions.boto3.client')
    def test_describe_function_should_return_a_list(self, client_mock, file_mock, json_mock):
        reservations = dict(Reservations=[])

        ec2_mock = Mock()
        ec2_mock.describe_instances.return_value = reservations
        client_mock.return_value = ec2_mock

        instances = describe()

        assert type(instances) == list

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open())
    @patch('light_switch.functions.boto3.client')
    def test_describe_function_should_exit_when_cloud_fails(self, client_mock, file_mock, json_mock):
        ec2_mock = Mock()
        ec2_mock.describe_instances.side_effect = ClientError({'Error': {'Code': 'ClientError'}}, 'error')
        client_mock.return_value = ec2_mock

        with self.assertRaises(SystemExit) as cm:
            instances = describe()

        self.assertEqual(cm.exception.code, 1)

    @patch('json.load')
    @patch('builtins.open', new_callable=mock_open())
    @patch('light_switch.functions.boto3.client')
    def test_describe_function_should_exit_when_instances_file_is_empty(self, client_mock, file_mock, json_mock):
        json_mock.return_value = None

        with self.assertRaises(SystemExit) as cm:
            instances = describe()

        self.assertEqual(cm.exception.code, 1)
