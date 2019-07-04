#!/usr/bin/env python3


class Error(Exception):
   pass

class SalaryGivingError(Error):
   def __init__(self):
      #super().__init__(self,"SalaryGivingError")
      Exception.__init__(self,"SalaryGivingError")

class NotEmployeeException(Error):
   def __init__(self):
      Exception.__init__(self,"List must not be empty")
  
class WrongEmployeeRoleError(Error):
   def __init__(self, second_name):
      Exception.__init__(self)
      self.second_name = second_name
   
   def __str__(self):
     return "Employee " + str(self.second_name) + " has unexpected role!"
   

class Employee(object):
    def __init__(self, first_name, second_name, salary, experiance, higher_manager=None):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = int(salary)
        self.experiance = int(experiance)
        self.higher_manager = higher_manager

    def introduce(self):
        print("My name is " + self.first_name + " " + self.second_name)

    def show_finance(self):
        if self.experiance > 5:
            final_salary = (self.salary * 1.2) + 500
        elif self.experiance > 2:
            final_salary = self.salary + 200
        else:
            final_salary = self.salary
        return final_salary

    def __str__(self):
        return str(self.first_name) + " " + str(self.second_name) + ", manager: " + str(self.higher_manager.first_name) + " " + str(self.higher_manager.second_name) + ", experiance: " + str(self.experiance)  


class Developer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, higher_manager=None):
        super().__init__(first_name, second_name, salary, experiance, higher_manager)

    def show_higher_man(self):
        print("I am working with " + str(self.higher_manager))


class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experiance, eff_koef, higher_manager=None):
        super().__init__(first_name, second_name, salary, experiance, higher_manager)
        self.eff_koef = float(eff_koef)

    def show_finance(self):
        final_salary = super().show_finance()
        return final_salary * self.eff_koef
        

class Manager(Employee,Error):
    def __init__(self, first_name, second_name, salary, experiance, higher_manager=None, team_members=None):
        super().__init__(first_name, second_name, salary, experiance, higher_manager)
        if team_members is not None:
            self.team_members = team_members
        else:
            self.team_members = []

    def add_team_member(self, team_member_object):
        team_member_object.higher_manager = self
        self.team_members.append(team_member_object)
    
    def add_to_team(self, array_of_members=False):
        if not array_of_members: 
            raise NotEmployeeException()
        for i in array_of_members:
            if type(i).__name__ == "Manager":
                raise WrongEmployeeRoleError(i.second_name)
        self.team_members.extend(array_of_members)

    def show_team_members(self):
        return self.team_members

    def num_of_team_members(self):
        return len(self.team_members)

    def show_finance(self):
        final_salary = super().show_finance()
        team_members_num = len(self.team_members)
        team_devs_members_num = 0 
        for i in self.team_members : 
             if type(i).__name__ == "Developer":
                 team_devs_members_num += 1    
        if team_devs_members_num > ( team_members_num / 2) : 
             final_salary = final_salary * 1.1
             return final_salary
        if team_members_num > 10 :
             final_salary += 300
        elif team_members_num > 5 :
             final_salary += 200
        return final_salary


class Department(Error):
    def __init__(self, managers_list):
        self.managers_list = managers_list

    def show_managers_list(self):
        print(self.managers_list)

    def give_salary(self):
        for i in self.managers_list:
            print(" --- " + i.second_name + "'s team ---")
            print(str(i.first_name) + " " + str(i.second_name) + " : got salary : " + str(i.show_finance()))
            if i.num_of_team_members() == 0:
                raise SalaryGivingError()
            for j in i.show_team_members():
                print(str(j.first_name) + " " + str(j.second_name) + " : got salary : " + str(j.show_finance()))
     
    def add_to_team_members(self, manager, array):
        try:
            manager.add_to_team(array)
        except NotEmployeeException as err:
            print("Warning: Error to add employees to team: {0}".format(err)) 
        except WrongEmployeeRoleError as err:
            print("Warning: Managers can't be added as team member. Original error:\n{0}".format(err))

### end of code. add some data
#manager1 = Manager("Virktor", "Piatochnik1", 800, 3)
#manager2 = Manager("Virktor", "Piatochnik2", 700, 1)
#manager3 = Manager("Virktor", "Piatochnik3", 1000, 2, manager1)
#manager4 = Manager("Virktor", "Piatochnik4", 2000, 3)
#
#print(manager1.show_finance())
#worker1 = Developer("Steve", "Wozniak1", 900 , 2, manager1) 
#worker2 = Developer("Steve", "Wozniak2", 1000 , 3) 
#worker3 = Developer("Steve", "Wozniak3", 1200 , 4) 
#worker4 = Developer("Steve", "Wozniak4", 1200 , 5) 
#worker5 = Developer("Steve", "Wozniak5", 1500 , 6) 
#worker6 = Developer("Steve", "Wozniak6", 1500 , 7) 
#worker7 = Developer("Steve", "Wozniak7", 1500 , 6) 
#worker8 = Developer("Steve", "Wozniak8", 1500 , 7) 
#worker9 = Developer("Steve", "Wozniak9", 1500 , 5) 
#worker10 = Developer("Steve", "Wozniak10", 2000 , 8) 
#
#designer1 = Designer("Dan", "Moris1", 1100, 5, 0.9)
#designer2 = Designer("Dan", "Moris2", 1200, 7, 0.7)
#designer3 = Designer("Dan", "Moris3", 1300, 3, 0.8)
#designer4 = Designer("Dan", "Moris4", 1400, 1, 0.6)
#designer5 = Designer("Dan", "Moris5", 1000, 6, 0.8)
#designer6 = Designer("Dan", "Moris6", 900, 2, 1.0, manager2)
#
#manager1.add_team_member(worker1)
#manager1.add_team_member(worker2)
##manager1.add_team_member(worker5)
#manager1.add_team_member(designer1)
#manager1.add_team_member(designer2)
#
##manager1.add_to_team()
##manager1.add_to_team([worker3,worker4])
##manager1.add_to_team([worker3,worker4,manager4])
#
#manager2.add_team_member(worker3)
#manager2.add_team_member(worker4)
#manager2.add_team_member(worker5)
#manager2.add_team_member(worker6)
#manager2.add_team_member(designer3)
#manager2.add_team_member(designer4)
#manager2.add_team_member(designer5)
#manager2.add_team_member(designer6)
#
#manager3.add_team_member(worker7)
#manager3.add_team_member(worker8)
#manager3.add_team_member(worker9)
#manager3.add_team_member(worker10)
#manager3.add_team_member(worker6)
#manager3.add_team_member(designer1)
#manager3.add_team_member(designer2)
#manager3.add_team_member(designer3)
#manager3.add_team_member(designer4)
#manager3.add_team_member(designer5)
#manager3.add_team_member(designer6)
#
#department1 = Department([manager1,manager2,manager3])
##department1 = Department([manager1,manager2,manager3,manager4])
## department1.give_salary()
#department2 = Department([manager1])
#department2.give_salary()
##department2.add_to_team_members(manager1,[worker3,worker4])
##department2.add_to_team_members(manager1,[])
#department2.add_to_team_members(manager1,[worker3,worker4,manager4])
#department2.give_salary()
#print(worker1)
#print(manager3)
#print(designer6)
