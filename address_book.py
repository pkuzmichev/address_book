import json

from json.decoder import JSONDecodeError


class AddressBook:

    def __init__(self):
        self.book = {}

    def add(self, name, address, phone, email):
        self.book[name] = {'address': address, 'phone': phone, 'email': email}

        try:
            try:
                with open('address_book.json', 'r') as f:
                    address_book_file = json.load(f)
            except JSONDecodeError:
                pass
        except FileNotFoundError:
            pass

        try:
            address_book_file.update(self.book)
        except UnboundLocalError:
            address_book_file = self.book

        try:
            with open('address_book.json', 'w') as file:
                json.dump(address_book_file, file)
        except JSONDecodeError:
            print('file is empty or not valid')

    def show(self):
        try:
            with open('address_book.json') as json_file:
                address_book = json.load(json_file)

                print()
                for i in address_book:
                    print(i, address_book[i], sep=': ')
        except JSONDecodeError:
            print('file is empty or not valid')

    def change(self, name, change_info, new_info):
        try:
            with open('address_book.json', 'r') as f:
                address_book_file = json.load(f)
        except JSONDecodeError:
            print('file is empty or not valid')

        address_book_file[name][change_info] = new_info

        address_book_file.update(self.book)

        with open('address_book.json', 'w') as file:
            json.dump(address_book_file, file)

    def delete(self, name):
        try:
            with open('address_book.json', 'r') as f:
                address_book_file = json.load(f)
        except JSONDecodeError:
            print('file is empty or not valid')

        address_book_file.pop(name)

        try:
            with open('address_book.json', 'w') as file:
                json.dump(address_book_file, file)
        except JSONDecodeError:
            print('file is empty or not valid')

    def search(self, name):
        try:
            with open('address_book.json') as json_file:
                address_book = json.load(json_file)
        except JSONDecodeError:
            print('file is empty or not valid')

        print()
        for i in address_book[name]:
            print(i, address_book[name][i], sep=': ')
