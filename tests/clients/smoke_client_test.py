import os
import pytest
import requests
import dotenv
from tests.clients.requests_test_methods import ClientInfoMethods

dotenv.load_dotenv()


@pytest.mark.usefixtures('temp_db')
class TestMain:
    # @pytest.mark.debug
    def test_starter_eligible_true(self, temp_db):
        full_url = os.getenv("CLIENT_SERVICE_TEST_URL") + os.getenv("STARTER_ELIGIBLE_PATH")
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
        full_url = os.getenv("CLIENT_SERVICE_TEST_URL") + os.getenv("CLIENT_INFO_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        print(full_auth)
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        response_body = response.json()
        ClientInfoMethods.client_info_asserting(response=response_body, db_values=temp_db.get("db_client_data"))


        # response_body = response.json()
        # print("\n---------------------------------------------------------")
        # print(response_body)
        # assert response.status_code == 200
