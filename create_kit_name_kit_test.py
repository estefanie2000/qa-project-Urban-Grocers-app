import data
import sender_stand_request

def  get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def get_kit_name(kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = kit_name
    return current_kit_name

def positive_assert_201(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


def test1_create_kit_1_letter_in_name_get_success_response():
    current_kit_name = get_kit_name("a")
    positive_assert_201(current_kit_name)

def test2_create_kit_511_letter_in_name_get_success_response():
    current_kit_name = get_kit_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert_201(current_kit_name)

def test3_create_kit_0_letter_in_name_get_success_response():
    current_kit_name = get_kit_name( "")
    negative_assert_400(current_kit_name)

def test4_create_kit_512_letter_in_name_get_success_response():
     current_kit_name = get_kit_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
     negative_assert_400(current_kit_name)

def test5_create_kit_symbols_letter_in_name_get_success_response():
     current_kit_name = get_kit_name(""%",")
     positive_assert_201(current_kit_name)

def test6_create_kit_with_space_letter_in_name_get_success_response():
     current_kit_name = get_kit_name( "A Aaa ")
     positive_assert_201(current_kit_name)

def test7_create_kit_with_numbers_in_name_get_success_response():
     current_kit_name = get_kit_name("123")
     positive_assert_201(current_kit_name)

def test8_create_kit_in_name_get_success_response():
    current_kit_name = get_kit_name()
    negative_assert_400(current_kit_name)

def test9_create_kit_number_in_name_get_success_response():
    current_kit_name = get_kit_name(123)
    negative_assert_400(current_kit_name)




