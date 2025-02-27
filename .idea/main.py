# import random
# class Human:
#     def __init__(self, name="Human", job=None, home=None, car=None):
#         self.name = name
#         self.money = 100
#         self.gladness = 50
#         self.satiety = 50
#         self.job = job
#         self.car = car
#         self.home = home
#     def get_home(self):
#         self.home = House()
#     def get_car(self):
#         self.car = Auto(brands_of_car)
#     def get_job(self):
#         if self.car.drive():
#             pass
#         else:
#             self.to_repair()
#             return
#         self.job = Job(job_list)
#
#     def eat(self):
#         if self.home.food <= 0:
#             self.shopping("food")
#         else:
#             if self.satiety >= 100:
#                 self.satiety = 100
#                 return
#             self.satiety += 5
#             self.home.food -= 5
#
#     def work(self):
#         if self.car.drive():
#             pass
#         else:
#             if self.car.fuel < 20:
#                 self.shopping("fuel")
#                 return
#             else:
#                 self.to_repair()
#                 return
#             self.money += self.job.salary
#             self.gladness -= self.job.gladness_less
#             self.satiety -= 4
#     def shopping(self, manage):
#         if self.car.drive():
#             pass
#         else:
#             if self.car.fuel < 20:
#                 manage = "fuel"
#             else:
#                 self.to_repair()
#                 return
#         if manage == "fuel":
#             print("I bought fuel")
#             self.money -= 100
#             self.car.fuel += 100
#         elif manage == "food":
#             print("Bought food")
#             self.money -= 50
#             self.home.food += 50
#         elif manage == "delicacies":
#             print("Hooray! Delicious!")
#             self.gladness += 10
#             self.satiety += 2
#             self.money -= 15
#     def chill(self):
#         self.gladness += 10
#         self.home.mess += 5
#     def clean_home(self):
#         self.gladness -= 5
#         self.home.mess = 0
#     def to_repair(self):
#         self.car.strength += 100
#         self.money -= 50
#     def days_indexes(self, day):
#         day = f" Today the {day} of {self.name} 's life "
#         print(f"{day:=^50}", "\n")
#         human_indexes = self.name + "'s indexes"
#         print(f"{human_indexes:^50}", "\n")
#         print(f"Money – {self.money}")
#         print(f"Satiety – {self.satiety}")
#         print(f"Gladness – {self.gladness}")
#         home_indexes = "Home indexes"
#         print(f"{home_indexes:^50}", "\n")
#         print(f"Food – {self.home.food}")
#         print(f"Mess – {self.home.mess}")
#         car_indexes = f"{self.car.brand} car indexes"
#         print(f"{car_indexes:^50}", "\n")
#         print(f"Fuel – {self.car.fuel}")
#         print(f"Strength – {self.car.strength}")
#     def is_alive(self):
#         if self.gladness < 0:
#             print("Depression...")
#             return False
#         if self.satiety < 0:
#             print("Dead...")
#             return False
#         if self.money < -500:
#             print("Bankrupt...")
#             return False
#     def live(self, day):
#         if self.is_alive() == False:
#             return False
#         if self.home is None:
#             print("Settled in the house")
#             self.get_home()
#         if self.car is None:
#             self.get_car()
#             print(f"I bought a car {self.car.brand}")
#         if self.job is None:
#             self.get_job()
#             print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
#         self.days_indexes(day)
#         dice = random.randint(1, 4)
#         if self.satiety < 20:
#             print("I'll go eat")
#             self.eat()
#         elif self.gladness < 20:
#             if self.home.mess > 15:
#                 print("I want to chill, but there is so much mess...")
#                 self.clean_home()
#             else:
#                 print("Let`s chill!")
#                 self.chill()
#         elif self.money < 0:
#             print("Start working")
#             self.work()
#         elif self.car.strength < 15:
#             print("I need to repair my car")
#             self.to_repair()
#         elif dice == 1:
#             print("Let`s chill!")
#             self.chill()
#         elif dice == 2:
#             print("Start working")
#             self.work()
#         elif dice == 3:
#             print("Cleaning time!")
#             self.clean_home()
#         elif dice == 4:
#             print("Time for treats!")
#             self.shopping(manage="delicacies")
#
# class Auto:
#     def __init__(self, brand_list):
#         self.brand = random.choice(list(brand_list))
#         self.fuel = brand_list[self.brand]["fuel"]
#         self.strength = brand_list[self.brand]["strength"]
#         self.consumption =brand_list[self.brand]["consumption"]
#
#     def drive(self):
#         if self.strength > 0 and self.fuel >= self.consumption:
#             self.fuel -= self.consumption
#             self.strength -= 1
#             return True
#         else:
#             print("The car cannot move")
#             return False
#
# class House:
#     def __init__(self):
#         self.mess = 0
#         self.food = 0
#
# job_list = {
# "Java developer": {"salary":50, "gladness_less": 10 },
# "Python developer": {"salary":40, "gladness_less": 3 },
# "C++ developer": {"salary":45, "gladness_less": 25 },
# "Rust developer": {"salary":70, "gladness_less": 1 },
# }
#
# brands_of_car = {
# "BMW":{"fuel":100, "strength":100, "consumption": 6},
# "Lada":{"fuel":50, "strength":40, "consumption": 10},
# "Volvo":{"fuel":70, "strength":150, "consumption": 8},
# "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
# }
#
# class Job:
#     def __init__(self, job_list):
#         self.job = random.choice(list(job_list))
#         self.salary = job_list[self.job]["salary"]
#         self.gladness_less = job_list[self.job]["gladness_less"]
#
# roman = Human(name="Nick")
# for day in range(1,8):
#     if roman.live(day) == False:
#         break

