#Let's test all the classes we made!

from IoT_Lighting import *
from Other_classes import *
#above .py files contain the classes

#Let's test the main IoT class!
cctv = IoT("On","CCTV","Entrance")
print(cctv.__str__()) #prints device details
vacuum_cleaner = IoT("On","Robotic Vacuum Cleaner","Living Room")
heater = IoT("Off","Water Heater","Bathroom")
print(vacuum_cleaner.__str__())
print(vacuum_cleaner.change_state()) #like pressing a button
print(vacuum_cleaner.__str__())
print(heater.__str__())
print()

#Let's test the Lighting class!
living_lights = Lighting("On","Standard Lighting","Living Room",2)
outdoor_lights = Lighting("On","Garden Lights","Outdoors",1)
print(living_lights. __str__())
print(outdoor_lights.__str__())
print(living_lights.change_state())
print(outdoor_lights.increase_brightness())
print()

#Let's test the security_lock class!
main_door = security_lock("On","Main door lock","Entrance","Locked")
bhk_safe = security_lock("On","Lock of safe","Bedroom","Unlocked")
print(main_door. __str__())
print(bhk_safe.__str__())
print(bhk_safe.change_security("Locked"))
print()

#Let's test the door_vehicle class!
garage = door_vehicle("On","Garage door","Garage", 199)
gate = door_vehicle("On","Main Gate","Entrance of property", 250)
print(garage.__str__())
print(gate.__str__())
print()

#Let's test the AC class!
AC1 = AC("On","AC","Bedroom 1",24)
AC2 = AC("On","AC","Bedroom 2",66)
print(AC1.__str__())
print(AC2.__str__())
print()

