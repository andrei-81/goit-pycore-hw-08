from field import Field
from custom_error import Invalid_phone_number_error
class Phone(Field):

    def __init__(self, value):
        if self.is_valid_phone(value):
            super().__init__(value)
        else: 
            raise Invalid_phone_number_error()
    
    def is_valid_phone(self, number): 
        #len 3 for testing
        return len(str(number)) in [3, 10] and str(number).isdigit() 