# class Human:
#     height = 170
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# nick = Student()
# ann = Worker()
# print(nick.satiety)
# print(ann.satiety)
#

# class Granparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Granparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
# nick = Child()

# class Computer:
#     def __init__(self):
#         self.memory = 128
#
# class Display:
#     def __init__(self):
#         self.resolution = "4K"
#
# class SmartPhone(Display ,Computer):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
#
# iphone = SmartPhone()
# iphone.print_info()

# my_list = [1, 2, 3]
# iterator = iter(my_list)
#
# for elem in iterator:#одноразовий об'єкт
#     print(elem)
# # print(next(interator))
# # print(next(interator))#наступна ітерація
# #

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(5)
# # for elem in count:
# #     print(elem)
#     print()
#

#Генератор

# def raise_to_the_degrees(number):
#     i = 0
#     # for _ in range (max_degree):
#     while True:
#         yield number **i
#         i += 1
#
# res = raise_to_the_degrees(122345)
# print(res)
# for _ in res:
#     print(_)

# class Helper:
#     def __init__(self, work):
#         self.work = work
#
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help you with {work}"
#
# helper = Helper("homework")
# print(helper("cleaning"))

# def helper(work):
#     work_in_memory = work
#
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
#     return helper
#
# helper= helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

# words = ["Собака", "Меркурій", "Воларбебе", "Телефон", "Книга"]
# iterator = iter(words)
# for word in iter(words):
#     print(f"{word}: {len(word)} Букв.")

# def three():
#     for i in range(21):
#         yield f"3^{i}={3 ** i}"
# for i in three():
#         print(i)

#Декоратори
# def checker (function):
#     def checker( *args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print("We have problem {exc}")
#         else:
#             print("No problem. Result - {result}")
#     return checker()
#
# @checker
#
# def calculate(expression):
#     return eval(expression)
# calculate("2+2")

# def checker(*exc_types):
#     def checker(function):
#         def checker(*args, **kwargs):
#             try:
#                 result = function(*args, **kwargs)
#             except exc_types as exc:
#                 print(f"We have problems {exc}")
#             else:
#                 print(f"No problem. Result - {result}")
#
#         return checker
#     return checker
#
#
# @checker(NameError, TypeError, SyntaxError)
# def calculate(expression):
#     return eval(expression)
# calculate("2+2")

# class Checker:
#     def __init__(self, *exc_types):
#         self.exc_types = exc_types
#     def __call__(self, function):
#         def error(*args, **kwargs):
#             try:
#                 result = function(*args, **kwargs)
#             except self.exc_types as exc:
#                 print(f"We have problems: {exc}")
#             else:
#                 print(f"No problem, result:{result}")
#                 return result
#         return error
# @Checker(Exception)
# def calculate(expression):
#     return eval(expression)
# calculate("2+2")


# #1
#
# class Car:
#     make = 'Audi'
#     model = 'E-tron'
#     year = 2021
#
# get_info = (Car.make,Car.model,Car.year)
# print(get_info)

#2

# class employee:
#  def __init__(self,name,position,salary):
#   self.name = name
#   self.position = position
#   self.salary = salary
#
#
# class department:
#  def __init__(self, name):
#   self.name = name
#   self.employees = []
#
#  def add_employees(self, employee):
#   self.employees.append(employee)
#
#   def remove_employee(self, employee_name):
#    for employee in self.employees:
#     if employee.name == employee_name:
#      self.employees.remove(employee)
#      break
#
#   def all_salaries(self):
#    all_salaries = 0
#    for employee in self.employees:
#     all_salaries += employee.salary
#    return all_salaries
#
#   def list_of_employees(self):
#    return self.employees


#3

# class Device:
#     def on(self):
#         print("Device is on")
#
#     def off(self):
#         print("Device is off")
#
# class Mouse(Device):
#     pass
#
# class PC(Device):
#     pass
#
# class Clock(Device):
#     pass
#
#
# print("Mouse")
# tv = PC()
# tv.on()
# tv.off()
# print("-")
# print("PC")
# phone = Clock()
# phone.on()
# phone.off()
# print("-")
# print("Clock")
# laptop = Mouse()
# laptop.on()
# laptop.off()






#4

# import random
# abc = list("абвгґдежзийклмнопрстуфхцчшщьюя")
# def generator_randomnih_liter():
#     return [random.choice(abc) for _ in range(1)]
# random_letters = generator_randomnih_liter()
# print(f"{random_letters}")
