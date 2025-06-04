from tabulate import tabulate
from lib.db.session import session
from lib.models.user import User

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
    from lib.models.habit import Habit

    habits = session.query(Habit).all()
    if not habits:
        print("No habits found.")
    for habit in habits:
        print(habit)

def create_habit(user):
    name = input("Enter habit name: ").strip()
    description = input("Enter a description of the habit: ").strip()
    time_period = input("Enter time period (e.g. morning): ").strip()
    category = input("Enter habit category (e.g. health): ").strip()
    frequency = int(input("Enter frequency (e.g. 7): "))

    from lib.models.habit import Habit

    habit = Habit(
        name=name,
        description=description,
        time_period=time_period,
        category=category,
        frequency=frequency,
        user_id=user.id 
    )
    habit.save(session)
    print(f"✅ Habit '{name}' created for {user.username}.")

def main_menu(user):
    print(f"\nWelcome, {user.username}!")

    while True:
        print("\n📈 BetterEveryday Habit Tracker")
        print("1. Create a new habit")
        print("2. Log progress")
        print("3. View report")
        print("4. Delete a habit")
        print("5. Logout")
        print("6. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_habit(user)

        elif choice == "2":
            log_progress(user)

        elif choice == "3":
            view_report(user)

        elif choice == "4":
            delete_habit(user)

        elif choice == "5":
            print("Logging out...")
            return 

        elif choice == "6":
            print("Goodbye!")
            return "quit"

        else:
            print("❌ Invalid option. Try again.")

def log_progress(user):

    from lib.models.habit import Habit

    habits = session.query(Habit).filter_by(user_id=user.id).all()
    if not habits:
        print("You have no habits to log.")
        return

    print("\nYour habits:")
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit.name}")

    try:
        choice = int(input("Select habit number: "))
        habit = habits[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    from lib.models.log import Log

    status = input("Accomplished? [Y/N]: ").strip().upper()
    log = Log(status=status, habit_id=habit.id)
    session.add(log)
    session.commit()
    print(f"Progress logged for '{habit.name}'.")

def view_report(user):
    from lib.models.habit import Habit

    habits = session.query(Habit).filter_by(user_id=user.id).all()
    if not habits:
        print("No habits found for this user.")
        return

    print("\nYour habits:")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit.name}")

    try:
        index = int(input("Choose habit number to view logs: "))
        habit = habits[index - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    
    from lib.models.log import Log

    logs = Log.get_logs_for_user_habit(session, user.username, habit.name)

    if not logs:
        print("⚠️ No logs found.")
        return

    table = [[log.id, habit.name, log.status, log.timestamp.strftime("%Y-%m-%d %H:%M")] for log in logs]
    print(tabulate(table, headers=['ID', 'Habit', 'Status', 'Timestamp'], tablefmt="fancy_grid"))

def delete_habit(user):
    from lib.models.habit import Habit
    from lib.models.log import Log

    habits = session.query(Habit).filter_by(user_id=user.id).all()
    if not habits:
        print("❌ You have no habits to delete.")
        return

    print("\n🗑️ Your habits:")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit.name}")

    try:
        index = int(input("Select habit number to delete: "))
        habit_to_delete = habits[index - 1]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    confirm = input(f"Are you sure you want to delete '{habit_to_delete.name}'? [y/N]: ").strip().lower()
    if confirm == "y":
        session.query(Log).filter_by(habit_id=habit_to_delete.id).delete()
        session.delete(habit_to_delete)
        session.commit()
        print(f"✅ Habit '{habit_to_delete.name}' has been deleted.")
    else:
        print("❎ Deletion cancelled.")
