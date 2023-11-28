# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = N2I1OGVmNzYtZjQ5Yy00NWFmLTk1Y2ItMGQyNjExOTYxYjZiMzBjMDYxMmItMjE1_P0A1_36820416-bfff-433a-84bf-39585b2b3f67
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
params = {
    'email': cjfoster5@gmail.com

}

person_id = Y2l
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))