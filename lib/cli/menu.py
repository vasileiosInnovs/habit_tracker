from tabulate import tabulate
from lib.db.session import session
from lib.models.user import User
from lib.models.habit import Habit
from lib.models.log import Log

def login_or_register():
    print("\nWelcome to BetterEveryday")
    while True:
        action = input("Do you want to [login] or [register]? ").strip().lower()
        if action in ("login", "register"):
            break
        print("Please enter 'login' or 'register'.")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    email = input("Enter email: ").strip()

    if action == "register":
        if User.get_by_username(session, username):
            print("Username already exists. Try logging in.")
            return login_or_register()
        elif User.get_by_username(session, email):
            print("Email already exists.")
            return login_or_register()
        user = User(username=username, password=password)
        user.save(session)
        print("Registration successful. You're now logged in.")
        return user

    elif action == "login":
        user = User.get_by_username(session, username)
        if user and user.password == password:
            print("Login successful!")
            return user
        else:
            print("Invalid credentials.")
            return login_or_register()


def list_habits():
    habits = session.query(Habit).all()
    if not habits:
        print("No habits found.")
    for habit in habits:
        print(habit)

def create_habit():
    name = input("Enter habit name: ")
    description = input("Enter a description of the habit: ")
    time_period = input("Enter time period: ")
    category = input("Enter habit category: ")
    frequency = int(input("Enter frequency (daily/weekly): "))

    habit = Habit(
        name=name,
        description=description,
        time_period=time_period,
        category=category,
        frequency=frequency
    )    
    habit.save(session)
    print("Habit created successfully.")

def main_menu(user):
    print(f"\nWelcome, {user}!")

    while True:
        print("\n📈 BetterEveryday Habit Tracker")
        print("1. Create a new habit")
        print("2. Log progress")
        print("3. View report")
        print("4. Quit")

        choice = input("\Choose an option: ").strip()

        if choice == "1":
            create_habit()

        elif choice == "2":
            log_progress()

        elif choice == "3":
            view_report()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")

def create_habit():
    name = input("Enter habit name: ").strip()
    frequency = input("Enter frequency (daily/weekly): ").strip().lower()
    print(f"Habit '{name}' with {frequency} frequency created.")

def log_progress():
    habit_name = input("Enter habit name: ").strip()
    status = input("Accomplished?[Y/N]: ").strip()
    print(f"Progress logged for habit {habit_name}.")

def view_report():
    habit_name = input("Enter habit name: ").strip()
    logs = Log.get_logs_by_habit(session, habit_name)

    if not logs:
        print("⚠️ No logs found.")
        return
    
    table = [[log.id, log.habit_name, log.status, log.timestamp.strftime("%Y-%m-%d %H:%M")] for log in logs]
    print(tabulate(table, headers=['ID', 'Habit', 'Status', 'Timestamp'], tablefmt="fancy_grid"))