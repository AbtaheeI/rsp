class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns ${self.salary}"

    def yearly_bonus(self):
        return self.salary * 0.05

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def yearly_bonus(self):
        return (self.salary * 2) + (1000 * self.team_size)

    def describe(self):
        return super().describe() + f" and manages {self.team_size} people"

class Intern(Employee):
    def yearly_bonus(self):
        return 0
    