# 📚 Basic Library Project

A simple Library Management web application built using **Flask**, **SQLite**, and **SQLAlchemy** to learn database integration and implement CRUD (Create, Read, Update, Delete) operations.

## 🚀 Overview

This project was built as a hands-on learning exercise to understand how Flask applications interact with databases using SQLAlchemy ORM.

Users can:

* Add new books
* View all books
* Update book ratings
* Store data permanently using SQLite

The project focuses on understanding database concepts rather than UI design.

---

## ✨ Features

* 📖 Add books to the library
* 👀 Display all books
* ⭐ Update book ratings
* 🗄️ Store data using SQLite
* 🔗 Database interaction using SQLAlchemy ORM
* 🌐 Dynamic pages using Flask and Jinja templates

---

## 🛠️ Tech Stack

### Backend

* Python 3.12
* Flask
* Flask-SQLAlchemy
* SQLAlchemy

### Database

* SQLite

### Frontend

* HTML
* Jinja2 Templates

---

## 📂 Project Structure

```text
basic-library-project/

├── main.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── add.html
│   └── EditRating.html
│
├── instance/
│   └── new-books-collection.db
│
├── .gitignore
└── README.md
```

---

## 🧠 Concepts Learned

* Flask routing
* HTML forms
* GET and POST requests
* Jinja templating
* SQLite databases
* SQLAlchemy models
* Database sessions
* CRUD operations

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/keshava-in-me/basic-library-project.git

cd basic-library-project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows

```bash
.\.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📝 CRUD Operations Implemented

### Create

Add new books to the database.

### Read

Display all books stored in the database.

### Update

Modify an existing book's rating.

### Delete

Planned for future implementation.

---

## 🔮 Future Improvements

* [ ] Delete books
* [ ] Search books
* [ ] Sort books
* [ ] Add book covers
* [ ] Flash messages
* [ ] Better UI styling
* [ ] Pagination

---

## 📚 Learning Goal

The purpose of this project is to learn how Flask applications interact with databases and how ORM simplifies database management compared to writing raw SQL queries.

---

## 👨‍💻 Author

**Keshav Kant**

NIT Durgapur

GitHub: https://github.com/keshava-in-me
