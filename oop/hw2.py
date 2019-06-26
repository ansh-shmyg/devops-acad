#!/usr/bin/env python3

class Employee(object):
    def __init__(self, first_name, second_name, salary, experiance):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = int(salary)
        self.experiance = int(experiance)

    def introduce(self):
        print("My name is " + self.first_name + " " + self.second_name)

    def show_self(self):
        print("My salary is " + str(self.salary) + "." + "I am working here " + str(self.experiance) + " years")

class Developer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, higher_manager=None):
        Employee.__init__(self, first_name, second_name, salary, experiance)
        self.higher_manager = higher_manager

    def show_higher_man(self):
        print("I am working with " + str(self.higher_manager))
# Super ?
class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, eff_koef, higher_manager=None):
        Employee.__init__(self, first_name, second_name, salary, experiance)
        self.eff_koef = float(eff_koef)
        self.higher_manager = higher_manager


class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experiance, higher_manager=None):
        self.team_members = []
        Employee.__init__(self, first_name, second_name, salary, experiance)
        self.higher_manager = higher_manager
    
    def add_team_member(self, team_member):
        team_members.append(str(self.team_member))
        
    def show_team_members(self):
        print(self.team_members)


class Department(object):
    pass


worker1 = Employee("Adriano","Celentano",900,5)
worker1.introduce()
worker1.show_self()
worker2 = Developer("Jon", "Dou", 999, 6, "Jon Martin")
worker2.show_higher_man()
worker3 = Developer("Jon", "Dou2", 999, 6)
worker3.show_higher_man()
manager1 = Manager("Tom","Fozz", 888, 5)
manager1.add_team_member("Some person")
manager1.show_team_members()
manager1.add_team_member("Person 2")
manager1.show_team_members()


