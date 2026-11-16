class Patient: #Creates a class named Patient, which will later serve as the parent class. L
    def __init__(self, name, bill_amount):
        self.__name = str(name)
        self.__bill_amount = float(bill_amount)
    
    def get_name(self): #Creates a function get_name() which acts as a getter and returns the informtion regarding the name of whatever object is instantiated from this class.
        return self.__name

    def set_name(self, name): #Creates a function set_name() which acts as a setter and updates the informtion regarding the name of whatever object is instantiated from this class.
        self.__name = name

    def get_bill_amount(self): #Creates a function get_name() which acts as a getter and returns the informtion regarding the attribute named "bill_amount" of whatever object is instantiated from this class.
        return self.__bill_amount

    def set_bill_amount(self, bill_amount): #Creates a function bill_amount() which acts as a setter and updates the informtion regarding the attribute "bill_amount" of whatever object is instantiated from this class.
        self.__bill_amount = bill_amount

    def calculate_bill(self): #Creates a function named calculate_bill() which essentially calculates the final bill of the patients while taking each of the their respective discounts into effec. In this class, the discount is zero.
        return self.__bill_amount             

    def display_patient_type(self): #Creates a function named display_patient_type() which returns the patient type of whatever object is instantiated from this class.
        return "Regular Patient"

class Senior_Patient(Patient): #Creates a child class of the class Patient named Senior_Patient, and inherits all of the existing methods and attributes of the said parent class. E

    def calculate_bill(self): #Overrrides the calculate_bill() method from the parent class and instead modifies the method into calculating the final bill alongside a 20% discount in accordance to the said senior patient discount.
        return self.get_bill_amount() - self.get_bill_amount() * 0.20

    def display_patient_type(self): #Overrides the display_patient_type() method from the parent class and instead modifies the method into denoting the instantiated object as a Senior Citizen.
        return "Senior Citizen"

class PhilHealth_Patient(Patient): #Creates a child class of the class Patient named PhilHealth_Patient, and also inherits ALL of the existing methods and atttributes of the parent class. O

    def calculate_bill(self):  #Overrrides the calculate_bill() method from the Patient class and instead modifies the method into calculating the final bill alongside a 15% discount in accordance to the said  philhealth member discount.
        return self.get_bill_amount() - self.get_bill_amount() * 0.15

    def display_patient_type(self): #Overrides the display_patient_type() method from the parent class and instead modifies the method into denoting the instantiated object as a PhilHealth Member.
        return "PhilHealth Member"

#Instantiates three different objects from each of the three classea abovementioned. N
patient = Patient("Frank Ocean", 15000.00)
senior_patient = Senior_Patient("Christopher Wallace", 15000.00)
philhealth_patient = PhilHealth_Patient("Tupac Shakur", 15000.00)


print("———————————————————————————————————")
print("      Hospital Billing System")
print("———————————————————————————————————")

#Calls all the respective methods from the parent class Patient including the overrriden methods and displays the regarding information about the instantiated object "patient". C
print(f"Patient Name: {patient.get_name()}")
print(f"Patient Type: {patient.display_patient_type()}")
print(f"Original Bill: ₱{patient.get_bill_amount():.2f}")
print(f"Final Bill: ₱{patient.calculate_bill():.2f}")

#Calls all the respective inherited methods of the child class Senior_Patient from the parent class Patient including the overrriden methods and displays the regarding information about the instantiated object "senior_patient". I
print(f"\nPatient Name: {senior_patient.get_name()}")
print(f"Patient Type: {senior_patient.display_patient_type()}")
print(f"Original Bill: ₱{senior_patient.get_bill_amount():.2f}")
print(f"Final Bill: ₱{senior_patient.calculate_bill():.2f}")

#Calls all the respective inherited methods of the child class PhilHealth_Patient from the parent class Patient including the overrriden methods and displays the regarding information about the instantiated object "philhealth_patient". O
print(f"\nPatient Name: {philhealth_patient.get_name()}")
print(f"Patient Type: {philhealth_patient.display_patient_type()}")
print(f"Original Bill: ₱{philhealth_patient.get_bill_amount():.2f}")
print(f"Final Bill: ₱{philhealth_patient.calculate_bill():.2f}")
