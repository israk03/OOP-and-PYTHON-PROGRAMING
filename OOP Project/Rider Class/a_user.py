# create a user abstract class with rider

from abc import ABC, abstractmethod

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