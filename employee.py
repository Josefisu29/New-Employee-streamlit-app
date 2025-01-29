# Class to define the Employee attributes
class Employee:
    def __init__(self, first_name, second_name, address):
        self.first_name = first_name
        self.second_name = second_name
        self.address = address

    def get_name(self):
        return f"{self.first_name} {self.second_name}"

# Class for PartTimeEmployee inheriting Employee
class PartTimeEmployee(Employee):
    def __init__(self, first_name, second_name, address, weekly_pay):
        super().__init__(first_name, second_name, address)
        self.weekly_pay = weekly_pay

    def get_pay(self):
        return f"Weekly Pay: ${self.weekly_pay}"

# Class for FullTimeEmployee inheriting Employee
class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, address, monthly_pay):
        super().__init__(first_name, second_name, address)
        self.monthly_pay = monthly_pay

    def get_pay(self):
        return f"Monthly Pay: ${self.monthly_pay}"

# Address class to store employee address
class Address:
    def __init__(self, street_number, street_name, state_code, state_name):
        self.street_number = street_number
        self.street_name = street_name
        self.state_code = state_code
        self.state_name = state_name

    def get_full_address(self):
        return f"{self.street_number} {self.street_name}, {self.state_code} {self.state_name}"
