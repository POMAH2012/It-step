#
#
# class Human:
#     def __init__(self, name = "Human"):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passenger = []
#
#     def add_passenger(self, *args): #реєтрує пасажирів авто
#         for passenger in args:
#             self.passenger.append(passenger)
#
#     def print_passenger_names(self):
#         if self.passenger != []:
#             print("Names of {self.brand} passenger: ")
#             for passenger in self.passenger:
#                 print(passenger.name)
#         else:
#             print("There are no passenger in {self.brand} ")
# nick = Human("Nick")
# kate = Human("Kate")
# car = Auto("Audi")
# car.add_passenger(nick, kate)
# car.print_passenger_names()

import random
class Human:

    def __init__(self, name ="Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satierty = 50
        self.job = job
        self.car = car
        self.homa = home


    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            ...
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.eat():
            self.eat = 0
            self.eat += 100
    def work(self):
        ...
    def schopping(self):
        ...
    def chill(self):
        ...
    def clean_home(self):
        ...
    def to_repair(self):
        ...

    def days_indexes(self, day):
        ...
    def is_alive(self):
        ...
    def live(self, day):
        ...


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consuption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel>=self.consuption:
            self.fuel-=self.consuption
            self.strenght -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0



brands_of_car = {
        "Buggati":{"fuel": 100, "strenght": 110, "consumption":6},
        "Bobik":{"fuel": 40, "strenght": 10, "consumption":7},
        "Lada":{"fuel": 20, "strenght": 10, "consumption":4},
        "Reno": {"fuel": 60, "strenght": 70, "consumption": 9},

}

job_list = {
    "Army": {"salary" : 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "Actor": {"salary": 45, "gladness_less": 25},
    "Streamer": {"salary": 70, "gladness_less": 1},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"] #зарплата
        self.gladness_less = job_list[self.job]["gladness_less"] #трата радості


