import requests

API_KEY = '49e66cf87550bb46f2d9c99cae01c183'

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Wo möchtest du nach dem Wetter gucken? Stadtname: ')
request_url = f'{BASE_URL}/?q={city}&appid={API_KEY}'
response = requests.get(request_url)
print(response)
if response.status_code == 200:
    print('Success')

else:
    print('Error')