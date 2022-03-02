import datetime     #import datetime package for showing and selecting dates

# Task 1
# ticket prices stored as constants
one_day_adult_price = 20
one_day_child_price = 12
one_day_senior_price = 16
one_day_family_price = 60
one_day_group_price = 15
two_day_adult_price = 30
two_day_child_price = 18
two_day_senior_price = 24
two_day_family_price = 90
two_day_group_price = 22.5
lion_feeding_price = 2.5
penguin_feeding_price = 2
barbecue_price = 5

booking_number = 1000   # booking number initialised for the day

# number of family tickets, group tickets and barbecue tickets initialised as 0
family_tickets = 0
group_tickets = 0
barbecue_tickets = 0

# until the customer wants, tickets would not be considered as family tickets or group tickets
family_ticket_choice = 'n'
group_ticket_choice = 'n'

# Ticket prices to be shown saved as a string
one_day_prices = 'One-day ticket prices:\n Adult\t$20\n Child\t$12\n Senior\t$16\n Family ticket\t$60\n Group ticket\t$15\n'
two_day_prices = "Two-day ticket prices:\n Adult\t$30\n Child\t$18\n Senior\t$24\n Family ticket\t$90\n Group ticket\t$22.5\n"
extra_attractions = "Extra attraction prices:\n Lion feeding\t$2.50\n Penguin feeding\t$2\n Evening barbecue\t$5\n"

# printing the prices and dates
print(one_day_prices)
print(two_day_prices)
print(extra_attractions)
print("Available dates:")

for i in range(1, 8):
    print(datetime.date.today() + datetime.timedelta(days=i))

# Task 2: Processing bookings
while True: # iterating for multiple customers
    while True: # validating the input
        try:
            booking_duration = input("Is it a one-day booking or two-day booking? Enter 1 or 2.")
        except:
            booking_duration = '0'
        if booking_duration == '1' or booking_duration == '2':
            break
        else:
            print("Enter a valid value.")
    print("Enter the first day.")
    print("Available dates:")

    for i in range(1, 8):
        print("Enter", i, "for", datetime.date.today() + datetime.timedelta(days=i),". Decimal numbers will be converted to the closest integer.")

    while True: # validating the date choice
        try:
            first_day = int(input()) # the date to be input as a choice of number from 1 to 7.
        except:
            first_day = 100
        if 1 <= first_day <= 7:
            break
        else:
            print("Enter a value from 1 to 7.")

    while True: #validating the input of the number of tickets
        try:
            adult_tickets = int(input("Enter the number of adult tickets."))
        except: # no need for specific exception
            adult_tickets = -1
        while True:
            try:
                child_tickets = int(input("Enter the number of child tickets."))
            except:
                child_tickets = -1
            if child_tickets > adult_tickets * 2: # validating children tickets separately
                print("One adult cannot take more than 2 children")
            else:
                break
        try:
            senior_tickets = int(input("Enter the number of senior tickets."))
        except:
            senior_tickets = -1
        if all(map(lambda value: value >= 0, (adult_tickets, child_tickets, senior_tickets))):
            adult_n_senior_tickets = adult_tickets + senior_tickets # total of adult and child tickets
            total_tickets = adult_n_senior_tickets + child_tickets # total tickets taken including adults, seniors and children, but excluding family and group tickets
            break
        else:
            print("You can't enter a negative value.")

    while True:
        try:
            lion_feeding_tickets = int(input("Enter the number of tickets requesting lion feeding."))
            penguin_feeding_tickets = int(input("Enter the number of tickets requesting penguin feeding."))
        except:
            lion_feeding_tickets = -1
        if booking_duration == 2:
            try:
                barbecue_tickets = int(input("Enter the number of tickets requesting barbecue."))
            except:
                barbecue_tickets = -1

        # validating attractions
        if all(map(lambda value: 0 <= value <= total_tickets, (lion_feeding_tickets, penguin_feeding_tickets, barbecue_tickets))):
            break
        else:
            print("You cannot enter a negative value or your attraction tickets cannot be more than your total tickets.")

    # Task 3: the tickets, if possible, considered as family tickets
    if adult_n_senior_tickets >= 2 and child_tickets >= 3:
        family_ticket_choice = input("Would you like to buy a family ticket for up to two adults or seniors and 3 children that costs $60 instead as it is the best value pack? Enter y for yes.")

    if family_ticket_choice == 'y':
        while adult_n_senior_tickets >= 2 and child_tickets >= 3:
            family_tickets += 1
            child_tickets -= 3
            if adult_tickets >= 2:
                adult_tickets -= 2

            elif senior_tickets >= 2:
                if adult_tickets == 1:
                    adult_tickets -= 1
                    senior_tickets -= 1
                else:
                    senior_tickets -= 2

    # the left-over adult and senior tickets to be considered as group tickets if more than 6
    if adult_n_senior_tickets >= 6:
        group_ticket_choice = input("Would you like to buy a group ticket for groups of 6 or more that costs $15 for each as it is a better value pack? Enter y for yes.")

    if group_ticket_choice == 'y':
        while adult_n_senior_tickets >= 6:
            group_tickets = adult_n_senior_tickets
            adult_tickets = 0
            senior_tickets = 0

    # calculating and printing the bill after considering the family ticket and group ticket
    if booking_duration == 1:
        print("Booked date: ", datetime.date.today() + datetime.timedelta(days=first_day))
        booking_cost = adult_tickets * one_day_adult_price + child_tickets * one_day_child_price + senior_tickets * one_day_senior_price + family_tickets * one_day_family_price + group_tickets * one_day_group_price + lion_feeding_price * lion_feeding_tickets + penguin_feeding_price * penguin_feeding_tickets
    else:
        print("Booked dates: ", datetime.date.today() + datetime.timedelta(days=first_day), " and ", datetime.date.today() + datetime.timedelta(days=first_day+1))
        booking_cost = adult_tickets * two_day_adult_price + child_tickets * two_day_child_price + senior_tickets * two_day_senior_price + family_tickets * two_day_family_price + group_tickets * two_day_group_price + lion_feeding_price * lion_feeding_tickets + penguin_feeding_price * penguin_feeding_tickets + barbecue_price * barbecue_tickets



    print("You are booking", adult_tickets, "adult tickets,", child_tickets, "child tickets,", senior_tickets, "senior tickets,", family_tickets, "family tickets and", group_tickets, "group tickets for", booking_duration,"days. You are also booking", lion_feeding_tickets, "lion feeding tickets,", penguin_feeding_tickets, "penguin feeding tickets and", barbecue_tickets, "barbecue tickets.")
    print("Total booking cost: $", booking_cost)
    print("Booking number:", booking_number)

    booking_number += 1     # booking number incremented for the next customer

    # Looping if there are more customers
    choice = input("Any more customers? Enter y if yes and n if no.")
    if choice == "n":
        print("No more customers for the day.")
        break
