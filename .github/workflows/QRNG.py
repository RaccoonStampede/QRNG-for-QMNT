import requests

url = "https://qrng.anu.edu.au/API/jsonI.php?length=10&type=uint8"
response = requests.get(url)
data = response.json()
print(data['data'])
