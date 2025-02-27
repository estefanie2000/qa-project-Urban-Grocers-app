import configuration
import requests
import data

def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
                         json=body,
                         headers=data.headers)

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())