# figuring out how to assign numbers to individual tickets in a list

class Ticket:
    ticket_numbers = []

    def __init__(self, summary, description, status='Open'):
        self.summary = summary
        self.description = description
        self.status = status
        self.ticket_number = self.generate_ticket_number()

    def generate_ticket_number(self):
        ticket_number = len(Ticket.ticket_numbers) + 1
        Ticket.ticket_numbers.append(ticket_number)
        return ticket_number

