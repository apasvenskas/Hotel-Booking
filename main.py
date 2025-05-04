import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze() # add squeeze for correct string format
        if availability == "yes":
            return True
        else:
            return False
    

class ReservTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
       pass


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is unavailable.")