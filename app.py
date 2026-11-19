
import pymysql


# Function to connect to MySQL
def create_connection():
    return pymysql.connect(
        host="172.17.0.2",
        user="root",
        password="hello",
        database="user-info",
        port=3306
    )


# Function to create table
def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usernames (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()


# Function to insert username
def insert_name(connection, name):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO usernames (name) VALUES (%s)",
        (name,)
    )

    connection.commit()
    cursor.close()

    print(f"Username '{name}' added successfully!")


# Function to display all usernames
def fetch_all_usernames(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM usernames")

    usernames = cursor.fetchall()

    cursor.close()

    return usernames


# Main function
def main():

    try:
        connection = create_connection()
        print("Successfully connected to MySQL!")

    except pymysql.MySQLError as error:
        print("MySQL connection failed:", error)
        return

    create_table(connection)

    while True:

        print("\n===== USER MANAGEMENT SYSTEM =====")
        print("1. Add a username")
        print("2. Show all usernames")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter username: ").strip()

            if name:
                insert_name(connection, name)
            else:
                print("Username cannot be empty!")

        elif choice == "2":

            usernames = fetch_all_usernames(connection)

            if usernames:
                print("\n===== ALL USERNAMES =====")

                for user in usernames:
                    print(f"ID: {user[0]} | Name: {user[1]}")

            else:
                print("No usernames found.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

    connection.close()
    print("MySQL connection closed.")


if __name__ == "__main__":
    main()
