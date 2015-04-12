class Employee():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super().__init__(name)
        self.hourly_wage = hourly_wage

    def weekly_pay(self, hours):
        if hours <= 40:
            return self.hourly_wage * hours
        else:
            return (40 * self.hourly_wage) + (hours - 40) * self.hourly_wage * 1.5


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def weekly_pay(self, hours):
        return self.annual_salary / 12


class Manager(SalariedEmployee):
    def __init__(self, name, annual_salary, weekly_bonus):
        super().__init__(name, annual_salary)
        self.weekly_bonus = weekly_bonus

    def weekly_pay(self, hours):
        return self.annual_salary / 12 + self.weekly_bonus
