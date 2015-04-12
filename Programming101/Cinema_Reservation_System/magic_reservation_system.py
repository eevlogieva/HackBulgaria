import sqlite3


def main():
    database = sqlite3.connect("cinema.db")
    cursor = database.cursor()
    command = input("Enter a command> ")
    lst = command.split(" ")
    while lst[0] != "exit":
        if lst[0] == "show_movies":
            show_movies(cursor)
        if lst[0] == "show_movie_projections":
            if len(lst) == 3:
                show_projections(cursor, lst[1], lst[2])
            else:
                show_projections(cursor, lst[1], None)
        if lst[0] == "make_reservation":
            make_reservation(database, cursor)
        if lst[0] == "help":
            print("choose one of the following commands:\n" +
                  "show_movies\n show_movie_projections\n" +
                  "make_reservation\n help\n exit\n")
        command = input("Enter a command> ")
        lst = command.split(" ")


def show_movies(cursor):
    print("Current movies:")
    result = cursor.execute("SELECT id, name, rating FROM movies ORDER BY rating")
    for row in result:
        print("[{}] - {} ({})".format(row[0], row[1], row[2]))


def show_projections(cursor, movie_id, date):
    cursor.execute("SELECT name FROM movies where id = ?", movie_id)
    print("Projections for {}".format(cursor.fetchone()[0]))
    if date:
        cursor.execute('''SELECT projections.id, projections.date1, projections.time1, projections.type FROM projections
           where projections.date1 = ? and projections.movie_id = ?''', (date, movie_id))
        result = cursor.fetchall()
        for row in result:
            seats_taken = seats_taken_in_projection(cursor, row[0])
            print ("[{}] - {} {} ({}) - {} seats available".format(row[0], row[1], row[2], row[3], int(100 - seats_taken)))
    else:
        cursor.execute('''SELECT projections.id, projections.date1, projections.time1, projections.type FROM projections
           where projections.movie_id = ?''', movie_id)
        result = cursor.fetchall()
        for row in result:
            seats_taken = seats_taken_in_projection(cursor, row[0])
            print ("[{}] - {} {} ({}) - {} seats available".format(row[0], row[1], row[2], row[3], int(100 - seats_taken)))


def make_reservation(database, cursor):
    name = input("Step 1 (User): Enter name> ")
    number_of_tickets = input("Step 2 (User): Enter numbber of tickets> ")
    show_movies(cursor)
    movie_id = input("Step 2 (Movie): Choose a movie> ")
    show_projections(cursor, movie_id, None)
    projection = input("Step 3 (Projection): Choose a projection> ")
    if 100 - seats_taken_in_projection(cursor, projection) < int(number_of_tickets):
        print("There are not enought tickets for this projection. Choose another one!")
        projection = input("Step 3 (Projection): Choose a projection> ")
    show_available_spots(cursor, projection)
    choose_seats(database, cursor, name, number_of_tickets, projection_id)


def seats_taken_in_projection(cursor, projection_id):
    cursor.execute('''SELECT COUNT (reservations.id) FROM reservations WHERE reservations.projection_id = (?)''', (projection_id, ))
    seats_taken = cursor.fetchone()[0] or 0
    return seats_taken


def show_available_spots(cursor, projection_id):
    cursor.execute('''SELECT row, col FROM reservations WHERE projection_id = ?''', (projection_id, ))
    result = cursor.fetchall()
    print("Available seats (marked with a dot):")
    str_result = "  1 2 3 4 5 6 7 8 9 10\n"
    for row in range(1, 11):
        for col in range(11):
            if col == 0:
                str_result += (str(row) + " ")
            elif (row, col) in result:
                str_result += ("X ")
            else:
                str_result += (". ")
        str_result += '\n'
    print(str_result)


def choose_seats(database, cursor, name, number_of_tickets, projection_id):
    cursor.execute('''SELECT row, col FROM reservations WHERE projection_id = ?''', (projection_id, ))
    result = cursor.fetchall()
    for ticket in range(number_of_tickets):
        string_input = input("Step 4(Seats): Choose seat {}> ".format(ticket + 1))
        row_col = (string_input.replace("(", "").replace(")", "")).split(", ")
        if (row_col[0], row_col[1]) in result:
            print("This seat is already taken, please choose another!")
            string_input = input("Step 4(Seats): Choose seat {}> ".format(ticket + 1))
            row_col = (string_input.replace("(", "").replace(")", "")).split(", ")
        if row_col[0] > 10 or row_col[1] > 10:
            print("Lol...NO!")
            string_input = input("Step 4(Seats): Choose seat {}> ".format(ticket + 1))
            row_col = (string_input.replace("(", "").replace(")", "")).split(", ")
        cursor.execute('''INSERT INTO reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?)''',
                        (name, projection_id, row_col[0], row_col[1]))
        database.commit()



if __name__ == '__main__':
    main()
