# COM101 Assignment 1 coding project

# Creating a basic UI

# defining a variable so that the program will exit when requested
keep_going = 'y'


def user_interface():
    print('Press a number from 1-7 to use a feature')
    print('1. List record titles and details')
    print('2. List record titles and details above a certain price')
    print('3. Report of record quantities in each genre')
    print('4. Add a new Record and display summary report')
    print('5. Check record availability')
    print('6. Display a visual chart of vinyls on record')
    print('7. Quit')


# creating each user option
# option 1 - Output a list of record titles and their respective details, including a summary report displaying
# (a) the total number of titles in stock and (b) the value of records in stock.
def option_one():
    print('You selected option 1: List record titles and details.')
    print('******************************************************')
    data = open('RECORD_DATA.txt')
    print(data.readlines())

# option 2 - Output a list of record titles and their respective details
# which are above a user provided price threshold.
def option_two():
    print('You selected option 2: List record titles and details above a certain price.')


# option 3 - Output a report giving the number of records existing in each genre type.
def option_three():
    print('You selected option 3: Report of record quantities in each genre.')


# option 4 - Option to add a new record and present a summary report displaying
# (a) the new total number of titles in stock and (b) the new total value of records in stock.
def option_four():
    print('You selected option 4: Add a new record and display summary report.')


# option 5 - Query if a record title is available and present option of
# (a) increasing stock level or (b) decreasing the stock level, due to a sale.
def option_five():
    print('You selected option 5: Check record availability.')


# option 6 - Plot a labelled bar chart that presents the number of titles existing in each genre type.
def option_six():
    print('You selected option 6: display visual chart of vinyls on record.')


# option 7 - quit the program
def option_seven():
    global keep_going
    keep_going = 'n'
    print('You selected option 7. Quitting the program...')


def options():
    try:
        option = int(input())
        if option == 1:
            option_one()
        elif option == 2:
            option_two()
        elif option == 3:
            option_three()
        elif option == 4:
            option_four()
        elif option == 5:
            option_five()
        elif option == 6:
            option_six()
        elif option == 7:
            option_seven()
    except ValueError:
        print("Oops! that isn't a valid choice!")

# defining the main function that will run each step in the process
def main():
    user_interface()
    options()


while keep_going == 'y':
    main()
