import os
import pytest
import requests
import dotenv

dotenv.load_dotenv()


@pytest.mark.usefixtures('temp_db')
class TestMain:
    @pytest.mark.debug
    def test_starter_eligible_true(self, temp_db):
        full_url = os.getenv("GATEWAY_URL") + os.getenv("STARTER_ELIGIBLE_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        print("\n", response.json())
        assert (response.json() ==
                {
                    "status": True
                }), "Wrong answer"

    def test_client_info(self, temp_db):
        full_url = os.getenv("GATEWAY_URL") + os.getenv("CLIENT_INFO_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        response_body = response.json()
        print("\n---------------------------------------------------------")
        print(response_body)
        assert response.status_code == 200