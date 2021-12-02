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
alarm1 = fire_alarm("On","Temperature Sensor","Kitchen",25)
object_list = [cctv,vacuum_cleaner,heater,living_lights,outdoor_lights,main_door,bhk_safe,garage,gate,AC1,AC2,alarm1]
#all objects are added into a list to make the program less complicated in 2nd commit

#now the menu
#code under choices were similar when they are under same class, so let's make a common one for them!
#shorter codes are more faster and efficient, therefore provides better performance!

choice = 1
while choice != 13:
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
    print("Option - 12: Alarm")
    print("Option - 13: Exit")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    
    choice = int(input("Enter Option:"))
    
    if choice in [1,2,3]: #since these 3 objects are under same class, same code will work for all of them
        print(object_list[choice-1].__str__()) #will put object name before the function call
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(object_list[choice-1].change_state())
        else:
            print("No changes done")
            
    elif choice in [4,5]: #both under Lighting class
        print(object_list[choice-1]. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Increase Brightness")
        print("Option - 3: Decrease Brightness")
        print("*******************************")
        light_choice = int(input("Enter Option:"))
        if light_choice == 1:
            print(object_list[choice-1].change_state())
        elif light_choice == 2:
            print(object_list[choice-1].increase_brightness())
        elif light_choice == 3:
            print(object_list[choice-1].decrease_brightness())
        else:
            print("Invalid Option")
            
    elif choice in [6,7]: #both under security_lock class
        print(object_list[choice-1]. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Lock/Unlock")
        print("*******************************")
        lock_choice = int(input("Enter Option:"))
        if lock_choice == 1:
            print(object_list[choice-1].change_state())
        elif lock_choice == 2:
            print(object_list[choice-1].change_security())
        else:
            print("Invalid Option")
            
    elif choice in [8,9]:
        print(object_list[choice-1].__str__())
        changestate = input("Do you wish to turn this device On/Off? [y/n]: ")
        if changestate in ["Y","y"]:
            print(object_list[choice-1].change_state())
        else:
            print("No changes done")
            
    elif choice in [10,11]:
        print(object_list[choice-1]. __str__())
        print("*******************************")
        print("Option - 1: Turn On/Off")
        print("Option - 2: Increase Temperature")
        print("Option - 3: Decrease Temperature")
        print("*******************************")
        temp_choice = int(input("Enter Option:"))
        if temp_choice == 1:
            print(object_list[choice-1].change_state())
        elif temp_choice == 2:
            print(object_list[choice-1].increase_temp())
        elif temp_choice == 3:
            print(object_list[choice-1].decrease_temp())
        else:
            print("Invalid Option") 
    elif choice == 12:
        print(object_list[choice-1]. __str__())
    elif choice not in range(1,14):
        print("Invalid Option")
