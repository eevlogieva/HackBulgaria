import sqlite3


def main():
    database = sqlite3.connect("company.db")
    cursor = database.cursor()
    print("Hello and welcome to our company. Please, " +
          "enter one of the following commands: " + "\n"
          "list_employees" + "\n"
          "monthly_spending" + "\n"
          "yearly_spending" + "\n"
          "add_employee" + "\n"
          "delete_employee <employee_id>" + "\n"
          "update_employee <employee_id>")

    command = input("enter command> ")
    lst = command.split(" ")
    while lst[0] != "finish":
        if lst[0] == "list_employees":
            result = cursor.execute("SELECT name, position from company")
            for row in result:
                print(row[0] + " - " + row[1])
        if lst[0] == "monthly_spending":
            cursor.execute("SELECT SUM(monthly_salary) FROM company")
            total_money = cursor.fetchone()
            print("The company is spending $%i every month" % (total_money[0]))
        if lst[0] == "yearly_spending":
            cursor.execute("SELECT SUM(monthly_salary) FROM company")
            total_money = cursor.fetchone()[0] * 12
            cursor.execute("SELECT SUM(yearly_bonus) FROM company")
            total_money += cursor.fetchone()[0]
            print("The company is spending $%i for a year" % (total_money))
        if lst[0] == "delete_employee":
            name = cursor.execute("SELECT name from company WHERE id = ?", (lst[1])).fetchone()
            cursor.execute("DELETE FROM company WHERE id = ?", (lst[1]))
            database.commit()
            print("{} was deleted".format(name))
        if lst[0] == "update_employee":
            new_name = input("name>")
            new_salary = input("monthly salary>")
            new_year_bonus = input("yearly bonus>")
            new_position = input("new position>")
            cursor.execute("UPDATE company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?", (new_name, new_salary, new_year_bonus, new_position, lst[1]))
            database.commit()
        if lst[0] == "add_employee":
            new_name = input("name>")
            new_salary = input("monthly salary>")
            new_year_bonus = input("yearly bonus>")
            new_position = input("position>")
            cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?, ?, ?, ?)",
                          (new_name, new_salary, new_year_bonus, new_position))
            database.commit()
        command = input("enter command> ")
        lst = command.split(" ")

if __name__ == '__main__':
    main()
