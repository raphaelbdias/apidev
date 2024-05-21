import sqlite3
con = sqlite3.connect("login.db")
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()

# data = [
#     (1,"admin", "2210",),
#     (2,"user@testmail.com", "12345678")
# ]
# cur.executemany("INSERT INTO login VALUES(?, ?, ?)", data)
# con.commit()  # Remember to commit the transaction after executing INSERT.


for row in cur.execute("SELECT * FROM login"):
    print(row)

con.close()