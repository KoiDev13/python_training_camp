import sqlite3 

DB_NAME = "employees.db"

con = sqlite3.connect(DB_NAME)
cur = con.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER  PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        years_with_company INTEGER DEFAULT 0
    );
    """
)

cur.executemany("""
                    INSERT INTO employees (first_name, last_name, email, years_with_company) VALUES (?,?,?,?)
                """,
                [
                    ('Khoi1', 'Nguyen', 'khoinguyen1@gmail.com', 1),
                    ('Khoi2', 'Le', 'khoile@gmail.com', 1),
                    ('Khoi3', 'Ly', 'khoily@gmail.com', 1),
                ] 

)
con.commit()

cur.execute("select * from employees")
print(cur.fetchall())


cur.close()
con.close()