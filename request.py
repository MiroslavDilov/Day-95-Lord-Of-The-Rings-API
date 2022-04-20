import requests

url = 'https://the-one-api.dev/v2/'

access_token = '-7Vs34BzKVUSZL-nv4t4'

headers = {
    'Authorization': f'Bearer {access_token}'
}


def api_request(choice_route):
    route = choice_route
    response = requests.get(url+route, headers=headers)
    return response.json()
