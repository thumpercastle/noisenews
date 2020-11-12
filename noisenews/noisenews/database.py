import sqlite3

conn = sqlite3.connect('articles.db')
curr = conn.cursor()

curr.execute("""create table articles_tb(
                headline text,
                subheading text,
                url text,
                date_detected real)""")

#curr.execute("""insert into articles_tb values ('testing 123', 'testing 456', 'testing 789')""")


conn.commit()
conn.close()