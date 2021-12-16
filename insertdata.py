
import sqlite3 as lit

employees = (

    (1, 'sankore', 'info@sankore.com'),
    (2, 'gbemileke', 'gbemileke@sankore.com'),
    (3, 'bose', 'bose@sankore.com'),
    (4, 'henry', 'henry@sankore.com'),

)
db = lit.connect('sankore.db')

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?)', employees)

    print("Data Inserted Successfully")