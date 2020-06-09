import requests 

def test_endpoint1():
  url = 'http://localhost:3000'
  response = requests.get(url)
  assert response.status_code == 200
  assert response.text == "Hello from Flask version 1!"