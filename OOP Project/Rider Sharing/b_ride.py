# a -> Ride class to create a ride

from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, name, mail, id, nid):
        self.name = name
        self.mail = mail
        self.__id = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, mail, id, nid, current_location, current_ride):
        self.current_location = current_location
        self.current_ride = current_ride
        self.wallet = 0
        super().__init__(name, mail, id, nid)

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def display_profile(self):
        print(f"Rider name: {self.name} with email {self.mail}.")

    def request_ride(self, location, destination):
        if not self.current_ride:
            # TODO : set ride properly
            # TODO : set current ride via ride match
            ride_request = None
            self.current_ride = None

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