import math


# Question 1

class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 14

    def move_bookmark(self):
        self.bookmarked_page = self.current_page

    def turn_page(self, forward):
        if forward:
            self.current_page += 1
            if self.current_page > self.num_pages:
                self.current_page = 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.num_pages


# Question 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"{self.width * self.height}m^2"

    def perimeter(self):
        return f"{(self.width*2) + (self.height*2)}m"

    def diagonal(self):
        return f"{math.sqrt(self.width**2 + self.height**2)}m"
    
    def is_rectangle(self):
        if self.width > self.height:
            return "This is a rectangle"
        else:
            return "This is a square"

# Question 3 & 4

class Vehicle:
    def __init__(self, make, model, colour, seats, max_speed, 
    current_speed, dist_travelled_since_refill, fuel_tank_capacity
    ):
        self.make = make
        self.model = model
        self.colour = colour
        self.seats = seats
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.dist_travelled_since_refill = dist_travelled_since_refill
        self.fuel_tank_capacity = fuel_tank_capacity
    
    def __str__(self):
        return f"""Vehicle Summary:
    {self.make} {self.model} - Colour: {self.colour}, Seats: {self.seats}, Max Speed: {self.max_speed}km/hr"""

    def rev_engine(self):
        if self.current_speed == 0:
            return "Silence..."
        if self.current_speed < 80:
            return "Vrrmm"
        return "VRRRMMMMMM!"
    
    def fuel_level(self):
        fuel_consumption = 11.5 #km/L
        fuel_remaining = round(self.fuel_tank_capacity-(self.dist_travelled_since_refill/fuel_consumption))
        tank_level = round(100*(fuel_remaining/self.fuel_tank_capacity))
        if tank_level > 10: #10%
            return f"Fuel tank {tank_level}% full"
        return f"Refuel now! Only {tank_level}% left!"
    
    def refill_tank(self):
        self.dist_travelled_since_refill = 0


car = Vehicle("Fiat", "500c", "Gunmetal Grey", 4, 120, 100, 390, 35)
print(str(car))
print(car.rev_engine())
print(car.fuel_level())
car.refill_tank()
print(car.fuel_level())
