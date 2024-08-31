from abc import ABC, abstractmethod

class abstract_example(ABC):
    @abstractmethod
    def get_price(self):
        pass

class mealoption(abstract_example):
    def __init__(self, meal, price):
        self.meal = meal
        self.price = price

    def get_price(self):
        return self.price


class airport:
    def __init__(self, name):
        self.name = name

class flight:
    def __init__(self, flight_number, airline, departure, arrival, price, seats):
        self.flight_number = flight_number
        self.airline = airline
        self.departure = departure
        self.arrival = arrival
        self.price = price
        self.seats = seats

class customer:
    def __init__(self, name, id_number, contact_info):
        self.name = name
        self.id_number = id_number
        self.contact_info = contact_info

class booking(customer):
    def __init__(self,customer, flight, departure_airport, arrival_airport):
        self.customer = customer
        self.flight = flight
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.meal_option = None

    def add_meal_option(self, meal_option):
        self.meal_option = meal_option


    def calculate_total_price(self):
        total_price = self.flight.price
        if self.meal_option:
            total_price += self.meal_option.get_price()
            return total_price

    def display_booking_details(self):
        print(f"Customer: {self.customer.name}")
        print(f"Flight: {self.flight.flight_number} ({self.flight.airline})")
        print(f"Departure: {self.departure_airport.name} - {self.flight.departure}")
        print(f"Arrival: {self.arrival_airport.name} - {self.flight.arrival}")
        if self.meal_option:
            print(f"Meal Option: {self.meal_option.meal} - ${self.meal_option.get_price()}")
            
        print(f"Total Price: ${self.calculate_total_price()}")



departure_airport = airport("Borg Alarab , Egypt")
arrival_airport = airport("meddina , Saudi Arabia")

flight_object = flight("183", "Egyptian Air Line", "12:00 AM", "5:00 PM", 300.0, 50)

customer_object = customer("Ahmed Saber", "123456789", "ahmed@gmail.com")

booking_object = booking(customer_object, flight_object, departure_airport, arrival_airport)

meal_option = mealoption("Meat", 10.0)
booking_object.add_meal_option(meal_option)


booking_object.display_booking_details()



        