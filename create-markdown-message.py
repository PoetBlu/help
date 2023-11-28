# Fill in this file with the messages code from the Webex Teams exercise
import requests
access_token = N2I1OGVmNzYtZjQ5Yy00NWFmLTk1Y2ItMGQyNjExOTYxYjZiMzBjMDYxMmItMjE1_P0A1_36820416-bfff-433a-84bf-39585b2b3f67
room_id = owner
person_email = cjfoster5@gmail.com
url = 'https://webexapis.com/v1/memberships'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {owner: room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())