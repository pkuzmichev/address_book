import json
import unittest
import os

from address_book import AddressBook
from parameterized import parameterized


class AddressBookTest(unittest.TestCase):

    def setUp(self):
        self.ab = AddressBook()
        with open('address_book.json', 'w'):
            pass

    def test_file_non_exist(self):
        os.remove('address_book.json')
        self.ab.add('test', 'test', 'test', 'test')
        assert os.path.isfile('address_book.json')

    @parameterized.expand([
        ('test', 'test', 'test', 'test', "{'test': {'address': 'test', 'phone': 'test', 'email': 'test'}}"),
        ('', '', '', '', "{'': {'address': '', 'phone': '', 'email': ''}}"),
        ('тест', 'тест', 'тест', 'тест', "{'тест': {'address': 'тест', 'phone': 'тест', 'email': 'тест'}}")
    ])
    def test_add_write(self, name, address, phone, email, expected_result):
        self.ab.add(name, address, phone, email)
        with open('address_book.json', 'r') as f:
            address_book_file = json.load(f)
        self.assertEqual(str(address_book_file), expected_result)

    def tearDown(self):
        os.remove('address_book.json')


if __name__ == '__main__':
    unittest.main()
