import requests
import json

url = "http://localhost:5000/auth/signin"

####################################################################### 

print("Case 1: Sign In a user and use the right access token to send a prompt")

payload = json.dumps({
  "username": "testUser1",
  "password": "TestPassword1"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

access_tocken = response.json()["access_token"]

print("User signed In with access token: ", access_tocken)


url = "http://localhost:5000/text/prompt"

payload = json.dumps({
  "prompt": "Best soccer player? Give me 3 names"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_tocken}'}


response = requests.request("POST", url, headers=headers, data=payload)

print("User Prompt: Best soccer player? Give me 3 names")
print(response.text)

####################################################################### 

print("Case 2: Sign In a user and use the incorrect access token to send a prompt")

access_tocken2 = access_tocken + 'aSDFGHJGGDFSASDFGH'
print("Incorrect access token: ", access_tocken2)

url = "http://localhost:5000/text/prompt"

payload = json.dumps({
  "prompt": "Best soccer player? Give me 3 names"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_tocken2}'}


response = requests.request("POST", url, headers=headers, data=payload)

print("User Prompt: Best soccer player? Give me 3 names")
print(response.text)

####################################################################### 

print("Case 3: Sign In a user and send a request without any prompt")

url = "http://localhost:5000/text/prompt"

payload = json.dumps({
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_tocken}'}


response = requests.request("POST", url, headers=headers, data=payload)

print("User Prompt: None")
print(response.text)

####################################################################### 