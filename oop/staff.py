class Staff():
    def __init__(self, name, role, department, working_hours = 34, salary = 26000):
        self.name = name
        self.role = role
        self.department = department
        self.employed_at_NC = True
        self.working_hours = working_hours
        self.salary = salary


    def update_working_hours(self, new_hours):
        self.working_hours = new_hours

    def increase_salary(self, addition_to_salary):
        if type(addition_to_salary) not in [float, int] or addition_to_salary < 0:
            raise Exception('The amount added must be a positive number')
        self.salary += addition_to_salary

    def fire(self, hr_report):
        if(hr_report['approved']):
            self.employed_at_NC = False
        else:
            raise Exception('Staff cannot be fired until offical approval on hr_report')
