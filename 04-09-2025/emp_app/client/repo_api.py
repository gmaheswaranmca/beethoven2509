import requests
baseUrl = 'http://localhost:5000'
def create_employee(employee):
    url = f'{baseUrl}/employees'
    body = {'name' : employee['name']}
    response = requests.post(url, json=body)
    return response.json()

def read_all():
    url = f'{baseUrl}/employees'
    response = requests.get(url)
    return response.json()

def read_by_id(id): 
    url = f'{baseUrl}/employees/{id}'
    response = requests.get(url)
    return response.json()

def update(employee):
    url = f'{baseUrl}/employees/{employee["id"]}'
    body = {'name' : employee['name']}
    response = requests.put(url, json=body)
    return response.json()

def delete_by_id(id):
    url = f'{baseUrl}/employees/{id}'
    response = requests.delete(url)
    return response.json()