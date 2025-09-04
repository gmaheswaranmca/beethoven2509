# pip install requests 

import requests 
baseUrl = 'https://jsonplaceholder.typicode.com'
response = requests.get(f'{baseUrl}/posts')
posts = response.json()
print(posts)