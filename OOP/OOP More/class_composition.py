class Room:
    def __init__(self, name, area):
        self.name = name
        self.area = area

class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def total_area(self):
        return sum(room.area for room in self.rooms)
    
    def print_rooms(self):
        print("Rooms in the house:")
        for room in self.rooms:
            print(f"{room.name}: {room.area} sq. ft.")

kitchen = Room("Kitchen", 150)
bed_room = Room("Bed Room", 250)
my_house = House()

my_house.add_room(kitchen)
my_house.add_room(bed_room)

print(f"Total area of the house", my_house.total_area(), "sq. ft.}.")
my_house.print_rooms()