import requests
import json

url = "http://localhost:5000/auth/signin"

####################################################################### 

print("Case 1: Sign In an existing user in the database and the logout")

payload = json.dumps({
  "username": "testUser1",
  "password": "TestPassword1"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

access_token = response.json()["access_token"]

print("Access Token: ", access_token)

url = "http://localhost:5000/auth/logout"

payload = {}
headers = {
  'Authorization': f'Bearer {access_token}'
  }

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

####################################################################### 

print("Case 2: Attemp to log out with an incorrect access token")

access_token = access_token + "Abdehfjdsghvbfcd"

print("Access Token: ", access_token)

url = "http://localhost:5000/auth/logout"

payload = {}
headers = {
  'Authorization': f'Bearer {access_token}'
  }

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

####################################################################### 