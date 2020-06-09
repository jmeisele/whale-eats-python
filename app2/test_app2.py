import requests 

def test_endpoint2():
  url = 'http://localhost:3001'
  response = requests.get(url)
  assert response.status_code == 200
  assert response.text == "Hello from Flask version 2!"