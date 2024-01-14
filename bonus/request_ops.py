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