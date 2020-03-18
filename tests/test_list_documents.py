
import pytest
import requests_mock
from c20_server import list_documents
from c20_server import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/document.json?"
API_KEY = "12345"


