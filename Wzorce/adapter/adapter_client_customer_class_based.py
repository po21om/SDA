from typing import Union, Dict


class Customer:
    def get_first_name(self) -> str:
        pass

    def get_last_name(self) -> str:
        pass

    def get_email(self) -> str:
        pass

    def get_phone_numer(self) -> str:
        pass

    def get_transaction_count(self) -> int:
        pass


class Client:
    def __init__(self, full_name: str, contact_details: Union[Dict, None],
                 number_of_transactions: int):
        self._full_name = full_name
        self._contact_details = contact_details
        self._number_of_transactions = number_of_transactions

    def get_full_name(self) -> str:
        return self._full_name

    def get_contact_details(self) -> Dict[str, str]:
        return self._contact_details or {'email': '', 'phone': ''}

    def get_numer_of_transactions(self) -> int:
        return self._number_of_transactions


class ClientAdapter(Customer, Client):
    def __init__(self, full_name: str, contact_details: Union[Dict, None],
                 number_of_transactions: int):
        super().__init__(full_name, contact_details, number_of_transactions)

    def get_first_name(self) -> str:
        return self.get_full_name().split(' ')[0]

    def get_last_name(self) -> str:
        return self.get_full_name().split(' ')[1]

    def get_email(self) -> str:
        return self.get_contact_details().get('email')

    def get_phone_numer(self) -> str:
        return self.get_contact_details().get('phone')

    def get_transaction_count(self) -> int:
        return self.get_numer_of_transactions()


if __name__ == "__main__":
    customers = [
        ClientAdapter('John Kowalsky', {'email': 'johnkowalsky@example.com',
                                        'phone': '123456789'}, 10),
        ClientAdapter('Joe Doe', {'email': 'joedoe@example.com', 'phone': '456123789'}, 12),
        ClientAdapter('Eve First', {'email': 'evefirst@example.com', 'phone': '789123456'}, 1000)
    ]

    for c in customers:
        print(f'{c.get_first_name()} {c.get_last_name()} has email: '
              f'{c.get_email()} and phone number: '
              f'{c.get_phone_numer()} and did {c.get_transaction_count()} transactions.')
