from .api import fetch_contacts, fetch_contact, delete_contact

class Format():
    ''' ASCI codes for formatting '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'

class CLI():
    ''' User interface '''
    def __init__(self):
        self._user_input = ""

    def start(self):
        try:
            # self._user_input = input(f'''\n{Format.BLUE}What is your github username?\n{Format.CLEAR}''')
            # if self._user_input == 'exit':
            #     return self.goodbye()
            # if not self.valid_input(self._user_input):
            #     raise ValueError
            # self.show_repos()
            # self.get_user_github()

            while True:
                print("""
                ----------------------MENU-----------------------
                1. View a list of contacts
                2. View a specific contact
                3. Create new contact
                4. Delete a contact
                5. Exit
                """)

                user_choice = input("\nWhich task would you like to complete: \n")
                if user_choice == '1':
                    print("""
                    Here is a list of all contacts:
                    """)
                    contacts = fetch_contacts()
                    for contact in contacts:
                        print(f"{contact['id']}. {contact['name']}")

                    print('''
                    Would you like to see details for a specific contacts?
                    ''')
                    decision = input("\ntype y/n for yes/no: \n")
                    if decision == "y":
                        contact_id = input("\n Which contact would you like to view? \n")
                        contact = fetch_contact(contact_id)
                        print(f'''
                        here are the details for {contact['name']}:
                        //////////////////////////////
                        name: {contact['name']}
                        email: {contact['email']}
                        number: {contact['number']}
                        workplace: {contact['workplace']}
                        //////////////////////////////
                        ''')
                        # print(contact)
                    self.start()
                    break
                elif user_choice == '2':
                    contacts = fetch_contacts()
                    name = input("\nName of contact you would like to view: \n")
                    for i in range(len(contacts)):
                        if contacts[i]['name'] == name:
                            print(f'''
                                {contacts[i]['name']}
                                {contacts[i]['email']}
                                {contacts[i]['number']}
                                {contacts[i]['workplace']}
                            ''')
                    break
                elif user_choice == '3':
                    break
                elif user_choice == '4':
                    destroy_id = input("\nEnter id of contact you want to delete:\n")
                    delete_contact(destroy_id)
                    self.start()
                elif user_choice == '5':
                    print("You chose to exit this app...")
                    exit_program()
                    break
                else:
                    print("Invalid choice. Please choose a number 1- 3.\n")

        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()
