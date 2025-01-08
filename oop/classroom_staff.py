from oop.staff import Staff

class ClassroomStaff(Staff):

    def __init__(self, name, role, languages, working_hours, salary):
        super().__init__(name, role, department='classroom', working_hours = working_hours, salary = salary)
        self.overtime = 0
        self.languages = languages
        self.title = 'junior developer'

    def add_overtime(self, overtime_hours):
        self.overtime += overtime_hours
    
    def overtime_paid(self):
        if self.working_hours == 0:
            raise Exception('Working hours cannot be 0')
        return self.overtime(salary/working_hours) 

    def change_title(self):
        if self.salary >= 50000:
            self.title = 'senior developer'
        elif self.salary >= 36000:
            self.title = 'mid-level developer'