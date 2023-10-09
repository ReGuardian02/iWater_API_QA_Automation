import json
import os
import pytest
import requests
import dotenv
from tests.clients import requests_test_methods as methods
from tests.conftest import jwt_gen

dotenv.load_dotenv()


@pytest.mark.usefixtures('temp_db')
class TestClients:

    # @pytest.mark.skip
    def test_starter_eligible_true(self, temp_db):
        full_url = os.getenv("CLIENT_API_ORDERS_URL") + os.getenv("STARTER_ELIGIBLE_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        print("\n", response.json())
        assert response.json() == {"status": True}, "Wrong answer"

    # @pytest.mark.skip
    def test_client_info_positive(self, temp_db):
        full_url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("CLIENT_INFO_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        # print(full_auth)
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        response_body = response.json()
        methods.client_info_asserting(response=response_body, db_values=temp_db.get("db_client_data"))

    # @pytest.mark.skip
    def test_client_info_negative(self, temp_db):
        full_url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("CLIENT_INFO_PATH")
        full_auth = "Bearer " + jwt_gen("definitely_wrong_client_id")
        # print(full_auth)
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)

        assert response.status_code == 401, "ERROR | Wrong status code"
        assert response.json() == {'detail': 'Unauthorized'}

    # @pytest.mark.skip
    def test_favourite_list_positive(self, temp_db):
        new_client_token = temp_db.get("new_client_token")
        random_product_id = methods.get_random_product_id()

        get_response = methods.get_fav_products(new_client_token)

        assert get_response.status_code == 200, "ERROR | Wrong status code while getting empty product list"
        assert get_response.json() == {"favorites_list": []}, "ERROR | Wrong empty product list message"

        add_product_resp = methods.add_random_favourite_product(new_client_token, random_product_id)

        assert add_product_resp.status_code == 200, "ERROR | Wrong status code while getting adding product success message"
        assert add_product_resp.json() == {
            "status": True,
            "message": "Список любимых товаров пользователя успешно изменен."
        }, "ERROR | Wrong adding product success message"

        second_get_response = methods.get_fav_products(new_client_token)

        assert second_get_response.status_code == 200, "ERROR | Wrong status code while getting filled product list"
        assert second_get_response.json() == {"favorites_list": [random_product_id]}

        delete_response = methods.delete_fav_product(new_client_token, random_product_id)

        assert delete_response.status_code == 200, "ERROR | Wrong status code while getting deleting product success message"
        assert delete_response.json() == {
            "status": True,
            "message": f"Товар с id {random_product_id} из списка успешно удален."
        }, "ERROR | Wrong deleting product success message"

        last_get_response = methods.get_fav_products(new_client_token)

        assert last_get_response.status_code == 200, "ERROR | Wrong status code while getting empty product list after deleting"
        assert last_get_response.json() == {"favorites_list": []}, "ERROR | Wrong empty product list message after deleting"
