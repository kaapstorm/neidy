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


def send_request():
    domain = 'nhooper'
    version = 'v0.5'
    user_id = '3c6d579a8abdddd07c033d1725b10735'

    username = os.environ['CCHQ_USERNAME']
    api_key = os.environ['CCHQ_API_KEY']
    headers = {
        'Authorization': f'ApiKey {username}:{api_key}'
    }
    url = f'https://www.commcarehq.org/a/{domain}/api/{version}/user/{user_id}'

    resp = requests.put(
        url,
        headers=headers,
        data=json.dumps(testy_mctestface),
    )
    if 200 <= resp.status_code < 300:
        print('OK')
    pprint(resp.json())


if __name__ == '__main__':
    send_request()
