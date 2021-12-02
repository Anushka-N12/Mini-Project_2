#Let's make a menu to easily use the functions!

from IoT_Lighting import *
from Other_classes import *
#above .py files contain the classes

#will first create all IoT devices of the house
cctv = IoT("On","CCTV","Entrance")
vacuum_cleaner = IoT("On","Robotic Vacuum Cleaner","Living Room")
heater = IoT("Off","Water Heater","Bathroom")
living_lights = Lighting("On","Standard Lighting","Living Room",2)
outdoor_lights = Lighting("On","Garden Lights","Outdoors",1)
main_door = security_lock("On","Main door lock","Entrance","Locked")
bhk_safe = security_lock("On","Lock of safe","Bedroom","Unlocked")
garage = door_vehicle("On","Garage door","Garage", 199)
gate = door_vehicle("On","Main Gate","Entrance of property", 250)
AC1 = AC("On","AC","Bedroom 1",24)
AC2 = AC("On","AC","Bedroom 2",66)

#now the menu
choice = 1
while choice != 12:
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("*         SMART HOME          *")
    print("*******************************")
    print("Option - 1: CCTV")
    print("Option - 2: Robotic Vacuum Cleaner")
    print("Option - 3: Water Heater")
    print("Option - 4: Standard Lighting")
    print("Option - 5: Garden Lights")
    print("Option - 6: Main Door Lock")
    print("Option - 7: Lock of Safe")
    print("Option - 8: Garage Door")
    print("Option - 9: Main Gate")
    print("Option - 10: AC1")
    print("Option - 11: AC2")
    print("Option - 12: Exit")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    choice = int(input("Enter Option:"))
    if choice == 1:
        print(cctv.__str__())
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(cctv.change_state())
        else:
            print("No changes done")
    elif choice == 2:
        print(vacuum_cleaner.__str__())
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(vacuum_cleaner.change_state())
        else:
            print("No changes done")
    elif choice == 3:
        print(heater.__str__())
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(heater.change_state())
        else:
            print("No changes done")
            
    elif choice == 4:
        print(living_lights. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Increase Brightness")
        print("Option - 3: Decrease Brightness")
        print("*******************************")
        light_choice = int(input("Enter Option:"))
        if light_choice == 1:
            print(living_lights.change_state())
        elif light_choice == 2:
            print(living_lights.increase_brightness())
        elif light_choice == 3:
            print(living_lights.decrease_brightness())
        else:
            print("Invalid Option")    
    elif choice == 5:
        print(outdoor_lights. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Increase Brightness")
        print("Option - 3: Decrease Brightness")
        print("*******************************")
        light_choice = int(input("Enter Option:"))
        if light_choice == 1:
            print(outdoor_lights.change_state())
        elif light_choice == 2:
            print(outdoor_lights.increase_brightness())
        elif light_choice == 3:
            print(outdoor_lights.decrease_brightness())
        else:
            print("Invalid Option") 
    elif choice == 6:
        print(main_door. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Lock/Unlock")
        print("*******************************")
        lock_choice = int(input("Enter Option:"))
        if lock_choice == 1:
            print(main_door.change_state())
        elif lock_choice == 2:
            print(main_door.change_security())
        else:
            print("Invalid Option")
    elif choice == 7:
        print(bhk_safe. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Lock/Unlock")
        print("*******************************")
        lock_choice = int(input("Enter Option:"))
        if lock_choice == 1:
            print(bhk_safe.change_state())
        elif lock_choice == 2:
            print(bhk_safe.change_security())
        else:
            print("Invalid Option")
    elif choice == 8:
        print(garage.__str__())
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(garage.change_state())
        else:
            print("No changes done")
    elif choice == 9:
        print(gate.__str__())
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(gate.change_state())
        else:
            print("No changes done")
    elif choice == 10:
        print(AC1. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Increase Temperature")
        print("Option - 3: Decrease Temperature")
        print("*******************************")
        temp_choice = int(input("Enter Option:"))
        if temp_choice == 1:
            print(AC1.change_state())
        elif temp_choice == 2:
            print(AC1.increase_temp())
        elif temp_choice == 3:
            print(AC1.decrease_temp())
        else:
            print("Invalid Option") 
    elif choice == 11:
        print(AC2. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Increase Temperature")
        print("Option - 3: Decrease Temperature")
        print("*******************************")
        temp_choice = int(input("Enter Option:"))
        if temp_choice == 1:
            print(AC2.change_state())
        elif temp_choice == 2:
            print(AC2.increase_temp())
        elif temp_choice == 3:
            print(AC2.decrease_temp())
        else:
            print("Invalid Option") 
    elif choice not in range(1,13):
        print("Invalid Option")
