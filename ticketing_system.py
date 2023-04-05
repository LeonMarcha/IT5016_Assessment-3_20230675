# ticketing_system.py

# first iteration includes class Ticket
# implemented encapsulation
# second iteration includes user console


class Ticket:
    stored_tickets = []
    ticket_number = 2000  # counter static field begins at 2000
    tickets_created = 0
    tickets_closed = 0
    tickets_open = 0

    def __init__(self, s_id, name, se, sd, re, oc):
        self.s_id = s_id  # Staff ID
        self.name = name  # Staff Name
        self.se = se  # Staff Email
        self.sd = sd  # Description of issue
        self.re = re  # Response
        self.oc = oc  # Status (Open/Closed)
        Ticket.stored_tickets.append(self)
        Ticket.ticket_number += 1
        Ticket.tickets_created += 1
        Ticket.tickets_open += 1
        self.change_pass()

    def get_id(self):
        return self.s_id

    def set_id(self, s_id):
        self.s_id = s_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.se

    def set_email(self, se):
        self.se = se

    def get_disc(self):
        return self.sd

    def set_disc(self, sd):
        self.sd = sd

    def get_response(self):
        return self.re

    def set_response(self, re):
        self.re = re

    def get_status(self):
        return self.oc

    def set_status(self, oc):
        self.oc = oc

    def get_ticket(self, ticket_number):
        for ticket in Ticket.stored_tickets:
            if ticket.ticket_number == ticket_number:
                return f"\n\nTicket Number:{str(Ticket.ticket_number)}\n" \
                       f"Ticket Creator:{self.get_name()}\n" \
                       f"Staff ID:{self.get_id()}\n" \
                       f"Email Address:{self.get_email()}\n" \
                       f"Description:{self.get_disc()}\n" \
                       f"Response:{self.get_response()}\n" \
                       f"Ticket Status:{self.get_status()}\n"
        return "Ticket Not found"

    def get_stats():
        ticket_stats = f"\n\nTickets Created:{Ticket.tickets_created}\n"
        ticket_stats += f"Tickets Resolved:{Ticket.tickets_closed}\n"
        ticket_stats += f"Tickets To Solve:{Ticket.tickets_open}\n"
        return ticket_stats

    def change_pass(self):
        if "password change" in self.sd.lower() or "change password" in self.sd.lower():
            new_pass = self.s_id[:2] + self.name[:3]
            self.set_response("New Password generated:" + new_pass)


t1 = Ticket("Staff ID", "Name", "Email address", "Description", "Not yet provided", "Open")


# if user asks to submit ticket, show input console
# store data given in console
# user asks to see submitted ticket, show ticket
class Main:

    def __init__(self):
        action = 0

        while action != 4:
            print("\n"
                  "1. Submit a ticket\n"
                  "2. View ticket\n"
                  "3. Show ticket stats\n"
                  "4. Exit program\n")
            action = int(input("Enter number (1-4):"))

            if action == 1:  # Submit a ticket
                print("Please enter the following -")
                s_id = input("Staff ID:")
                name = input("Name:")
                se = input("Email:")
                sd = input("Description:")
                t = Ticket(s_id, name, se, sd, "Not yet provided", "Open")
                print("Ticket number:", t1.ticket_number)

            elif action == 2:  # View ticket
                while True:
                    ticket_number = int(input("Enter ticket number:"))

                    print("Printing Tickets:", (t1.get_ticket(ticket_number)))

                    sub_action = input("Would you like to respond to, or reopen a ticket? Y/N:")

                    if sub_action.upper() == "Y":
                        print("Ticket reopened.")

                    elif sub_action.upper() == "N":
                        print("Ticket status unchanged")
                        break

                    else:
                        print("Please select again.")

            elif action == 3:  # Show ticket status
                print("Displaying Ticket Stats:",
                      (Ticket.get_stats()))

            elif action == 4:  # Exit
                print("\n"
                      "Goodbye")
                break

            else:
                print("Please select a number between 1 and 4.")


Main()

# to retrieve ticket, stored_tickets[list index].desired function
