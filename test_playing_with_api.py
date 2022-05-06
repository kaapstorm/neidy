import os
from contextlib import contextmanager

from playing_with_api import get_headers


def test_get_headers():
    with get_environ():
        headers = get_headers()
        expected = {
            'Authorization': 'ApiKey test@example.com:abc123'
        }
        assert headers == expected


@contextmanager
def get_environ():
    username = os.environ['CCHQ_USERNAME']
    api_key = os.environ['CCHQ_API_KEY']

    os.environ['CCHQ_USERNAME'] = 'test@example.com'
    os.environ['CCHQ_API_KEY'] = 'abc123'
    try:
        yield
    finally:
        os.environ['CCHQ_USERNAME'] = username
        os.environ['CCHQ_API_KEY'] = api_key
