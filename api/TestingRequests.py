import requests

response = requests.get("http://dummy.restapiexample.com/api/v1/employees")

if response.status_code == 200:
    print(response.content)
