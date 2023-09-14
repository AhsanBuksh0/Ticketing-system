# Ticketing-system
**HELP DESK TICKETING SYSTEM USER MANUAL**

**Purpose:**
A prototype designed to manage tickets from internal consumers within an organisation is called the Help Desk Ticketing System. Staff employees may use this system to submit support tickets to the Help Desk, follow the progress of such requests, and get statistical data on the cases.
Scope:The Help Desk Ticketing System user manual explains how to use it, including how to create tickets, resolve them, change passwords for password change requests, view tickets, and access ticket statistics.

**Getting Started**
**Installtion**
There is no installation required for this system. You only need a Python environment to run the provided code.

**Running the Program**
Open a terminal or command prompt.
Navigate to the directory containing the Python script (.py file) using the cd command.
Run the program by entering the following command and pressing Enter:python help_desk_ticketing.py

**USING THE SYSTEM**
**MAIN MENU**
Upon running the program, you will see a main menu with the following options:
1.**Create Ticket** Create a new support ticket.
2. **Resolve Ticket** Resolve an open ticket by providing a response.
3. **Change Password (if Password Change Request):** Change the password for a password change request ticket.
4. **View All Tickets:** Display information about all tickets, including resolved and open tickets.
5. **View Open Tickets:** Display information about open (unresolved) tickets.
6. **View Closed Tickets:** Display information about closed (resolved) tickets.
0. **Exit:** Exit the program.

**Creating a Ticket**
1. Select option 1 from the main menu.
2. Enter the requested information:
    - Creator Name
    - Staff ID
    - Contact Email
    - Description of the issue
    - **NOTE** During creating the ticket for Password Change request remember that the 'P'and 'C' will be in Caps Lock eg."Password Change"
3. The ticket will be created, and you will receive a confirmation message.

**Resolving a Ticket**
To resolve an open ticket, follow these steps:
1. Select option 2 from the main menu.
2. Choose the ticket you want to resolve by entering its index.
3. Provide a response for the selected ticket.
4. The ticket will be marked as resolved, and you will receive a confirmation message.

**Changing Password for Password Change Request**
**NOTE** During creating the ticket for Password Change request remember that the 'P'and 'C' will be in Caps Lock eg."Password Change" in the Description.
To change the password for a "Password Change" request:
1. Choose option (3) from the menu.
2. Select the "Password Change" request you want to process by entering its index.
3. The system will automatically generate a new password based on the specified rules.
4. The ticket will be marked as "Closed," and the new password will be displayed.

**Viewing Ticket**
You can view ticket details and statistics using the following options:
- **View All Tickets (4):** Displays all ticket details and statistics.
- **View Open Tickets (5):** Displays open ticket details and statistics.
- **View Closed Tickets (6):** Displays closed ticket details and statistics.

**Exiting the system**
To exit the program, select option 0 from the main menu. You will receive a confirmation message, and the program will exit.

**CONCLUSION**
The Help Desk Ticketing System provides a convenient way to manage support tickets for your organization's internal customers. Follow the provided instructions to create, resolve, and view tickets.
