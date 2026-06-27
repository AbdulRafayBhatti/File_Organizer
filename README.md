# 📂 Python File Organizer

A simple Python automation script that organizes files into folders based on their file extensions.

This project demonstrates the use of Python's built-in file handling libraries to automatically sort files into categorized directories, making folders cleaner and easier to manage.

---

# 📌 Project Overview

Managing folders with hundreds of mixed files can be time-consuming.

This script scans a selected directory, identifies each file's extension, creates a folder for that extension (if it doesn't already exist), and moves the file into the corresponding folder.


---

# 💼 Problem Statement

Folders often become cluttered with files of different types, making it difficult to locate documents quickly.

This project automates file organization by sorting files into extension-based folders.

---

# ⚙️ Features

- Automatically scans a selected folder
- Detects file extensions
- Creates folders for each file type
- Moves files into corresponding folders
- Ignores directories
- Detects files without extensions
- Simple command-line interface

---

# 🏗 Workflow

```text
User Inputs Folder Path
          │
          ▼
Read All Files
          │
          ▼
Check File Extension
          │
          ├── No Extension
          │      │
          │      ▼
          │   Display Message
          │
          ▼
Create Folder (if needed)
          │
          ▼
Move File
          │
          ▼
Repeat Until Complete
          │
          ▼
Sorting Finished
```

---

# 🛠 Technologies Used

- Python 3
- os module
- shutil module

---

# 📂 Project Structure

```text
Python-File-Organizer/
│
├── organizer.py
└── README.md
```

---

# ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/AbdulRafayBhatti/File_Organizer.git
```

2. Navigate to the project directory.

```bash
cd File_Organizer
```

3. Run the script.

```bash
FileSorter.py
```

4. Enter the folder path you want to organize.

Example:

```text
Enter the folder path you want to sort:
C:\Users\Rafay\Downloads
```

---

# 📋 Example

### Before

```text
Downloads/
├── Resume.pdf
├── Photo.jpg
├── Python.zip
├── Notes.txt
├── Music.mp3
```

### After

```text
Downloads/
├── PDF/
│   └── Resume.pdf
├── JPG/
│   └── Photo.jpg
├── ZIP/
│   └── Python.zip
├── TXT/
│   └── Notes.txt
└── MP3/
    └── Music.mp3
```

---

# 🧠 Python Concepts Demonstrated

- File Handling
- Directory Management
- Exception Handling
- String Manipulation
- Loops
- Conditional Statements
- Python Standard Library

---

# 🎯 Learning Outcomes

Through this project, the following skills were strengthened:

- Python File Handling
- Automation Scripting
- Working with Directories
- Error Handling
- Standard Library Usage
- Problem Solving

---

# 🚀 Future Improvements

Possible enhancements include:

- Graphical User Interface (GUI)
- Undo functionality
- Organize by file size
- Organize by creation date
- Duplicate file detection
- Logging support
- Recursive folder organization

---

# 🙌 Acknowledgment

Special thanks to:

## 🎓 Alex The Analyst

YouTube Channel: https://www.youtube.com/@AlexTheAnalyst

for providing valuable Python and data analytics learning resources.

---

# 👨‍💻 Author

## Abdul Rafay Bhatti
Aspiring Data Analyst | Python Enthusiast | Data Analytics Learner
