import os
import pytest
import requests
import dotenv

dotenv.load_dotenv()


@pytest.mark.usefixtures('temp_db')
class TestBebra:
    def test_starter_bebra(self, temp_db):
        full_url = os.getenv("GATEWAY_URL") + os.getenv("STARTER_ELIGIBLE_PATH")
        full_auth = "Bearer " + temp_db.get("new_client_token")
        headers = {"Authorization": full_auth}
        response = requests.get(url=full_url, headers=headers)
        print("\n", response.json())
        assert (response.json() ==
                {
                    "status": True
                }), "Wrong answer"
