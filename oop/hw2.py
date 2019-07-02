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
        super().__init__(first_name, second_name, salary, experiance)
        self.higher_manager = higher_manager

    def show_higher_man(self):
        print("I am working with " + str(self.higher_manager))

class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, eff_koef, higher_manager=None):
        super().__init__(first_name, second_name, salary, experiance)
        self.eff_koef = float(eff_koef)
        self.higher_manager = higher_manager


class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experiance, higher_manager=None, team_members=None):
        super().__init__(first_name, second_name, salary, experiance)
        self.higher_manager = higher_manager
        if team_members != None :
            self.team_members = team_members
        else : 
            self.team_members = []
        print("class")
        print(team_members)
    
    def add_team_member(self, team_member_sec_name):
#        self.team_member_sec_name = team_member_sec_name
        self.team_members.append(team_member_sec_name)
        
    def show_team_members(self):
        print(self.team_members)


class Department(object):
    def __init__(self, managers_list):
        self.managers_list = managers_list
#   pass
#    def show_managers_


worker1 = Employee("Adriano","Celentano",900,5)
worker1.introduce()
worker1.show_self()
worker2 = Developer("Jon", "Dou", 999, 6, "Jon Martin")
worker2.show_higher_man()
worker3 = Developer("Jon", "Dou2", 999, 6)
worker3.show_higher_man()
worker4 = Designer("Stive","Jobs", 1000, 5 , 1.0)
worker5 = Designer("Steave", "Moris", 1100, 5, 0.9)
manager1 = Manager("Tom","Fozz", 888, 5)
manager1.add_team_member(worker1)
manager1.show_team_members()
manager1.add_team_member(worker2)
manager1.add_team_member(worker4)
manager1.show_team_members()
manager2 = Manager("Tim", "Collins", 989, 6)
print("manager2-1")
manager2.show_team_members()
manager2.add_team_member(worker3)
print("manager2-2")
manager2.show_team_members()

#print(manager1)
