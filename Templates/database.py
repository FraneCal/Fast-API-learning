import sqlite3

DB_NAME = "my_database.db"

def create_connection(db_name=DB_NAME):
    """Create a database connection."""
    return sqlite3.connect(db_name)

def create_table(connection):
    """Create the Students table if it doesn't already exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()

def insert_student(connection, name, age, email):
    """Insert a new student record into the Students table."""
    insert_query = """
    INSERT INTO Students (name, age, email)
    VALUES (?, ?, ?);
    """
    cursor = connection.cursor()
    cursor.execute(insert_query, (name, age, email))
    connection.commit()

def fetch_students(connection):
    """Fetch all students from the Students table."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Students;")
    return cursor.fetchall()

def main():
    # Open a database connection
    with create_connection() as conn:
        # Set up the database
        create_table(conn)

        # Example insert
        insert_student(conn, "Jane Doe", 23, "jane@example.com")

        # Example query
        students = fetch_students(conn)
        for student in students:
            print(student)

        print("Database setup complete.")

if __name__ == "__main__":
    main()
