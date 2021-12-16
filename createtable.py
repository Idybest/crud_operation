import sqlite3 as lit


def main() :
    try:
        db = lit.connect ('sankore.db')
        cur = db.cursor()

        tablequery = "CREATE TABLE users (id INT, name TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created")

    except lit.Error as e:
        print("Unable To Create Table")



if __name__ == "__main__":
    main()