import os
import pytest
import requests
import dotenv
from tests.clients.requests_test_methods import ClientInfoMethods
from tests.conftest import jwt_gen

dotenv.load_dotenv()


@pytest.mark.usefixtures('temp_db')
class TestMain:
    @pytest.mark.debug
    def test_starter_eligible_true(self, temp_db):
        full_url = os.getenv("CLIENT_API_ORDERS_URL") + os.getenv("STARTER_ELIGIBLE_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        print("\n", response.json())
        assert (response.json() ==
                {
                    "status": True
                }), "Wrong answer"

    @pytest.mark.debug
    def test_client_info_positive(self, temp_db):
        full_url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("CLIENT_INFO_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        # print(full_auth)
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        response_body = response.json()
        ClientInfoMethods.client_info_asserting(response=response_body, db_values=temp_db.get("db_client_data"))

    # @pytest.mark.debug
    def test_client_info_negative(self, temp_db):
        full_url = os.getenv("CLIENT_API_CLIENTS_URL") + os.getenv("CLIENT_INFO_PATH")
        full_auth = "Bearer " + jwt_gen("definitely_wrong_client_id")
        # print(full_auth)
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)

        assert response.status_code == 401, "ERROR | Wrong status code"
        assert response.json() == {'detail': 'Unauthorized'}
