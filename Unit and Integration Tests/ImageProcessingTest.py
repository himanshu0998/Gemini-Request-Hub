import requests
import json

url = "http://localhost:5000/auth/signin"

####################################################################### 

print("Case 1: Sign In a user and use the right access token and send a prompt and image")

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

url = "http://localhost:5000/image/process"

payload = {'prompt': 'Describe the image in 50 words'}
files=[
  ('image',('test1',open('test1.jpg','rb'),'application/octet-stream'))
]
headers = {
  'Authorization': f'Bearer {access_tocken}'}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

####################################################################### 
print("Case 2: Send a request without an image")

url = "http://localhost:5000/image/process"

payload = {'prompt': 'Describe the image in 50 words'}
files=[
 
]
headers = {
  'Authorization': f'Bearer {access_tocken}'}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

####################################################################### 

print("Case 3: Send a request without a prompt")

url = "http://localhost:5000/image/process"

payload = {}
files=[
 ('image',('test1',open('test1.jpg','rb'),'application/octet-stream'))
]
headers = {
  'Authorization': f'Bearer {access_tocken}'}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

####################################################################### 