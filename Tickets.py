import random
import string

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
        self.password = None

    # Method to submit a response
    def submit_response(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.resolved_tickets += 1

    # Reopening a closed ticket
    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.open_tickets += 1
        Ticket.resolved_tickets -= 1

    # To resolve password change request and close the ticket
    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.generate_password()
            self.response = f"Password changed to: {new_password}"
            self.status = "Closed"
            Ticket.open_tickets -= 1
            Ticket.resolved_tickets += 1
            self.password = new_password

    # Generate a new password 
    def generate_password(self):
        # Extract the first two characters of staff ID and the first three characters of the ticket creator name
        staff_id_chars = self.staff_id[:2]
        creator_name_chars = self.creator_name[:3]

        # Generate a random 3-character string 
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))

        # create the new password
        new_password = staff_id_chars + creator_name_chars + random_chars

        return new_password

    # Displaying ticket information
    def display_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        if self.password:
            print(f"Password: {self.password}")
        print(f"Ticket Status: {self.status}\n")

    # Class method to display ticket statistics
    @classmethod
    def ticket_stats(cls):
        return f"Tickets Created: {cls.ticket_counter - 2000}\nTickets Resolved: {cls.resolved_tickets}\nTickets To Solve: {cls.open_tickets}"

# Function where the code/program starts execution(main program)
def main():
    tickets = []

    while True:
        # Display menu for user interaction
        print("\nMenu:")
        print("1. Create Ticket")
        print("2. Resolve Ticket")
        print("3. Change Password (if Password Change Request)")
        print("4. View All Tickets")
        print("5. View Open Tickets")
        print("6. View Closed Tickets")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            #Creating new tickets
            creator_name = input("Enter Creator Name: ")
            staff_id = input("Enter Staff ID: ")
            contact_email = input("Enter Email Address: ")
            description = input("Enter Description: ")

            tickets.append(Ticket(staff_id, creator_name, contact_email, description))
            print("Ticket created successfully.")
        elif choice == "2":
            # Resolve a ticket
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. Ticket Number: {ticket.ticket_number} (Status: {ticket.status})")
            ticket_index = int(input("Enter the index of the ticket to resolve: ")) - 1
            if 0 <= ticket_index < len(tickets):
                response = input("Enter response for the selected ticket: ")
                tickets[ticket_index].submit_response(response)
                print("Ticket resolved successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "3":
            # Resolve a password change request and change the password
            for i, ticket in enumerate(tickets, start=1):
                if "Password Change" in ticket.description:
                    print(f"{i}. Ticket Number: {ticket.ticket_number} (Status: {ticket.status})")
            ticket_index = int(input("Enter the index of the Password Change Request to change the password: ")) - 1
            if 0 <= ticket_index < len(tickets):
                tickets[ticket_index].resolve_password_change()
                print("Password changed successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "4":
            # View all tickets and the statistics
            print("\nAll Tickets:")
            for ticket in tickets:
                ticket.display_ticket_info()
            print("\nTicket Statistics:")
            print(Ticket.ticket_stats())
        elif choice == "5":
            # Only view the open tickets with the statistics
            print("\nOpen Tickets:\n")
            for ticket in tickets:
                if ticket.status == "Open":
                    ticket.display_ticket_info()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "6":
            # Only view the closed tickets and the statistics
            print("\nClosed Tickets:\n")
            for ticket in tickets:
                if ticket.status == "Closed":
                    ticket.display_ticket_info()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "0":
            # Exting the program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
