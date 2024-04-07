import requests
import json

url = "http://localhost:5000/auth/signin"

####################################################################### 

print("Case 1: Test to Sign In an existing user in the database")

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

print("Case 2: Test to Sign In a non-existing user in the database")

payload = json.dumps({
  "username": "testUser102",
  "password": "TestPassword102"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

####################################################################### 

print("Case 3: Test to Sign In an existing user with a wrong password in the database")

payload = json.dumps({
  "username": "testUser1",
  "password": "TestPassword2"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

####################################################################### 