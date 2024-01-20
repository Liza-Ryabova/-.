class Ticket:
    def __init__(self, customer, issue, priority):
        self.customer = customer
        self.issue = issue
        self.priority = priority
        self.status = "New"

support_system.py:
from ticket import Ticket

class SupportSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer, issue, priority):
        ticket = Ticket(customer, issue, priority)
        self.tickets.append(ticket)
        self.notify_support_personnel(ticket)

    def notify_support_personnel(self, ticket):
        print(f"Notification: New ticket created - {ticket.issue}")

main.py:
from support_system import SupportSystem

def main():
    support = SupportSystem()
    support.create_ticket("Client1", "Can't run report", "High")
    support.create_ticket("Client2", "Error message on login", "Low")

    for ticket in support.tickets:
        print(f"Ticket from {ticket.customer}: {ticket.issue}, Priority: {ticket.priority}, Status: {ticket.status}")

if __name__ == "__main__":
    main()  
