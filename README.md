# Smart Todo CLI 🐍

A simple and lightweight command-line Todo application built with Python.

Smart Todo CLI allows you to manage your daily tasks directly from the terminal, with persistent JSON-based storage.

## ✨ Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 🔎 Search tasks
* 📊 View task statistics
* 💾 Persistent data storage using JSON
* 🚀 Lightweight and easy to use
* 🐍 Built entirely with Python

## 📁 Project Structure

```text
smart-todo-cli/
│
├── app.py          # Main application
├── todo.py         # Todo management functions
├── data.json       # Task storage
├── README.md       # Project documentation
└── .gitignore      # Git ignored files
```

## ⚙️ Requirements

* Python 3.8 or higher
* Git (optional, for development)

No external Python packages are required.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/develamir/smart-todo-cli.git
```

Navigate to the project directory:

```bash
cd smart-todo-cli
```

Run the application:

```bash
python app.py
```

## 🖥️ Usage

After starting the application, you will see the main menu:

```text
========================
       SMART TODO
========================
1. Add Task
2. Show Tasks
3. Complete Task
4. Delete Task
5. Search Task
6. Statistics
0. Exit
```

Choose an option by entering its corresponding number.

### Example

```text
Choose: 1
Task title: Learn Python

Task added successfully!
```

View your tasks:

```text
Choose: 2

========== TASKS ==========

1. [ ] Learn Python
```

## 💾 Data Storage

Tasks are stored locally in `data.json`.

Example:

```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "completed": false
    }
]
```

The application does not require a database or external service.

## 🛠️ Technologies

* Python
* JSON
* Command Line Interface
* Git & GitHub

## 🎯 Project Goals

This project was created as a simple Python project for practicing:

* Python functions
* File handling
* JSON data management
* Lists and dictionaries
* Command-line interfaces
* Git and GitHub workflow

## 🔮 Future Improvements

Possible future features:

* [ ] Task priorities
* [ ] Due dates
* [ ] Categories
* [ ] Colored terminal interface
* [ ] Task editing
* [ ] Better error handling
* [ ] SQLite database
* [ ] Unit tests

## 👨‍💻 Author

**develamir**

GitHub: https://github.com/develamir

## 📄 License

This project is open source and available under the MIT License.
