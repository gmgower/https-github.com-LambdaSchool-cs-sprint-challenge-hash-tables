#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

#Understand
    # Testcase given

#Plan
    # Setup tickets hash table
    # Iterate through the tickets
        # Set the source as the key & destination as the value
    
    # Set up route list
    # Initialize with the first location

    # Find the next destination based on the previous location
        # and append to the route

# Execute
    hash_tickets = {}

    for ticket in tickets:
        hash_tickets[ticket.source] = ticket.destination

    route = [hash_tickets["NONE"]] #[0:"LAX"]

    for i in range(1, length):     
        route.append(hash_tickets[route[i - 1]]) # [0:"LAX", 1: "SFO", 2: "BHM", etc...] # find key: LAX(destination) in dict to get value "SFO"

    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(type(tickets))

print(reconstruct_trip(tickets, 10))

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#             "SLC", "PIT", "ORD", "NONE"]
