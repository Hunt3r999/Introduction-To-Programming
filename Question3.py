# Define the Patient class
class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number,
                 emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    # Accessor methods
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip_code}"

    # Mutator methods (setters)
    def set_phone_number(self, new_phone):
        self.phone_number = new_phone

    def set_emergency_contact_phone(self, new_contact_phone):
        self.emergency_contact_phone = new_contact_phone


# Define the Procedure class
class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # Accessor methods
    def get_details(self):
        return f"Procedure Name: {self.name}\nDate: {self.date}\nPractitioner: {self.practitioner}\nCharge: ${self.charge}"
# Sample date
today_date = "2024-01-05"
# Create an instance of the Patient class
patient = Patient("John", "Doe", "", "123 Main St", "Anytown", "CA", "12345", "123-456-7890", "Jane Doe",
                  "987-654-3210")
# Create three instances of the Procedure class
procedure1 = Procedure("Physical Exam", today_date, "Dr. Irvine", 250.00)
procedure2 = Procedure("X-ray", today_date, "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood test", today_date, "Dr. Smith", 200.00)
# Display patient information
print("Patient Information:")
print(f"Full Name: {patient.get_full_name()}")
print(f"Address: {patient.get_address()}")
print(f"Phone Number: {patient.phone_number}")
print(f"Emergency Contact: {patient.emergency_contact_name}, {patient.emergency_contact_phone}")
# Display information about all three procedures
print("\nProcedure Details:")
print("Procedure 1:")
print(procedure1.get_details())
print("\nProcedure 2:")
print(procedure2.get_details())
print("\nProcedure 3:")
print(procedure3.get_details())
# Calculate and display the total charges
total_charges = procedure1.charge + procedure2.charge + procedure3.charge
print(f"\nTotal Charges: ${total_charges}")
