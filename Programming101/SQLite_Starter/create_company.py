import sqlite3


def main():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS company
        (id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')
    conn.commit()

    id1 = 1
    name1 = "Ivan Ivanov"
    monthly_salary1 = 5000
    yearly_bonus1 = 10000
    position1 = "Software Developer"

    cursor.execute(''' INSERT into company(id, name, monthly_salary, yearly_bonus, position)
                   VALUES(?, ?, ?, ?, ?)''', (id1, name1, monthly_salary1, yearly_bonus1, position1))
    conn.commit()

    id2 = 2
    name2 = "Rado Rado"
    monthly_salary2 = 500
    yearly_bonus2 = 0
    position2 = "Technical Support Intern"

    cursor.execute(''' INSERT into company(id, name, monthly_salary, yearly_bonus, position)
                   VALUES(?, ?, ?, ?, ?)''', (id2, name2, monthly_salary2, yearly_bonus2, position2))
    conn.commit()

    id3 = 3
    name3 = "Ivo Ivo"
    monthly_salary3 = 10000
    yearly_bonus3 = 100000
    position3 = "CEO"

    cursor.execute(''' INSERT into company(id, name, monthly_salary, yearly_bonus, position)
                   VALUES(?, ?, ?, ?, ?)''', (id3, name3, monthly_salary3, yearly_bonus3, position3))
    conn.commit()

    id4 = 4
    name4 = "Petar Petrov"
    monthly_salary4 = 3000
    yearly_bonus4 = 1000
    position4 = "Marketing Manager"

    cursor.execute(''' INSERT into company(id, name, monthly_salary, yearly_bonus, position)
                   VALUES(?, ?, ?, ?, ?)''', (id4, name4, monthly_salary4, yearly_bonus4, position4))
    conn.commit()

    id5 = 5
    name5 = "Maria Georgieva"
    monthly_salary5 = 8000
    yearly_bonus5 = 10000
    position5 = "COO"

    cursor.execute(''' INSERT into company(id, name, monthly_salary, yearly_bonus, position)
                   VALUES(?, ?, ?, ?, ?)''', (id5, name5, monthly_salary5, yearly_bonus5, position5))
    conn.commit()


if __name__ == '__main__':
    main()
