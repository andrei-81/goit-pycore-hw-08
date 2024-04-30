from name import Name
from phone import Phone
from birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phones_to_print = f", phones {'; '.join(p for p in self.phones)}" if len(self.phones) > 0 else ""
        bd_to_print = f", birhtday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}{phones_to_print}{bd_to_print}"
    
    def add_phone(self, phone: str):
        checkedPhone = Phone(phone)
        if checkedPhone:
            if self.get_phone_index(checkedPhone) < 0:
                self.phones.append(phone) 
    
    def remove_phone(self, phone_to_remove):
        index = self.get_phone_index(phone_to_remove)
        self.phones.pop(index) if index > 0 else self.phone_not_found_message(phone_to_remove)

    def get_phone_index(self, phone_to_find): 
        for i, phone_in_list in enumerate(self.phones):
            if phone_in_list == str(phone_to_find):
                return i
        return -1
    
    def edit_phone(self, phone_to_edit, newPhone):
        index = self.get_phone_index(phone_to_edit)
        
        if index >= 0: 
            self.phones[index] = Phone(newPhone)
            return "done"
        else: 
            return self.phone_not_found_message(phone_to_edit)
        
    def phone_not_found_message(self, phone_to_print):
        return f"Phone {phone_to_print} not found"
    
    def add_birthday(self, bd_stirng): 
        if self.birthday:
            print("contact already has birthday")
        self.birthday = Birthday(bd_stirng)
        return "birthday added"

    def show_birthday(self):
        return f"{self.name} birthday on {self.birthday}" if self.birthday else f"ask {self.name} about his birthday"
    
    def has_birthday(self):
        return True if self.birthday else False