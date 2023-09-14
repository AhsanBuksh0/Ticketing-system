# Class variables to keep track of ticket counts and statuses
class Ticket:
    ticket_counter = 2000
    open_tickets = 0
    resolved_tickets = 0

    # Ticket attributes
    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.open_tickets += 1

    # Method to submit a response
    def submit_response(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.resolved_tickets += 1

    #  Reopening a closed ticket
    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.open_tickets += 1
        Ticket.resolved_tickets -= 1

    # To resolve password change request and close the ticket
    def resolve_password_change(self, new_password):
        if "Password Change" in self.description:
            self.response = f"Password changed to: {new_password}"
            self.status = "Closed"
            Ticket.open_tickets -= 1
            Ticket.resolved_tickets += 1

    # Displaying ticket information
    def display_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}\n")

    # Class method to display ticket statistics
    @classmethod
    def ticket_stats(cls):
        return f"Tickets Created: {cls.ticket_counter - 2000}\nTickets Resolved: {cls.resolved_tickets}\nTickets To Solve: {cls.open_tickets}"

# Function where the code/program starts execution 
def main():
    tickets = []

    # Creates three ticket by taking users input 
    for i in range(3):
        print(f"\nEnter Details for Ticket {i + 1}:")

        creator_name = input("Creator Name: ")
        staff_id = input("Staff ID: ")
        contact_email = input("Email Address: ")
        description = input("Description: ")

        tickets.append(Ticket(staff_id, creator_name, contact_email, description))

    print("\nAll Three Tickets :")
    for ticket in tickets:
        ticket.display_ticket_info()

    # Resolving Ticket 1
    response = input("Enter response for Ticket 1: ")
    tickets[0].submit_response(response)

    # Changing password for Ticket 3
    new_password = input("Enter a new password for Ticket 3: ")
    tickets[2].resolve_password_change(new_password)

    print("\nAll Three Tickets:")
    for ticket in tickets:
        ticket.display_ticket_info()

    # Displaying ticket statistics
    print("\nTicket Statistics:")
    print(Ticket.ticket_stats())


if __name__ == "__main__":
    main()
