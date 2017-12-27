import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def length(self):
        return len(self.full_name()) - 1


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.full_name())


my_date = datetime.date(2016, 7, 10)

dev_1 = Developer('Dorota', 'Mierzwa', 10000000, 'Python')
dev_2 = Developer('Misio', 'Misiowy', 3000000, 'Java')


print(len(dev_1.full_name()))
print(dev_2 + dev_1)

# mgr_1 = Manager('Sue', 'Smith', 3333333, [dev_1])
# print(mgr_1.email)
#
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# Employee.set_raise_amt(1.07)

# emp_str_1 = 'John-Doe-90000'
# emp_str_2 = 'Joe-King-10000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
#
# print(new_emp_1.email)
# print(new_emp_2.email)

# print(Employee.is_workday(my_date))

print(str.__add__('1','2'))
