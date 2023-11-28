# Fill in this file with the code to get room details from the Webex Teams exercise
access_token = N2I1OGVmNzYtZjQ5Yy00NWFmLTk1Y2ItMGQyNjExOTYxYjZiMzBjMDYxMmItMjE1_P0A1_36820416-bfff-433a-84bf-39585b2b3f67
room_id = owner
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())