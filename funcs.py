import random
from myclass import Person, Employee, Office, Car
from globals import random_names, random_players, company_names, car_names, get_time, set_time, enter
from datetime import timedelta

################################ MAIN MENU FUNCTIONS ############################################
def example():
    car = Car("fiat 128")
    Samy = Employee("Samy", car)
    Iti= Office("ITI Smart Village")
    car.fuelRate = 50
    Samy.money, Samy.healthRate = 100, 100
    #introduction
    print(f"Our story follows the life of {Samy.name} who just got hired by the ITI, Samy ownes a {Samy.car.name}\nIt's Now {get_time()}")
    print(f"{Samy.name} has {Samy.money}$, his healthrate is {Samy.healthRate} and he is {Samy.mood}")
    enter()  
    #first day events
    Iti.hire(Samy)
    Samy.id,Samy.email, Samy.salary, Samy.distanceToWork=Iti.employeesnumber, Samy.name.replace(" ", "").lower()+"@"+Iti.name.replace(" ", "").lower()+ ".com", 150, 20
    print(f"Assigned ID: {Samy.id}, Distance to the office is {Samy.distanceToWork}km, his email is now: {Samy.email}, his salary is: {Samy.salary}$\n") 
    #routine
    Samy.eat(1)
    Samy.sleep(7)
    Samy.drive(Samy.distanceToWork, 80)
    Iti.check_lateness(Samy.id)
    Iti.all_employees()
    Samy.work(11)
    Samy.drive(Samy.distanceToWork, 80)
    Samy.buy(4)
    Samy.eat(2)
    #second day
    Samy.sleep(12)
    Samy.drive(Samy.distanceToWork, 80)
    Iti.check_lateness(Samy.id)
    print(Iti.employees.get(Samy.id))
    Iti.deduct(Iti.employeesnumber,60)
    Samy.work(6)
    Samy.drive(Samy.distanceToWork, 80)
    Samy.eat(1)
    #third day
    Samy.sleep(6)
    Samy.buy(1)
    Samy.eat(1)
    Samy.drive(Samy.distanceToWork, 80)
    Iti.check_lateness(Samy.id)
    Iti.reward(Iti.employeesnumber,60)
    Samy.work(8)
    Iti.fire(6)

def randomized():
    car = Car(random.choice(car_names))
    Player = Employee(random.choice(random_players), car)
    company = Office(random.choice(company_names))
    #introduction
    print(f"Our story today follows {Player.name}, who just got hired by {company.name} and owns a {Player.car.name}.")
    print(f"It's now {get_time()}. {Player.name} has ${Player.money}, health rate {Player.healthRate}, and feels {Player.mood}.")
    enter()
    #first day events
    company.hire(Player)
    Player.id = company.employeesnumber
    Player.email = Player.name.lower() + "@" + company.name.replace(" ", "").lower() + ".com"
    Player.salary = random.randint(100, 300)
    Player.distanceToWork = random.randint(15, 30)
    print(f"Assigned ID: {Player.id}, Email: {Player.email}, Salary: {Player.salary}$, Distance to the office: {Player.distanceToWork} km\n")
    enter()

    def will_eat(): # function for random chance of eating
        y = random.randint(1,3)
        if y == 3:
            Player.eat(random.choice([1, 2, 3]))
    def will_buy(): # function for random chance of buying
        y = random.randint(1,3)
        if y == 3:
            Player.buy(random.choice([1, 2, 3]))
#routine
    g=0                    
    while g == 0:
        Player.sleep(random.randint(6,9))
        will_eat()
        will_buy() # chance for buying on way to work
        Player.drive(Player.distanceToWork, random.choice([60, 80, 100]))
        company.check_lateness(Player.id)
        company.work_events() # chance for choosing 2 random events from work
        Player.work(random.choice([7, 8, 9]))
        Player.drive(Player.distanceToWork, random.choice([60, 80, 100]))
        will_buy() # chance for buying on way to home
        Player.eat(random.choice([1, 2, 3]))
        try:
            gen = input("Would you like to generate a new day? (y/n)\n").lower()
            if gen == "n" or gen == "no":
                g = 1
        except:
            print("No decline was entered, Generating a new day")

def custom():
    while True:
        name = input("What's your name? ")
        len(name)
        if len(name) == 0:
            print("Your name cant be empty")
        else:
            break
    while True:
        car_name = input("What car do you drive? ")
        if len(car_name) == 0:
            print("Your car name cant be empty")
        else:
            break
    while True:
        company_name = input("What's your company's name? ")
        if len(name) == 0:
            print("Your company name cant be empty")
        else:
            break
        
    car = Car(car_name)
    you = Employee(name, car)
    company = Office(company_name)
    #introduction
    print(f"\nWelcome, {you.name}, you own a {car.name} and you're about to start your story.\nit's {get_time()} now")
    enter()
    #first day events
    company.hire(you)
    you.id = company.employeesnumber
    you.email = you.name.lower() + "@" + company.name.replace(" ", "").lower() + ".com"
    you.salary = random.randint(150, 250)
    you.distanceToWork = random.randint(10, 40)
    print(f"Assigned ID: {you.id}, Email: {you.email}, Salary: ${you.salary}, Distance to the office: {you.distanceToWork} km\n")
    enter()
    #main game
    g= 0
    while g == 0:
        try:
            print("What to do next?")
            do = int(input("1.Sleep        2.Eat        3.Buy Something        4.Go to Work        5.Pass time        6.Show Status        7.Quit Story\n"))
            if do == 1:
                try:
                    sleep_hours = int(input("How many hours will you sleep?  "))
                    you.sleep(sleep_hours)
                except:
                    print("Invalid entry, returning to menu")
            elif do == 2:
                try:
                    meals = int(input("How many meals will you eat? (1-3): "))
                    you.eat(meals)
                except:
                    print("Invalid entry, returning to menu")
            elif do == 3:
                try:
                    items = int(input("How many items will you buy? "))
                    you.buy(items)
                except:
                    print("Invalid entry, returning to menu")
            elif do == 4:
                if (6 <= get_time().hour <= 12):
                    you.drive(you.distanceToWork,80)
                    company.check_lateness(you.id)
                    company.work_events()
                    you.work(random.choice([7, 8, 9]))
                    you.drive(you.distanceToWork,80)
                else:
                    print("You can't leave for work before 6 AM or after 12PM, returning to menu")
            elif do == 5:
                try:
                    hours = int(input("How many hours do you want to pass? "))
                    new_time = get_time() + timedelta(hours=hours)
                    set_time(new_time)
                    print(f"You managed to kill {hours} hours, it's now: {new_time}")
                except:
                    print("Invalid entry, returning to menu")
            elif do == 6:
                print(f"Hello {you.name}, it's currently {get_time()}")
                print(f"Mood: {you.mood}\nMoney: {you.money}$\nHealth Rate: {you.healthRate}/100")
                print(f"Company: {company.name}\nAssigned ID: {you.id}\nEmail: {you.email}\nSalary: {you.salary}$")
            elif do == 7:
                g=1
                break
        except:
            print("Invalid entry, try again")