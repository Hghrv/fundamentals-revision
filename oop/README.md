# OOP Issues

### Staff

In our OOP section, there is a `Staff Class` that has multiple properties, and a couple of methods. All of these have been tested.

However, there are still _a couple_ of tasks to complete.

1. Build a test for `increase_salary` that checks what happens when value passed is `'four_pounds'` rather than `4`.

2. Build a test that utilises a custom Exception for the `fire` method, when the `hr_report = {"approved": False}`.

_Are there other Exceptions you could use throughout this class?_
_Student's answer: Other similar Exceptions could also be raised when the name, role, or department entered as instance arguments are not strings_

***

### ClassroomStaff

You will have noticed another class called `ClassroomStaff`. This is a subclass of `Staff`, so will contain many properties and methods that belong to the `Staff` class. In the test file, you should remove/change the pytest decorator.

The `__init__` method here is declaring the arguments needed from the invocation.

The `super` method here is declaring the _inherited_ properties. As this is the classroom staff class, you can see that `department` has been fixed as `'classroom'`.

The method `add_overtime` is different from the methods it has inherited from `Staff`. The methods `fire`, `update_working_hours` and `increase_salary` have all previously been tested, so there's no need to create tests for them here. However, it's perfectly reasonable to still use those methods. 

1. Create a new method called `overtime_paid` that reduces the overtime property depending on how much has been paid. This method should take an argument of hours_paid, and you should test for some possible Exceptions.

2. Create a new method called `change_title`. Once a mentor's salary hits `36000`, they should be able to drop the title of 'junior developer' and become a 'mid-level developer'. Once they hit `50000`, they should become a 'senior developer'. This should _not_ impact their role.