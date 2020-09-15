from address_book import AddressBook


class Main:

    def main(self):
        Main.print_menu(self)
        user_input = Main.input_menu(self)
        Main.choose_option(self, user_input)

    def print_menu(self):
        print('''
welcome!
1. show book;
2. add contact;
3. change contact;
4. delete contact;
5. search contact;
0. - exit.
            ''')

    def input_menu(self):
        user_input = int(input('make choose: '))
        return user_input

    def choose_option(self, user_input):
        ab = AddressBook()
        if user_input == 1:
            ab.show()

        elif user_input == 2:
            name = input('input name: ')
            address = input('input address: ')
            phone = input('input phone: ')
            email = input('input email: ')

            ab.add(name, address, phone, email)

        elif user_input == 3:
            ab.show()

            name = input('input name for change: ')
            field = input('input field for change: ')
            new_info = input('input new info: ')

            ab.change(name, field, new_info)

            ab.show()

        elif user_input == 4:
            name = input('input name for delete: ')
            ab.delete(name)

        elif user_input == 5:
            name = input('input name: ')
            ab.search(name)

        elif user_input == 0:
            print('good bye!')

        else:
            return


if __name__ == '__main__':
    start = Main()
    start.main()
