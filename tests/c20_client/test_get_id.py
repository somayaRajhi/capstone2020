import requests_mock
from mock import mock_open, patch, MagicMock
import pytest
from c20_client.get_client_id import request_id, client_has_id

CLIENT_ID = 1234

def test_request_id_call():
    with requests_mock.Mocker() as mock:
        mock.get('http://capstone.cs.moravian.edu/get_client_id',
                 json={'client_id': CLIENT_ID})

        client_id = request_id()
        history = mock.request_history

        assert len(history) == 1
        assert 'capstone' in history[0].url
        assert client_id == CLIENT_ID
