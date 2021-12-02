
'''This program creates a class called IoT under which several sub-classes are created.
All the devices under IoT must have a state[On/Off], a name and its location.
Devices under sub-classes may have additional details or functions.'''

'''No extra security is provided under these classes and their functions since it is assumed that
in real-life, one has to provide an admin name and password in order to get access to change
the device details [working of IoT was learnt in "Introduction to packet Tracer" course from
Cisco Networking Academy.]'''

class IoT(): 
     def __init__(self, state, name, location): 
        self.state = state #state can be on or off
        self.name = name #name of device
        self.location = location #location of device
     def __str__(self):
          return f'IoT device {self.name} located in {self.location}'\
                 f' is {self.state}' #returns details of device
     def change_state(self): #works like a button
          if self.state in ["On","on"]:
            self.state = "Off"
            return f'{self.name} has been turned off'
          elif self.state in ["Off","off"]:
            self.state = "On"
            return f'{self.name} has been turned on'

class Lighting(IoT): #controls lighting in and around house
     def __init__(self, state, name, location, brightness): #brightness can be 1,2 or 3[dim to bright] or 0[if device is off]
        super().__init__(state, name, location) #makes actions under main class happen here too
        if self.state in ["On","on"]:
            self.brightness = brightness
        elif self.state in ["Off","off"]: #even if user types 1/2/3, it wouldn't make sense if device is off
            self.brightness = 0
     def __str__(self):
        return super().__str__() + f' with brightness set to {self.brightness} '#returns brightness along with main class details
     def increase_brightness(self):
        if self.state in ["On","on"]:
             if self.brightness < 3: #if brightness was below hightest value
                 self.brightness += 1
                 return f'{self.name} brightness has been changed to {self.brightness}'
             elif self.brightness == 3:
                 return f'{self.name} brightness is 3 [highest]' #even if we keep clicking higher, the highest stays the same, right?
        elif self.state in ["Off","off"]:
            return f'Sorry, {self.name} is off'
     def decrease_brightness(self):
        if self.state in ["On","on"]:
            if self.brightness > 1: #if brightness was above lowest value
                 self.brightness -= 1
                 return f'{self.name} brightness has been changed to {self.brightness}'
            elif self.brightness == 1:
                 return f'{self.name} brightness is 1 [lowest]'
        elif self.state in ["Off","off"]:
            return f'Sorry, {self.name} is off'
