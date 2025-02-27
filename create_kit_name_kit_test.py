import sender_stand_request
import data

def  get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

print(data.kit_body)
print(get_kit_body("Antonio"))

def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["authToken"] != ""
    print(kit_response.status_code)
    print(kit_response.json()["authToken"])