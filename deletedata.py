import sqlite3 as lit

db = lit.connect('sankore.db')

with db:
    newname = "updatedname"
    user_id = 1

    cur = db.cursor()
    cur.execute('DELETE FROM users WHERE id = ?  ', (user_id,))
    db.commit()
    print("Data Deleted Successfully")