# COM101 Assignment 1 coding project

# Creating a basic UI

# defining a variable so that the program will exit when requested
keep_going = 'y'
file_contents_record_data = []


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
def read_data():
    if not file_contents_record_data:
        infile = open('RECORD_DATA.txt', 'r')

        # parse through the file and add to list
        for row in infile:
            start = 0  # indicates position in each line
            string_builder = []
            if not row.startswith('#'):
                for index in range(len(row)):
                    if row[index] == ',' or index == len(row) - 1:
                        string_builder.append(row[start:index])
                        start = index + 1
                file_contents_record_data.append(string_builder)
        infile.close()

    # input('Press enter to return to the menu...')
    # clear = '\n' * 10  # this is intended to make the screen more readable for the user
    # print(clear)


def print_summary():
    value = 0
    in_stock = 0
    for each_row in file_contents_record_data:
        print(*each_row, sep=',')
        value += float(each_row[6])
        in_stock += int(each_row[5])

    print('The total value of records is ', format(value, '.2f'), sep='£')
    print('There are', in_stock, 'items in stock.')
    clear_screen()


def clear_screen():
    input('Press enter to return to the menu...')
    clear = '\n' * 10  # this is intended to make the screen more readable for the user
    print(clear)


# option 2 - Output a list of record titles and their respective details
# which are above a user provided price threshold.
def option_two():
    price_threshold = float(input("Enter the price threshold: "))
    above_threshold = []
    # if read_data has not already been called, do so here
    if not file_contents_record_data:
        read_data()
    for each_row in file_contents_record_data:
        if float(each_row[6]) > price_threshold:
            above_threshold.append(each_row)

    for listing in above_threshold:
        print(*listing, sep=',')
    clear_screen()


# option 3 - Output a report giving the number of records existing in each genre type.
def display_genre_tally():
    # create a dictionary for genres
    genres = []
    genre_tally = {}
    # if read_data has not already been called, do so here
    if not file_contents_record_data:
        read_data()

    # adding each genre to a list
    for each_row in file_contents_record_data:
        genres.append(each_row[2])
    # list off number of records in each genre

    for each_genre in genres:
        if each_genre in genre_tally:
            genre_tally[each_genre] = int(genre_tally[each_genre]) + 1
        else:
            genre_tally[each_genre] = 1

    for key, value in genre_tally.items():
        print(key, value, sep=':')

    clear_screen()


# option 4 - Option to add a new record and present a summary report displaying
# (a) the new total number of titles in stock and (b) the new total value of records in stock.
def option_four():
    print('You selected option 4: Add a new record and display summary report.')
    new_listing = []
    new_listing_qty = int(input('How many listings would you like to add: '))
    if not new_listing:
        artist, title, genre, length, condition, stock, cost = 0, 0, 0, 0, 0, 0, 0
        # if read_data has not already been called, do so here
        if not file_contents_record_data:
            read_data()

        for add_listing in range(new_listing_qty):
            artist = input("Artist name: ")
            title = input("Title: ")
            genre = input("Genre: ")
            length = input("Play Length: ")
            condition = input("Condition: ")
            stock = input("Stock: ")
            cost = input("Cost: ")
        new_listing += (artist, ' ' + title, ' ' + genre, ' ' + length, ' ' + condition, ' ' + stock, ' ' + cost)

        file_contents_record_data.append(new_listing)
        print_summary()


# option 5 - Query if a record title is available and present option of
# (a) increasing stock level or (b) decreasing the stock level, due to a sale.
def option_five():
    print('You selected option 5: Check record availability.')
    if not file_contents_record_data:
        read_data()




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
            print('You selected option 1: List record titles and details. \n')
            print('****************************************************** \n')
            read_data()
            print_summary()
        elif option == 2:
            print('You selected option 2: List record titles and details above a certain price.')
            print('****************************************************** \n')
            option_two()
        elif option == 3:
            print('You selected option 3: Report of record quantities in each genre.')
            print('****************************************************** \n')
            display_genre_tally()
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
