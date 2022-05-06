#!/usr/bin/env python3
import json
import os

import requests


testy_mctestface = {
    'first_name': 'Testy',
    'last_name': 'McTestface',
    'email': 'testy@example.com',
    'phone_numbers': [
        '27831231234',
    ],
}


def get_headers():
    username = os.environ['CCHQ_USERNAME']
    api_key = os.environ['CCHQ_API_KEY']
    return {
        'Authorization': f'ApiKey {username}:{api_key}',
        'Content-type': 'application/json',
        'Accept': 'application/json',
    }


def send_request():
    base_url = 'https://www.commcarehq.org'
    domain = 'nhooper'
    user_id = '3c6d579a8abdddd07c033d1725b10735'
    version = 'v0.5'

    # RuntimeError: You called this URL via PUT, but the URL doesn't end
    # in a slash and you have APPEND_SLASH set. Django can't redirect to
    # the slash URL while maintaining PUT data. Change your form to
    # point to .../a/demo/api/v0.5/user/22e9883da9b04c3e90baa7d303da749b/
    # (note the trailing slash), or set APPEND_SLASH=False in your
    # Django settings.
    url = f'{base_url}/a/{domain}/api/{version}/user/{user_id}/'

    resp = requests.put(
        url,
        headers=get_headers(),
        json=testy_mctestface,
    )
    if 200 <= resp.status_code < 300:
        print('OK')
    json_str = json.dumps(resp.json(), indent=2)
    print(json_str)


if __name__ == '__main__':
    send_request()
