# 📝 Python To-Do List Application

A simple, lightweight, command-line To-Do List Application built using Python. It allows users to manage their daily tasks through an interactive menu and stores tasks locally in a text file.

## ✨ Features

- **Add Tasks:** Add one or multiple tasks at once.
- **View Tasks:** Automatically displays previously saved tasks when the application starts.
- **Mark Tasks as Done:** Mark completed tasks with a `[✓]` indicator.
- **Clear All Tasks:** Remove all saved tasks.
- **Task Persistence:** Tasks are stored in a text file and remain saved even after closing the application.
- **Modular Structure:** Functions are organized into separate Python files for better code organization and maintainability.
- **Input Validation:** Handles invalid numerical inputs and task selections.

## 🛠️ Technologies Used

- Python 3
- File Handling
- Functions and Modules
- Exception Handling
- Conditional Statements and Loops

## 📁 Project Structure

```text
To-Do/
│
├── main.py
├── add_task.py
├── mark_tasks.py
├── delete_tasks.py
├── tasks.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd To-Do
```

### 3. Run the Application

```bash
python3 main.py
```

## 📖 How to Use

After running the application, an interactive menu will appear.

```text
Enter the option number:

    1. Enter new tasks.
    2. Mark one task as done.
    3. Clear all tasks.
    4. Exit.
```

Choose the corresponding option number to perform an operation.

### Task Completion Example

Tasks are stored in `tasks.txt` using the following format:

```text
[ ] Learn Python
[✓] Build a project
[ ] Practice JavaScript
```

The `[ ]` indicator represents a pending task, while `[✓]` represents a completed task.

## 💾 Data Storage

The application uses a simple text file (`tasks.txt`) to store tasks.

All changes are saved directly to this file, allowing tasks to persist between application sessions.

## 🎯 Project Goal

This project was developed to practice Python programming concepts, particularly:

- File handling and data persistence.
- Creating and importing custom modules.
- Writing and organizing functions.
- Exception handling and input validation.
- Building interactive command-line applications.

---

**Made with Python 🐍**