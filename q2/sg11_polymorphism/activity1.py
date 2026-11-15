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
        return self.__bill_amount             

    def display_patient_type(self):
        return "Regular Patient"

class Senior_Patient(Patient):

    def calculate_bill(self):   
        return self.__bill_amount - self.__bill_amount * 0.20

    def display_patient_type(self):
        return "Senior Citizen"

class PhilHealth_Patient(Patient):

    def calculate_bill(self):   
        return self.__bill_amount - self.__bill_amount * 0.15

    def display_patient_type(self):
        return "PhilHealth Member"
    
patient = Patient("Frank Ocean", 15000.00)
senior_patient = Senior_Patient("Christopher Wallace", 15000.00)
philhealth_patient = PhilHealth_Patient("Tupac Shakur", 15000.00)

print("    Hospital Billing System")
print("———————————————————————————————")

print(f"Patient Name: {patient.get_name()}")
print(f"Patient Type: {patient.display_patient_type()}")
print(f"Original Bill: ₱{patient.get_bill_amount():.2f}")
print(f"Final Bill: ₱{patient.calculate_bill():.2f}")

print(f"\nPatient Name: {senior_patient.get_name()}")
print(f"Patient Type: {senior_patient.display_patient_type()}")
print(f"Original Bill: ₱{senior_patient.get_bill_amount():.2f}")
print(f"Final Bill: {senior_patient.calculate_bill():.2f}")

print(f"\nPatient Name: {philhealth_patient.get_name()}")
print(f"Patient Type: {philhealth_patient.display_patient_type()}")
print(f"Original Bill: ₱{philhealth_patient.get_bill_amount():.2f}")
print(f"Final Bill: {phlhealth_patient.calculate_bill():.2f}")
