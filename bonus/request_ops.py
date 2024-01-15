import requests

url = 'https://www.google.com/search?q=pytest'
r = requests.get(url)
#print(r.text)

url = 'https://reqres.in/api/users'
r = requests.get (url)
print(r.cookies)
print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)
print(r.headers['Content-Type'])
print(r.json())
print('--------------------------------------')



url = 'https://httpbin.org/get'
myparams = {'key1': 'value', 'key2': 'value2'}
r = requests.get(url, params=myparams)
print(r.url)

for key, value in r.json().items():
    print (key, " : ",value)

print(r.json()['headers']['Host'])
print('--------------------------------------')

url = 'https://httpbin.org/post'
payload = {'key1': 'value', 'key2': 'value2'}
r = requests.post(url, json=payload)
print(r.url)
print(r.status_code)
print(r.text)

print('--------------------------------------')
url = 'https://httpbin.org/post'
payload = {'key1': 'value', 'key2': 'value2'}
r = requests.post(url, headers={'accept':'form-data'}, data=payload)
print(r.url)
print(r.status_code)
print(r.text)
