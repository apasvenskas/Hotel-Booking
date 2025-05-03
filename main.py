import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def availble(self):
        pass

class ReservTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
       pass

print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.availble():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is unavailable.")