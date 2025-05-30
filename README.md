
# 📈 BetterEveryday - Habit Tracker CLI App

**BetterEveryday** is a command-line application that helps users build better habits through daily logging and reporting. Built with Python and SQLAlchemy, it provides a simple and interactive experience to track your progress and stay accountable.

---

## 🚀 Features

- ✅ Register and log in as a user
- 🛠️ Create and manage habits
- 📆 Log daily or weekly habit progress
- 📊 View habit activity reports
- 🧠 Structured with SQLAlchemy, SQLite, and tabulate

---

## 🗂️ Project Structure

```

better-everyday/
├── lib/
│   ├── db/
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   ├── habit.py
│   │   └── log.py
├── main.py
├── requirements.txt
├── README.md
├── setup.py (optional)
└── .gitignore

````

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/vasileiosInnovs/habit_tracker
cd better-everyday
````

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

To start the habit tracker:

```bash
python main.py
```

Then follow the prompts to register or log in, create habits, log progress, and view reports.

---

## 💻 Dependencies

* `sqlalchemy` – ORM for database modeling
* `tabulate` – Used for formatting output tables
* `datetime` – For timestamps

Install them via:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Developer Notes

* Uses SQLite as the database engine
* Easily extendable with more features (e.g. reminders, goals, analytics)
* Modular codebase using OOP principles

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

Inspired by the need for simple and effective personal growth tools. Built with love and Python 🐍.