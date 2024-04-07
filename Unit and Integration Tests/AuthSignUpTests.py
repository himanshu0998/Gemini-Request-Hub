import requests
import json

url = "http://localhost:5000/auth/signup"

####################################################################### 

print("Case 1: Test to Create a New User in the database")

payload = json.dumps({
  "username": "testUser101",
  "password": "TestPassword101"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#######################################################################

print("Case 2: Test to Create a Existing User in the database")

payload = json.dumps({
  "username": "testUser1",
  "password": "TestPassword1"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#######################################################################

print("Case 3: Test to Create a New User in the database not matching password requirements:")

payload = json.dumps({
  "username": "testUser10",
  "password": "TestPassword"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#######################################################################