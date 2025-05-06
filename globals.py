from datetime import datetime
import msvcrt
################################ GLOBAL VARIABLES ###############################################
random_names=["Alice","Bob","Elyse ","Vaughn","Helena ","Sierra","Remy","Dayton","Doyle","Jordan","Adalynn","Marshall",
              "Annalise","Washington","Jaylen","Jennings","Palmer","Lian","Tyler","Stephenson","Brayden","Hayley","Roth",
              "Patel","Parker","Schwartz"]  # random names used for npc employee names
random_players = ['Lilliana', 'Saunders', 'Scott', 'Aurora', 'Townsend', 'Moyer', 'Martin', 'Mateo'] # random names used as player for randomized mode
company_names = [
    "TechNova", "ByteWorks", "Apex Solutions", "Visionary Labs", "Quantum Systems",
    "SkyHigh Technologies", "Peak Enterprises", "InnovateX", "CyberSphere", "NextGen Corp",
    "Stellar Dynamics", "FutureSoft", "Alpha Innovations", "Nimbus Tech", "CoreLogic",
    "Titan Industries", "CloudCrest", "SwiftTech", "Bluewave Solutions", "Vertex Global"]# random names used as company for randomized mode
car_names = [
    "Toyota", "Ford", "Chevrolet", "Honda", "Mercedes-Benz",
    "BMW", "Audi", "Volkswagen", "Nissan", "Hyundai",
    "Kia", "Porsche", "Tesla", "Jaguar", "Land Rover",
    "Mazda", "Subaru", "Ferrari", "Lamborghini", "Volvo"] # random names used as car for randomized mode

timern = datetime(2025, 5, 3, 23, 0) # default start time for the story

################################ UTILITY FUNCTIONS ###############################################
def get_time(): # time variable getter
    global timern
    return timern

def set_time(new_time): # time variable setter
    global timern
    timern = new_time

def enter(): # promts user to press any key to contiune
    print("Press any key to continue...\n")
    msvcrt.getch()