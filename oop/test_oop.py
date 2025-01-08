import pytest
from oop.staff import Staff
from oop.classroom_staff import ClassroomStaff

class TestStaffProperties:
    def test_initial_name_takes_argument(self):
        niamh = Staff('niamh', 'mentor', 'classroom')
        assert niamh.name == 'niamh'
    
    def test_initial_role_takes_argument(self):
        niamh = Staff('niamh', 'mentor', 'classroom')
        assert niamh.role == 'mentor'

    def test_initial_department_takes_argument(self):
        niamh = Staff('niamh', 'mentor', 'classroom')
        assert niamh.department == 'classroom'

    def test_initial_employed_at_NC_defaults_to_True(self):
        niamh = Staff('niamh', 'mentor', 'classroom')
        assert niamh.employed_at_NC is True

    def test_initial_working_hours_defaults_to_34(self):
        niamh = Staff('niamh','mentor', 'classroom')
        assert niamh.working_hours == 34

    def test_initial_working_hours_takes_argument(self):
        niamh = Staff('niamh','mentor', 'classroom', 22)
        assert niamh.working_hours == 22

    def test_initial_salary_defaults_to_26000(self):
        niamh = Staff('niamh','mentor', 'classroom', 22)
        assert niamh.salary == 26000

    def test_initial_salary_takes_argument(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 100000)
        assert niamh.salary == 100000


class TestStaffMethods:
    def test_update_working_hours_reduces_hours(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 100000)
        assert niamh.working_hours == 22
        niamh.update_working_hours(20)
        assert niamh.working_hours == 20

    def test_update_working_hours_increases_hours(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 100000)
        assert niamh.working_hours == 22
        niamh.update_working_hours(24)
        assert niamh.working_hours == 24

    def test_increase_salary_increases_salary(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 100000)
        assert niamh.salary == 100000
        niamh.increase_salary(24000)
        assert niamh.salary == 124000
    
    
    def test_increase_salary_raises_exception_for_incorrect_input(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 100000)
        with pytest.raises(Exception) as output:
            niamh.increase_salary('four_pounds')
        assert 'The amount added must be a positive number' in str(output.value)

    def test_fire_fires_with_hr_approval(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 124000)
        assert niamh.employed_at_NC == True
        hr_report = {"approved": True}
        niamh.fire(hr_report)
        assert niamh.employed_at_NC == False

   
    def test_fire_raises_exception_when_hr_approval_is_false(self):
        niamh = Staff('niamh','mentor', 'classroom', 22, 124000)
        hr_report = {"approved": False}
        with pytest.raises(Exception) as output:
            niamh.fire(hr_report)
        assert 'Staff cannot be fired until approval on hr_report'


@pytest.mark.skip
class TestClassroomStaffProperties:
    def test_classroom_staff_initial_name_takes_argument_inherited_from_staff(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.name == 'niamh'

    def test_classroom_staff_initial_role_takes_argument_inherited_from_staff(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.role == 'mentor'

    def test_classroom_staff_initial_languages_takes_argument_not_inherited(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.languages == ['python']

    def test_classroom_staff_initial_working_hours_inherits_from_staff(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 27000)
        assert niamh.working_hours == 22
    
    def test_classroom_staff_initial_salary_inherits_from_staff(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.salary == 123000

    def test_classroom_staff_has_overtime_property_initialised_to_0(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.overtime == 0

    def test_classroom_staff_has_title_property_initialised_to_junior(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.title == 'junior developer'

@pytest.mark.skip
class TestClassroomStaffMethods:
    def test_add_overtime_increases_overtime_hours(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.overtime == 0
        niamh.add_overtime(4)
        assert niamh.overtime == 4

    def test_add_overtime_increases_multiple_times(self):
        niamh = ClassroomStaff('niamh', 'mentor', ['python'], 22, 123000)
        assert niamh.overtime == 0
        niamh.add_overtime(3)
        assert niamh.overtime == 3
        niamh.add_overtime(5)
        assert niamh.overtime == 8