import requests
import json

url = "http://localhost:5000/auth/signup"

####################################################################### 

print("Case 1: Test to Create a New User in the database")

payload = json.dumps({
  "username": "testUser1",
  "password": "TestPassword1",
  "emailId": "testUser@abc.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print("Request Payload:\n", payload)
print("Response:\n",response.text)

#######################################################################

print("Case 2: Test to Create a Existing User in the database")

payload = json.dumps({
  "username": "testUser1",
  "password": "TestPassword1",
  "emailId": "testUser@abc.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("Request Payload:\n", payload)
print("Response:\n",response.text)

#######################################################################

print("Case 3: Test to Create a New User in the database not matching password requirements:")

payload = json.dumps({
  "username": "testUser10",
  "password": "TestPassword",
  "emailId": "testUser@abc.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print("Request Payload:\n", payload)
print("Response:\n",response.text)

#######################################################################

print("Case 4: Test to Create a New User in the database not matching emailID requirements:")

payload = json.dumps({
  "username": "testUser10",
  "password": "TestPassword",
  "emailId": "testUserabc.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print("Request Payload:\n", payload)
print("Response:\n",response.text)

#######################################################################

print("Case 5: Test to Create a New User in the database withoout providing email Id")

payload = json.dumps({
  "username": "testUser15",
  "password": "TestPassword15"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("Request Payload:\n", payload)
print("Response:\n",response.text)