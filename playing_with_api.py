#!/usr/bin/env python3
import json
import os
from pprint import pprint

import requests


testy_mctestface = {
    'first_name': 'Testy-One-Two-Three',
    'last_name': 'McTestface',
    'email': 'testy@example.com',
    'groups': [],
    'phone_numbers': [
        '+27837596738',
    ],
    'user_data': {
        'commcare_location_id': 'b5b03ec28e6f4deca9de2998c7a31d05',
        'commcare_location_ids': 'b5b03ec28e6f4deca9de2998c7a31d05',
        'commcare_primary_case_sharing_id': 'b5b03ec28e6f4deca9de2998c7a31d05',
        'commcare_project': 'nhooper',
    },
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
    domain = 'nhooper'
    version = 'v0.5'
    user_id = '3c6d579a8abdddd07c033d1725b10735'

    # RuntimeError: You called this URL via PUT, but the URL doesn't end
    # in a slash and you have APPEND_SLASH set. Django can't redirect to
    # the slash URL while maintaining PUT data. Change your form to
    # point to .../a/demo/api/v0.5/user/22e9883da9b04c3e90baa7d303da749b/
    # (note the trailing slash), or set APPEND_SLASH=False in your
    # Django settings.
    url = f'https://www.commcarehq.org/a/{domain}/api/{version}/user/{user_id}/'

    resp = requests.put(
        url,
        headers=get_headers(),
        json=testy_mctestface,
    )
    if 200 <= resp.status_code < 300:
        print('OK')
    pprint(resp.json())


if __name__ == '__main__':
    send_request()
