from src.enums.client_enums import Statuses


class Client:
    def __int__(self):
        self.result = {}

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['client_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_type(self, client_type=0):
        self.result['type'] = client_type
        return self

    def build(self):
        return self.result
