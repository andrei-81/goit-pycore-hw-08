import pickle
from addressBook import AddressBook
from record import Record

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    
help_message = '''Available commands: 
* hello             print greeting
* add               add or update contact. Arguments: <name>, <phone>. <Phone> is optional. Phone should contain 10 digits
* change            change phone number. Arguments: <name>, <old phone>, <new phone>
* phone             search contact by name or phone in address book. Argument: <name or phone>
* all               print all address book
* add-birthday      add birthday to contact. Arguments: <name>, <birthday>
* show-birthday     print contact's birthday. Argument: <name>
* birthdays         print all birthdays in address book
* close (exit)      exit the program
* help (?)          print this help
'''

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    print("type \"?\" or \"help\" to get help")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book) 
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(book.add(args))

        elif command == "change":
            print(book.change(args))

        elif command == "phone":
            print(book.phone(args))

        elif command == "all":
            book.print_all()

        elif command == "add-birthday":
            print(book.add_birthday(args))

        elif command == "show-birthday":
            print(book.show_birthday(args))

        elif command == "birthdays":
            book.print_birthdays()
        
        elif command in ["help", "?"]:
            print(help_message)

        else:
            print("Invalid command.")

def parse_input(inputString: str):
    strippedString = inputString.strip()
    if " " in strippedString:
        splitted = strippedString.split(" ")
        return splitted[0].lower(), *splitted[1:]
    return strippedString, 

main()
