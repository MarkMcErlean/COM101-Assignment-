# COM101 Assignment 1 coding project
import matplotlib.pyplot as plt

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


# option 1 - Output a list of record titles and their respective details, including a summary report displaying
# (a) the total number of titles in stock and (b) the value of records in stock.
def read_data():
    if not file_contents_record_data:  # if read_data() has not been called yet, do so here (prevents duplication)
        infile = open('RECORD_DATA.txt', 'r')  # open text file

        # parse through the file and add to list
        for row in infile:
            start = 0  # indicates position in each line
            string_builder = []
            if not row.startswith('#'):  # ignore rows starting with comments
                for index in range(len(row)):
                    if row[index] == ',' or index == len(row) - 1:
                        string_builder.append(row[start:index])
                        start = index + 1
                file_contents_record_data.append(string_builder)
        infile.close()  # close text file


# defining a function to print the summary so that the first function can be reused easily
def print_summary():
    value = 0  # set initial value to zero
    in_stock = 0  # set initial value to zero
    for each_row in file_contents_record_data:  # for each row
        print(*each_row, sep=',')
        value += float(each_row[6])  # add value at index 6 to value variable
        in_stock += int(each_row[5])  # add value at index 5 to stock variable

    print('The total value of records is ', format(value, '.2f'), sep='£')
    print('There are', in_stock, 'items in stock.')
    clear_screen()  # print the totals then clear the screen


# function to clear the screen and aid readability
def clear_screen():
    print('\n')
    input('Press enter to return to the menu...')
    clear = '\n' * 2  # creates new lines to aid readability
    print(clear)


# option 2 - Output a list of record titles and their respective details
# which are above a user provided price threshold.
def details_above_price_point():
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


genres = []
genre_tally = {}


# option 3 - Output a report giving the number of records existing in each genre type.
def genre_tally_function():
    # create a dictionary for genres
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


def show_genre_tally():
    for key, value in genre_tally.items():
        print(key, value, sep=':')

    clear_screen()


# option 4 - Option to add a new record and present a summary report displaying
# (a) the new total number of titles in stock and (b) the new total value of records in stock.
def add_records_show_summary():
    new_listing = []
    new_listing_qty = int(input('How many listings would you like to add: '))
    if new_listing_qty <= 0:
        print('Invalid input, try again. ')
        add_records_show_summary()

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

        file_contents_record_data.append(new_listing)  # appending the new record to the list from read_data()
        print_summary()


# option 5 - Query if a record title is available and present option of
# (a) increasing stock level or (b) decreasing the stock level, due to a sale.
def check_available_increase_decrease():
    # if read_data has not already been called, do so here
    if not file_contents_record_data:
        read_data()
    query_record_titles = ' ' + input("Enter a record title: ")  # user input of title name
    titles = []  # blank list to store title names
    stock = []  # blank list to store stock levels
    titles_in_stock = {}  # blank dictionary to pair title names with stock levels
    count = 0  # counter

    if not titles:
        for each_row in file_contents_record_data:  # if titles list is empty, run this
            titles.append(each_row[1].lower())  # parsing through each row and adding record titles to list
            stock.append(each_row[5])  # adding stock levels to a list
    if not titles_in_stock:  # if dictionary is empty, run this
        for names in titles:
            titles_in_stock[names] = stock[count]
            count += 1
    # if this code were to run multiple times, it would wipe the results of the previous time.

    if query_record_titles.lower() in titles:  # if user search is found in title list
        print('Record found! there are', titles_in_stock.get(query_record_titles, 'Record not found'), 'in stock')
        # print that the record was found, then show the stock level.

        # ask the user to increase or decrease stock or return to menu
        print("1: Increase stock levels")
        print("2: Decrease stock levels")
        print("3: Return to main menu")

        choice = int(input("Select an option: "))
        if choice == 1:
            temp_stock = int(input("How many vinyls are to be added to stock: "))  # user input stored
            if temp_stock < 0:  # if user input is less than zero, call error message
                print('Must be a positive number only')
                check_available_increase_decrease()  # run function again
            current_stock = int(titles_in_stock.get(query_record_titles))  # create variable with dictionary value
            new_stock = current_stock + temp_stock  # add the two values together

            for temporary in file_contents_record_data:  # loop through list
                if query_record_titles.lower() in temporary[1].lower():  # if the title is found in the loop
                    if temporary[5] + new_stock >= temporary[5]:  # and if the value is more than or equal to temporary
                        temporary[5] = new_stock  # change the stock level in the main list
                    else:
                        print('You cannot add negative stock...')

        elif choice == 2:
            temp_stock = int(input('How many vinyls were sold: '))  # user input stored
            if temp_stock < 0:  # id user input is less than zero
                print('Must be a positive number only')  # display error message and re-run function
                check_available_increase_decrease()
            current_stock = int(titles_in_stock.get(query_record_titles))  # set current_stock to dictionary value
            new_stock = current_stock - temp_stock  # subtract user input from current stock

            for temporary in file_contents_record_data:  # loop through main list
                if query_record_titles.lower() in temporary[1].lower():  # if title is in the main list
                    if temporary[5] - new_stock >= 0:  # amd the new value is zero or more
                        temporary[5] = new_stock  # change the stock value in the main list
                    else:
                        print('number entered is more than stock available')  # otherwise, show an error
                        clear_screen()

        elif choice == 3:  # return to menu
            clear_screen()
            options()

    else:  # if title not found, return to menu so that it can be added
        print('Item not found, please return to the menu to add this item...')
        clear_screen()


# option 6 - Plot a labelled bar chart that presents the number of titles existing in each genre type.
def plot_bar_chart():
    labels = []
    bar_values = []

    # if read_data has not already been called, do so here
    if not file_contents_record_data:
        read_data()
    genre_tally_function()

    for label, value in genre_tally.items():  # loop through tally dictionary and add to the labels and values
        labels.append(label)
        bar_values.append(value)

    plt.bar(labels, bar_values)  # plot the x and y values
    plt.title('Stock levels per genre')
    plt.xlabel('Genres')
    plt.ylabel('Stock Levels')
    plt.show()  # show the graph


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
            details_above_price_point()
        elif option == 3:
            print('You selected option 3: Report of record quantities in each genre.')
            print('****************************************************** \n')
            genre_tally_function()
            show_genre_tally()
        elif option == 4:
            print('You selected option 4: Add a new record and display summary report.')
            print('****************************************************** \n')
            add_records_show_summary()
        elif option == 5:
            print('You selected option 5: Check record availability.')
            print('****************************************************** \n')
            check_available_increase_decrease()
        elif option == 6:
            print('You selected option 6: Display visual chart of vinyls on record.')
            print('****************************************************** \n')
            plot_bar_chart()
        elif option == 7:
            option_seven()
    except ValueError:
        print("Oops! that isn't a valid choice!")
        clear_screen()


# defining the main function that will run each step in the process
def main():
    user_interface()
    options()


while keep_going == 'y':  # makes sure program will only exit when exit is called by user
    main()
