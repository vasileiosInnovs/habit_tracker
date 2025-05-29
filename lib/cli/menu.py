from lib.db.session import session
from lib.models.habit import Habit

def list_habits():
    habits = session.query(Habit).all()
    if not habits:
        print("No habits found.")
    for habit in habits:
        print(habit)

def create_habit():
    name = input("Enter habit name: ")
    description = input("Enter habit name: ")
    time_period = input("Enter habit name: ")
    category = input("Enter habit name: ")
    frequency = int(input("Enter habit name: "))

    habit = Habit(
        name=name,
        description=description,
        time_period=time_period,
        category=category,
        frequency=frequency
    )    
    habit.save(session)
    print("Habit created successfully.")

def main_menu():
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
    status = input("Accomplished?: ").strip()
    print(f"Progress logged for habit {habit_name}.")

def view_report():
    habit_name = input("Enter habit name: ").strip()
    print(f"Showing report for habit {habit_name}.")

