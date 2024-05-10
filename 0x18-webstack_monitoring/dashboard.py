#!/usr/bin/python3

import requests

# Set up your Datadog API credentials
api_key = '7e1ede40da87a575e68156e9b80833bc'
app_key = '4ed1e4dc131f6c3c78e45fd3b63cf4f3fae7f81f'

# Make the API request to list dashboards
url = 'https://api.datadoghq.com/api/v1/dashboard'
headers = {'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': app_key}
response = requests.get(url, headers=headers)

# Parse the response to find the dashboard ID
dashboards = response.json()['dashboards']
for dashboard in dashboards:
    print(f"Dashboard Name: {dashboard['title']}, ID: {dashboard['id']}")