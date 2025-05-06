import random, inspect
from datetime import timedelta, time
from globals import random_names, random_players, get_time, set_time, enter

class Person:     
    def __init__(self,name):
        self.name= name
        self.money= random.randint(50, 100)  # wasnt defined an starting value so i randomized them
        self.mood= "Content" 
        self.healthRate= random.choice([50, 75, 100])

    def sleep(self,hours):
        current_time = get_time()
        new_time = current_time + timedelta(hours=hours) #adds sleeping time to the time variable
        set_time(new_time)
        print("Sleeping...........................")
        if hours == 7:
            self.mood= "Happy"
            print(f"{self.name} Slept {hours} hours and woke up at {new_time} feeling {self.mood}")
        elif hours < 7:
            self.mood= "Tired"
            print(f"{self.name} Slept {hours} hours and woke up at {new_time} feeling {self.mood}")
        elif hours > 7:
            self.mood= "Lazy"
            print(f"{self.name} Slept {hours} hours and woke up at {new_time} feeling {self.mood}")
        set_time(new_time + timedelta(minutes=30)) # i usually take up to 30 min to get ready for leaving
        print(f"Off to Work at {get_time()}!")
        enter()
    
    def eat(self,meals):
        print("Eating...........................")
        current_time = get_time()
        new_time = current_time + timedelta(minutes=meals * 15) # eating usually takes about 15 min
        set_time(new_time)
        if meals == 3:
            self.healthRate = min(self.healthRate + 75, 100)
            print(f"{self.name} ate {meals} meals and his healthrate is now {self.healthRate}, it's {new_time} ")
        elif meals == 2:
            self.healthRate = min(self.healthRate + 50, 100)
            print(f"{self.name} ate {meals} meals and his healthrate is now {self.healthRate}, it's {new_time}  ")
        elif meals == 1:
            self.healthRate = min(self.healthRate + 25, 100)
            print(f"{self.name} ate {meals} meals and his healthrate is now {self.healthRate}, it's {new_time}  ")
        enter()
    
    def buy(self,items):
        current_time = get_time()
        new_time = current_time + timedelta(minutes=10*items) #buying usually takes about 10 min
        set_time(new_time)
        print(f"{self.name} counted his money and it was {self.money}")
        self.money= self.money-(10*items)
        print(f"{self.name} bought {items} items and now has {self.money}, it's now {new_time}")
        enter()

class Employee(Person):
    def __init__(self, name,car):
        super().__init__(name)
        self.id= ""
        self.car= car
        self.email=""
        self.salary= ""
        self.distanceToWork=""
    
    def work(self,hours):
        current_time = get_time()
        new_time = current_time + timedelta(hours=hours) #adds working hours to time variable
        set_time(new_time)
        print("Working..........................................")
        if hours == 8:
            self.mood = "Happy"
            self.healthRate -= 25 # usually work affects your health, so i added it
            print(f"{self.name} finished work on time ({new_time}) and is {self.mood}, his healthrate is now: {self.healthRate}")
        elif hours > 8:
            self.mood = "Tired"
            self.healthRate -= 50
            print(f"{self.name} overworked to ({new_time}) and he is {self.mood}, his healthrate is now: {self.healthRate}")
        elif hours < 8:
            self.mood = "Lazy"
            print(f"{self.name} worked incompetently to ({new_time}) and he is {self.mood}, his healthrate didnt change")
        self.money+= self.salary
        print(f"{self.name} recieved {self.salary}$, and now has a total of {self.money}\nTime to go home!")
        enter()

    def drive(self, distance, velocity):
        print(f"Driving..............................")
        current_time = get_time()
        rem = self.car.run(velocity, distance)
        if rem > 0:
            cost_to_refuel = 1.25 * rem # a liter probably costs 1.25, i dont drive
            if self.money >= cost_to_refuel:
                print(f"Not enough fuel to reach destination. Need to refuel {rem} liters costing ${cost_to_refuel:.2f}.")
                self.refuel(rem)
                rem_after_refuel = self.car.run(velocity, rem)
                if rem_after_refuel > 0:
                    print(f"Still not enough fuel after refuel! {rem_after_refuel} km left.")
                    print("Journey cannot continue further.")
                else:
                    new_time = current_time + timedelta(minutes=90) # it probably takes +30 min to refuel
                    set_time(new_time)
                    print(f"{self.name} arrived after refueling at {new_time}\n")
            else:
                print(f"Not enough money to refuel. Cannot continue journey.")
        else:
            new_time = current_time + timedelta(hours=1) #suppose the journey takes an hour
            set_time(new_time)
            print(f"{self.name} arrived at {new_time}")
        enter()
    
    def refuel(self, gas):
        added_fuel = gas + 10
        self.car.fuelRate += added_fuel
        cost = 1.25 * gas
        self.money -= cost
        print(f"\nRefueling... Added {added_fuel} liters ({gas} liters + 10 buffer).")
        print(f"Car now has: {self.car.fuelRate} liters.")
        print(f"{self.name} now has: ${self.money:.2f} left.\n")
        print("Continue driving........")

