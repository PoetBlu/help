# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests
access_token = N2I1OGVmNzYtZjQ5Yy00NWFmLTk1Y2ItMGQyNjExOTYxYjZiMzBjMDYxMmItMjE1_P0A1_36820416-bfff-433a-84bf-39585b2b3f67
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())