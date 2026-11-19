# 🐍 Python MySQL User Management System

A simple menu-driven User Management System built using **Python and MySQL**, with both services running in separate Docker containers.

The application connects to a MySQL database using PyMySQL and allows users to add new usernames and view all existing usernames. Docker makes the application easy to build and run in an isolated environment.

## 🚀 Features

- Connects Python application to a MySQL database.
- Adds new usernames to the database.
- Displays all existing usernames.
- Automatically creates the required database table.
- Uses separate Docker containers for Python and MySQL.
- Uses Docker for application containerization.

## 🛠️ Technologies Used

- Python 3.11
- MySQL
- PyMySQL
- Docker
- Docker Images and Containers
- Docker Networking

## 📂 Project Structure

```text
python-mysql-docker-user-management/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

## 🐳 Docker Setup

### 1. Run the MySQL Container

Create a MySQL container:

```bash
docker run -d \
  --name mysqldb \
  -e MYSQL_ROOT_PASSWORD=hello \
  -e MYSQL_DATABASE=user-info \
  mysql
```

### 2. Build the Python Docker Image

Navigate to the project directory and execute:

```bash
docker build -t user-management-app .
```

### 3. Run the Python Container

```bash
docker run -it --rm user-management-app
```

**Note:** Both containers must be connected to the same Docker network. Update the MySQL host in `app.py` to match the reachable container hostname or IP address.

## 💻 Application Menu

When the Python application starts, it displays:

```text
===== USER MANAGEMENT SYSTEM =====

1. Add a username
2. Show all usernames
3. Quit

Enter your choice:
```

### Add a Username

```text
Enter your choice: 1
Enter username: Ansh

Username 'Ansh' added successfully!
```

### View All Usernames

```text
Enter your choice: 2

===== ALL USERNAMES =====

ID: 1 | Name: Ansh
ID: 2 | Name: Rahul
```

## 📦 Python Dependencies

The project uses the following Python packages:

- **PyMySQL:** Connects Python to MySQL.
- **Cryptography:** Provides cryptographic support required by the configured MySQL authentication.

Install dependencies locally using:

```bash
pip install -r requirements.txt
```

## 🎯 Learning Outcomes

Through this project, I learned:

- How to create and manage Docker containers.
- How to build a custom Docker image using a Dockerfile.
- How to connect two separate containers.
- How to connect Python applications with MySQL.
- How to execute SQL queries using PyMySQL.
- How to insert and retrieve data from a database.
- How to manage Python dependencies in Docker.

## 🔮 Future Improvements

- Implement Docker Compose.
- Configure persistent MySQL storage