class Office():
    def __init__(self,name):
        self.name = name
        self.employees= {}  #npc employees
        self.employee_objects = {}   #player employees
        global random_names
        self.employeesnumber = random.randint(20,25) # an office usually has 20-25 employees
        for i,name in enumerate(random.sample(random_names,self.employeesnumber), start=1):
            self.employees[i] = name
    
    def all_employees(self):
        print(f"There are currently {len(self.employees)} employees working in {self.name}\n{self.employees}\n")
    
    def get_employee(self,id):
        try:
            found = self.employees.get(id)
            called = inspect.stack()[1].function
            if called == "<module>": # should only be printed if the parent isnt a function?
                print(f"The employee with the id of {id} is: {found}")
            return found
        except:
            print("No employees found\n")
    
    def hire(self, employee):
        if isinstance(employee, Employee): #checks if the employee passed is an instance from the class employee
            name = employee.name
            self.employee_objects[name] = employee
        else:
            name = employee

        if name in self.employees.values():
            print(f"{name} is already working in {self.name}")
        else:
            self.employeesnumber += 1
            self.employees[self.employeesnumber] = name
            print(f"Congrats, {self.name} just hired {name}")

    def fire(self,id):
        try:
            found = self.get_employee(id)
            self.employees.pop(id)
            print(f"{self.name} just fired {found}!\nEverything happens for a reason")
        except AttributeError:
            print(f"{self.name} doesn't have an employee named: {found}!\n")
        enter()
        
    def deduct(self, id, amount):
        name = self.employees.get(id)
        if name:
            if name in self.employee_objects:
                self.employee_objects[name].salary -= amount
                print(f"{self.name} just deducted {amount} from {name}, Time to work harder\n")
            else:
                print(f"{name} is not a real employee (object), cannot deduct money.\n")
        else:
            print(f"{self.name} doesn't have an employee with id: {id}!\n")
        enter()
            
    def reward(self, id, amount):
        name = self.employees.get(id)
        if name:
            if name in self.employee_objects:
                self.employee_objects[name].salary += amount
                print(f"{self.name} just rewarded {amount}$ to {name}!, Great Job\n")
            else:
                print(f"{name} is not a real person employee (not an object), cannot reward money.\n")
        else:
            print(f"{self.name} doesn't have an employee with id: {id}!\n")
        enter()
    
    def check_lateness(self,id):
        current_time = get_time().time()
        start= time(9,0)
        self.get_employee(id)
        if current_time > start:
            print("For arriving late")
            self.deduct(id,10)
        else:
            print("For arriving early")
            self.reward(id,10)
    
    def work_events(self):  # random work events for randmoized mode and custom player mpde
        print("What happened at work today:\n")
        for _ in range(2):
            x= random.randint(1,4)
            if x==1:
                print("reviewed the company's employees database")
                self.all_employees()
            elif x==2:
                print("Had a nice chat with a coworker")
                print(self.get_employee(random.randint(1,self.employeesnumber))) 
            elif x==3:
                print("Someone got hired today")
                self.hire(random_names[random.randint(0,len(random_players))])
            elif x==4:
                print("Someone got fired today")
                self.fire(random.randint(1,self.employeesnumber))

class Car:
    def __init__(self,name):
        self.name= name
        self.fuelRate = 100
        self.velocity = 0
    
    def run(self, velocity, distance):
        self.velocity = velocity  
        print(f"Car is running at {self.velocity} km/h")
        fuel_needed = distance

        if fuel_needed > self.fuelRate:
            remaining_distance = fuel_needed - self.fuelRate
            self.fuelRate = 0 
            print("Fuel empty!")
            self.stop(remaining_distance)
            return remaining_distance  
        else:
            self.fuelRate -= fuel_needed
            print(f"Reached destination, remaining fuel: {self.fuelRate} liters")
            return 0

    def stop(self, remaining_distance):
        self.velocity = 0
        print(f"Car stopped with {remaining_distance} km left to destination.")