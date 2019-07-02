#!/usr/bin/env python3


class Employee(object):
    def __init__(self, first_name, second_name, salary, experiance):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = int(salary)
        self.experiance = int(experiance)

    def introduce(self):
        print("My name is " + self.first_name + " " + self.second_name)

    def show_finance(self):
        if self.experiance > 2:
            final_salary = self.salary + 200
        elif self.experiance > 5:
            final_salary = (self.salary * 1.2) + 500
        else:
            final_salary = self.salary
        return self.first_name + " " + self.second_name + " : got salary : " + str(final_salary)

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
        if team_members is not None:
            self.team_members = team_members
        else:
            self.team_members = []

    def add_team_member(self, team_member_object):
        self.team_members.append(team_member_object)

    def show_team_members(self):
        return self.team_members


class Department(object):
    def __init__(self, managers_list):
        self.managers_list = managers_list

    def show_managers_list(self):
        print(self.managers_list)

    def give_salary(self):
        for i in self.managers_list:
            print(i.show_finance())
            for j in i.show_team_members():
                print(j.show_finance())


#   pass
#    def show_managers_


worker1 = Employee("Adriano", "Celentano", 900, 5)
worker1.introduce()
worker1.show_finance()
worker2 = Developer("Jon", "Dou", 999, 5, "Jon Martin")
worker2.show_higher_man()
worker3 = Developer("Jon", "Dou2", 999, 6)
worker3.show_higher_man()
worker4 = Designer("Stive", "Jobs", 1000, 5, 1.0)
worker5 = Designer("Steave", "Moris", 1100, 5, 0.9)
manager1 = Manager("Tom", "Fozz", 888, 5)
worker6 = Developer("Salaga", "Dou", 500, 1, "Jon Martin")

worker4.show_finance()
manager1.add_team_member(worker1)
manager1.add_team_member(worker2)
manager1.add_team_member(worker4)
manager1.add_team_member(worker6)
#manager1.show_team_members()
#manager1.give_salary()
manager2 = Manager("Tim", "Collins", 989, 6)
#print("manager2-1")
#manager2.show_team_members()
manager2.add_team_member(worker3)
#print("manager2-2")
#manager2.show_team_members()
department1 = Department([manager1,manager2])
department1.show_managers_list()
department1.give_salary()
# print(manager1)
