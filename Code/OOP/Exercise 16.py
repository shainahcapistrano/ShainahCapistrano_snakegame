class AirTicket:
    def __init__(self, passenger_name, departing_airport, destination_airport, ticket_class, price):
        self.passenger_name = passenger_name
        self.departing_airport = departing_airport
        self.destination_airport = destination_airport
        self.ticket_class = ticket_class
        self.price = price

    def __str__(self):
        out = self.passenger_name + "your ticket will cost" + str(self.price)
        out = out + "leaving from" + self.departing_airport + "flying to" + self.destination_airport
        return out


def tester():
    luke_ticket = AirTicket("Luke", "DSM", "LAX", "first", 1445)
    print(luke_ticket)


if __name__ == "__main__":
    tester()
