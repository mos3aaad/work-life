from funcs import example, randomized, custom

def menu():
    while True:
        print("Welcome to Story Time!\n\n1.ITI Example Story (Functionality Preview)\n2.Randomized Story\n3.Play your Story\n4.Quit")
        try:
            k = int(input("Choose from (1-4): \n"))
            if k == 1:
                example()  # the example story (samy) for the project
            if k == 2:
                randomized() #random story generated 
            if k == 3:
                custom() # create a story
            if k == 4:
                print("See you later!")
                exit()
        except ValueError:
            k = print("Invalid entry")
            
menu()
               