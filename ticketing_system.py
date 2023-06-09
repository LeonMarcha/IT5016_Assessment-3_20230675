# ticketing_system.py

# first iteration includes class Ticket
# second iteration includes user console


class Ticket:
    stored_tickets = []  # stores all tickets
    ticket_numbers = []  # stores all ticket numbers
    ticket_number = 2000  # counter static field begins at 2000
    tickets_created = 0
    tickets_closed = 0
    tickets_open = 0

    def __init__(self, s_id, name, email, disc, response, status):
        self.s_id = s_id  # Staff ID
        self.name = name  # Staff Name
        self.email = email  # Staff Email
        self.disc = disc  # Description of issue
        self.response = response  # Response
        self.status = status  # Status (Open/Closed)
        self.ticket_number = self.generate_ticket_number()
        Ticket.stored_tickets.append(self)  # Stores each new ticket in array
        Ticket.ticket_number += 1
        Ticket.tickets_created += 1
        Ticket.tickets_open += 1
        self.change_pass()

    def generate_ticket_number(self):
        ticket_number = len(Ticket.ticket_numbers) + 2001
        Ticket.ticket_numbers.append(ticket_number)
        return ticket_number

    def get_id(self):
        return self.s_id

    def set_id(self, s_id):
        self.s_id = s_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_disc(self):
        return self.disc

    def set_disc(self, disc):
        self.disc = disc

    def get_response(self):
        return self.response

    def set_response(self, response):
        self.response = response

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_ticket(self, ticket_number):
        for ticket in Ticket.stored_tickets:
            if ticket.ticket_number == ticket_number:
                return f"\n\nTicket Number: {ticket_number}\n" \
                       f"Ticket Creator: {self.get_name().capitalize()}\n" \
                       f"Staff ID: {self.get_id()}\n" \
                       f"Email Address: {self.get_email()}\n" \
                       f"Description: {self.get_disc()}\n" \
                       f"Response: {self.get_response()}\n" \
                       f"Ticket Status: {self.get_status()}\n"
        return "No tickets matching input."

    def get_stats():
        ticket_stats = f"\n\nTickets Created:{Ticket.tickets_created}\n"
        ticket_stats += f"Tickets Resolved:{Ticket.tickets_closed}\n"
        ticket_stats += f"Tickets To Solve:{Ticket.tickets_open}"
        return ticket_stats

    def change_pass(self):
        if "password change" in self.disc.lower() or "change password" in self.disc.lower():
            new_pass = self.s_id[:2] + self.name[:3]
            self.set_response("New Password generated:" + new_pass)


# if user asks to submit ticket, show input console
# store data given in console
# user asks to see submitted ticket, show ticket
class Main:

    def __init__(self):
        action = 0
        menu = "\n"\
               "1. Submit a ticket\n"\
               "2. View tickets\n"\
               "3. Show ticket stats\n"\
               "4. Exit program"

        while action != 4:
            try:
                print(menu)
                action = int(input("\nEnter number (1-4): "))
                if action == 1:  # Submit a ticket
                    print("\nCreating a ticket,\nPlease enter the following -")
                    s_id = input("Staff ID: ")
                    name = input("Name: ")
                    while True:
                        email = input("Email: ")
                        if '@' and "." in email:
                            break
                        else:
                            print("Please enter a valid email address.")
                    disc = input("Description: ")
                    Ticket(s_id, name, email, disc, "Not yet provided", "Open")
                    print("Ticket created,\n"
                          "Assigned ticket number: ", Ticket.ticket_number)

                elif action == 2:  # View tickets
                    if len(Ticket.stored_tickets) == 0:
                        print("No tickets.")
                    else:
                        print("All stored tickets:\n")
                        for ticket in Ticket.stored_tickets:
                            print(f"Ticket number: {ticket.ticket_number}, "
                                  f"Creator: {ticket.get_name().capitalize()}, "
                                  f"Status: {ticket.get_status()}")

                        ticket_number = int(input("\nEnter ticket number or '0' to go back:"))
                        if ticket_number == 0:
                            continue
                        else:
                            print("\nPrinting Ticket:", ticket.get_ticket(ticket_number))
                        open_option = 0
                        while open_option != 3:
                            try:
                                open_option = int(input("1. Respond to ticket\n"
                                                        "2. Reopen ticket\n"
                                                        "3. Back\n\n"
                                                        "Enter number (1-3):"))

                                if open_option == 1:
                                    ticket.set_response(input("Enter your response: "))
                                    ticket.set_status("Closed")
                                    Ticket.tickets_closed += 1
                                    Ticket.tickets_open -= 1

                                elif open_option == 2:
                                    if ticket.get_status() == "Closed":
                                        print("Ticket reopened.")
                                        ticket.set_status("Open")
                                        Ticket.tickets_closed -= 1
                                        Ticket.tickets_open += 1
                                    else:
                                        print("\nTicket is already open.\n")

                                elif open_option == 3:
                                    break

                                else:
                                    print("Select a number between 1 and 3")
                                continue
                            except ValueError:
                                print("Invalid input.")

                elif action == 3:  # Show ticket status
                    print("Displaying Ticket Stats:",
                          (Ticket.get_stats()))

                elif action == 4:  # Exit
                    print("\n"
                          "Goodbye")
                    break

                else:
                    print("Select a number between 1 and 4.")
                continue
            except ValueError:
                print("Invalid input.")


if __name__ == "__main__":
    Main()

# to retrieve ticket, stored_tickets[list index].desired function
