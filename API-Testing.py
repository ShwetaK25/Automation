import requests
import pytest
import json

#to verify response format
response = requests.get("http://api.zippopotam.us/us/90210")
assert response.headers["content-type"]=="application/json"

#to verify status code
assert response.status_code == 200

#to verify response body
response_body = response.json()
assert response_body["country"]=="United States"

#to verify length of a particular attribute in response body
assert len(response_body["places"])== 1
print(response_body["places"][0])
