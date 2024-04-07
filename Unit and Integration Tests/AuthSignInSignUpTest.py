import requests
import json

url = "http://localhost:5000/auth/signup"

####################################################################### 

print("Sign Up a New User\n")

payload = json.dumps({
  "username": "testUser102",
  "password": "TestPassword102"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "http://localhost:5000/auth/signin"

####################################################################### 

print("Use the credentials of the users registered above to sign in")

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