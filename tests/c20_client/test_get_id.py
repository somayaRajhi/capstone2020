from os import environ
import requests_mock
from unittest.mock import mock_open
import pytest
from c20_client.get_client_id import request_id, save_client_env_variable, client_has_id

CLIENT_ID = '1234'

def test_request_id_call():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_client_id',
                 json={'client_id': CLIENT_ID})

        client_id = request_id()
        history = mock.request_history

        assert len(history) == 1
        assert 'capstone' in history[0].url
        assert client_id == CLIENT_ID


def test_write_env_variable(mocker):
    file_mock = mocker.patch('c20_client.get_client_id.open', mock_open())
    save_client_env_variable(CLIENT_ID)
    file_mock.assert_called_once_with('.env', 'a+')
    file_mock().write.assert_called_once_with("CLIENT_ID=" + CLIENT_ID + "\n")


def test_id_not_exist_in_env():
    assert not client_has_id()


def test_id_exist_in_environment():
    environ['CLIENT_ID'] = CLIENT_ID
    assert client_has_id()
