from IoT_Lighting import * #IoT_Lighting.py file contains main class IoT
#Let's make some more classes for our smart home!

#below sub-class is meant to be used to lock/unlock devices for safety
class security_lock(IoT):
    def __init__(self, state, name, location, security): #security can be locked/unlocked
        super().__init__(state, name, location) #makes actions under main class happen here too
        if self.state in ["On","on"]:
            self.security = security
        elif self.state in ["Off","off"]:
            self.security = "Not secured" #lock doesn't function if its off
    def __str__(self):
        return super().__str__() + f' and is {self.security}' #returns device details
    def change_security(self): #to lock/unlock device
        if self.state in ["On","on"]: #device must be on to provide security
            if self.security == "Unlocked": #checks current state of security
                    self.security = "Locked"
                    return f'{self.name} is now {self.security}' #must assure user that action is done!
            elif self.security == "Locked":
                    self.security = "Unlocked"
                    return f'{self.name} is now {self.security}'
        elif self.state in ["Off","off"]:
            return f'Sorry, {self.name} is off' #doesn't function is device is off

#below class makes door open when vehicle is within the range of 200 metres
#below class may look similar to main class IoT but this one takes an additional parameter
class door_vehicle(IoT): 
    def __init__(self, state, name, location, distance_metre): #position[open/closed] decided based on vehicle distance from it
        super().__init__(state, name, location) #makes actions under main class happen here too
        self.distance_metre = distance_metre
    def __str__(self):
        if self.state in ["On","on"]:
            if self.distance_metre < 200: #when vehicle in near
                return super().__str__() + f' and has been opened'
            else:
                return super().__str__() + f' and remains closed.' #when no vehicle is close
        elif self.state in ["Off","off"]:
            return super().__str__() + f' and remains closed.' #doesn't function if its off
        
'''For the above class, one might worry if unknown vehicles can enter through the doors under this
class, since it is not checking vehicle plate numbers or doing any other type of check. One can simply
 just switch off that door and this will stop the door from opening even if there are vehicles uproaching.'''

#below class sets ac to mentioned temperature
class AC(IoT): 
    def __init__(self, state, name, location, temp_celcius): 
        super().__init__(state, name, location) #makes actions under main class happen here too
        self.temp_celcius = temp_celcius
    def __str__(self):
        if self.state in ["On","on"]:
            if self.temp_celcius > 10 and self.temp_celcius < 35: #ac can't be set to -100 or 200!
                return super().__str__() + f' and has been set to {self.temp_celcius}C.'
            else:
                self.temp_celcius = 24
                return super().__str__() + f' has been set to default 24C.'
        elif self.state in ["Off","off"]:
            return super().__str__() #won't display temperature if its off
    def increase_temp(self):
        if self.state in ["On","on"]:
             if self.temp_celcius < 35: #if temperature was below hightest value
                 self.temp_celcius += 1
                 return f'{self.name} has been changed to {self.temp_celcius}C.'
             elif self.temp_celcius == 35:
                 return f'{self.name} is set to 35C [highest]' #even if we keep clicking higher, the highest stays the same, right?
        elif self.state in ["Off","off"]:
            return f'Sorry, {self.name} is off'
    def decrease_temp(self):
        if self.state in ["On","on"]:
            if self.temp_celcius > 10: #if temperature was above lowest value
                 self.temp_celcius -= 1
                 return f'{self.name} has been changed to {self.temp_celcius}C'
            elif self.brightness == 10:
                 return f'{self.name} is set to 10C [lowest]'
        elif self.state in ["Off","off"]:
            return f'Sorry, {self.name} is off'

