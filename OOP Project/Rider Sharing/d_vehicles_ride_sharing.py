# a -> Ride class to create a ride

from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing():
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)


class User(ABC):
    def __init__(self, name, mail, id, nid):
        self.name = name
        self.mail = mail
        self.__id = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, mail, id, nid, current_location, current_ride, initial_amount):
        self.current_location = current_location
        self.current_ride = current_ride
        self.wallet = initial_amount
        super().__init__(name, mail, id, nid)

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def display_profile(self):
        print(f"Rider name: {self.name} with email {self.mail}.")

    def request_ride(self, destination):
        if not self.current_ride:
            # TODO : set ride properly
            # TODO : set current ride via ride match
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching()

            self.current_ride = ride_matcher.find_driver(ride_request)


# b -> Ride class to create a ride
class Driver(User):
    def __init__(self, name, mail, nid, current_location):
        super().__init__(name, mail, id, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver name {self.name} with email {self.mail}")

    def accept_ride(self, ride):
        ride.set_driver(self)

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare


# c -> Ride matching and request
class Ride_Request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class Ride_Matching:
    def __init__(self):
        self.available_drivers = []

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0: 
            # TODO : Find the closest driver of the rider 
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride()
            return ride
        

# d -> create vehicles and ride sharing (top) class
class Vehicle(ABC):

    def __init__(self, type, license, rate):
        self.type = type
        self.license = license
        self.rate = rate
        self.status = 'available'
    
    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, type, license, rate):
        super().__init__(type, license, rate)

    def start_drive(self):
        self.status = 'unavailable'