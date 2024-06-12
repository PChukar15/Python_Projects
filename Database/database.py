import sqlite3

conn = sqlite3.connect('project.db')

# initial setup of db and table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_project ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_files TEXT \
                )")
    conn.commit()

conn = sqlite3.connect('project.db')

# tuple of names
project_tuple = ('information.docx', 'Hello.txt', 'myImage.png',
                 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loops through each name to find those that are '.txt'
for x in project_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_project (col_files) VALUES (?)", (x,))
            print(x)

conn.close()