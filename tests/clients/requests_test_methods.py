import jsonpath
import json


class ClientInfoMethods:

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

        print("--------------------------------------------")
        for key, value in json_response.items():
            # print(key)
            # print(value)
            # print(vars(db_values).get(key))
            assert value == vars(db_values).get(key), f"{value} is NOT equal {vars(db_values).get(key)}"
