class Patient:
    def __init__(self, name, bill_amount):
        self.__name = str(name)
        self.__bill_amount = float(bill_amount)
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        

    def display_patient_type(self):
        print("Regular Patient")

class Senior_Patient(Patient):

    def calculate_bill(self):   

    def display_patient_type(self):
        print("Senior Citizen")

class PhilHealth_Patient(Patient):

    def calculate_bill(self):   

    def display_patient_type(self):
        print("PhilHealth Member")

print("Hospital Billing System")
print("———————————————————————")

print(f"Patient Name:")
print(f"Patient Type:")
print(f"Original Bill:")
print(f"Final Bill:")

print(f"\nPatient Name:")
print(f"Patient Type:")
print(f"Original Bill:")
print(f"Final Bill:")

print(f"\nPatient Name:")
print(f"Patient Type:")
print(f"Original Bill:")
print(f"Final Bill:")