import requests
from faker import Faker
from faker.providers import DynamicProvider
import os

random_product_provider = DynamicProvider(
    provider_name="random_product_id",
    elements=[493, 428, 421, 378, 373, 408],
)
fake = Faker()
fake.add_provider(random_product_provider)


def headers_maker(token):
    full_auth = "Bearer " + token
    headers = {"Authorization": full_auth}

    return headers


def client_info_asserting(response, db_values):
    json_response = response

    # !!! ВРЕМЕННОЕ РЕШЕНИЕ С УДАЛЕНИЕМ ЭТОГО ПОЛЯ ИЗ ОТВЕТА !!!
    json_response.pop("verified_client")

    # замена пробела в датах на "Т"
    date_created_replaced = str(vars(db_values).get("date_created")).replace(" ", "T")
    last_update_time_replaced = str(vars(db_values).get("last_update_time")).replace(" ", "T")
    vars(db_values).update(
        {
            "date_created": date_created_replaced,
            "last_update_time": last_update_time_replaced
        }
    )

    for key, value in json_response.items():
        assert value == vars(db_values).get(key), f"{value} is NOT equal {vars(db_values).get(key)}"


def get_random_product_id():
    return fake.random_product_id()


def add_random_favourite_product(client_token: str, product_id):
    headers = headers_maker(client_token)
    url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("PUT_CLIENT_FAVOURITE_LIST")
    request_body = {
        "product_id": product_id
    }
    response = requests.put(url=url, headers=headers, json=request_body)

    return response


def get_fav_products(client_token):
    headers = headers_maker(client_token)
    url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("GET_CLIENT_FAVOURITE_LIST")

    response = requests.get(url=url, headers=headers)

    return response


def delete_fav_product(client_token: str, product_id: int):
    headers = headers_maker(client_token)
    url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("DELETE_CLIENT_FAVOURITE")
    body = {
        "product_id": product_id
    }

    response = requests.delete(url=url, headers=headers, json=body)

    return response
