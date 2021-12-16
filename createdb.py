import sqlite3 as lit


def main():
    try:
        db = lit.connect('sankore.db')
        print("Database Created ", db)

    except:
        print("Failed To Create Database")



if __name__ == "__main__":
    main()


