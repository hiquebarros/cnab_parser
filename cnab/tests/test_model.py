from django.test import TestCase
from cnab.models import Transaction

class TestTransactionModel(TestCase):
    @classmethod
    def setUp(cls):
        """Creating a transaction instance"""
        cls.transaction_data = {
            'type': 1,
            'date': '20180301',
            'value': '0000019200',
            'cpf': '84515254073',
            'credit_card': '32344****1222',
            'hour': '145607',
            'owner': 'MARIA JOSEFINA',
            'name': 'JOÃO MACEDO   BAR DO JOÃO       '
        }

        cls.transaction = Transaction.objects.create(**cls.transaction_data)

    def test_transaction_fields(self):
        """Testing if the instance field values are equal to the setUp dict"""
        self.assertEqual(
            self.transaction.type, self.transaction_data["type"]
        )
        self.assertEqual(self.transaction.date, self.transaction_data["date"])
        self.assertEqual(self.transaction.value, self.transaction_data["value"])
        self.assertEqual(self.transaction.cpf, self.transaction_data["cpf"])
        self.assertEqual(self.transaction.credit_card, self.transaction_data["credit_card"])
        self.assertEqual(self.transaction.hour, self.transaction_data["hour"])
        self.assertEqual(self.transaction.owner, self.transaction_data["owner"])
        self.assertEqual(self.transaction.name, self.transaction_data["name"])

    def test_max_lengths(self):
        """Testing max lenght constraints"""
        date_max_length = self.transaction._meta.get_field("date").max_length
        value_max_length = self.transaction._meta.get_field("value").max_length
        cpf_max_length = self.transaction._meta.get_field("cpf").max_length
        credit_card_max_length = self.transaction._meta.get_field("credit_card").max_length
        hour_max_length = self.transaction._meta.get_field("hour").max_length
        owner_max_length = self.transaction._meta.get_field("owner").max_length
        name_max_length = self.transaction._meta.get_field("name").max_length

        self.assertEqual(date_max_length, 8)
        self.assertEqual(value_max_length, 10)
        self.assertEqual(cpf_max_length, 11)
        self.assertEqual(credit_card_max_length, 12)
        self.assertEqual(hour_max_length, 6)
        self.assertEqual(owner_max_length, 14)
        self.assertEqual(name_max_length, 19)


    def test_type_validators(self):
        """Testing type validators (only numbers from 1 to 9)"""
        self.transaction._meta.get_field("type")._validators[0].limit_value = 9
        self.transaction._meta.get_field("type")._validators[1].limit_value = 1