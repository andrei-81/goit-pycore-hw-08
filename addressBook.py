from collections import UserDict
from record import Record
from name import Name
from phone import Phone
from custom_error import *

class AddressBook(UserDict):

    def add_record(self, record: Record):
        if record.name in self.keys(): 
            print(f"contact {record.name} already in address book")
        else:
            self.update({record.name.value: record})

    def find(self, nameToFind) -> Record:
        if nameToFind in self.keys():
            return self.get(nameToFind)
        return None

    def delete(self, name): 
        if name in self.keys():
            self.pop(name)
            print(f"contact {name} has been deleted")
        else:
            print(f"contact {name} not found in address book")

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Invalid_birthday_error:
                return "birthday should be in DD.MM.YYYY format"
            except Invalid_phone_number_error: 
                return "phone should contain 10 digits"
        return inner

    @input_error
    def add(self, args):
        if len(args) < 1:
            return "give me name (and optionally phone) to add"
        
        name = args[0]
        record = self.find(name)
        message = "Contact exists."
        if record is None:
            record = Record(name)
            self.add_record(record)
            message = "Contact added."
        if len(args) > 1:
            phone = args[1]
            record.add_phone(phone)
        return message
    
    @input_error
    def change(self, args):
        if len(args) < 3:
            return "give me name, old and new phones"
        name = args[0]
        oldPhone = args[1]
        newPhone = args[2]
        if name not in self.keys():
            return f"contact {name} not found"
        return self.get(name).edit_phone(oldPhone, newPhone)

    def phone(self, args): 
        if len(args) < 1: 
            return "give me name or phone"
        if args[0] in self.keys():
            return self.get(args[0])
        nameByPhone = self.search_name_by_phone(args[0])
        if len(nameByPhone) > 0:
            return self.get(nameByPhone)
        return f"contact or phone {args[0]} not found in address book"
        
    
    def search_name_by_phone(self, phone): 
        result = ''
        for key in self.keys():
            if self.get(key).get_phone_index(phone) >= 0:
                return key
        return result
    
    def print_all(self): 
        for key in self.keys():
            print(self.get(key))

    @input_error
    def add_birthday(self, args):
        if len(args) < 2:
            return "give me name and birthday"
        name = args[0]
        bd = args[1]
        if name in self.keys():
            return self.get(name).add_birthday(bd)
        return f"contact with name {name} not found"


    def show_birthday(self, args):
        if len(args) < 1:
            return "give me the name"
        name = args[0]
        if name in self.keys():
            return self.get(name).show_birthday()
        return f"contact with name {name} not found"
    
    def print_birthdays(self): 
        no_rows = True
        for key in self.keys():
            if self.get(key).has_birthday():
                print(self.get(key).show_birthday())
                no_rows = False
        if no_rows:
            print("no record found with the specified birthday")
