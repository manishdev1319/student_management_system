
# Student Management System – Flask App 

This is a lightweight web application built using Flask for managing student records. It uses in-memory data storage, no database required. You can add, edit, delete, and export students. The app also includes admin login/logout functionality.

---

## Features

* Admin login/logout
* Add student
* Edit student
* Delete student
* Export students to CSV
* In-memory data storage (no database)
* Stylish ocean-themed UI (mobile-friendly)

---

## Technologies Used

* Python 3.x
* Flask (lightweight web framework)
* HTML / CSS (with custom ocean theme)
* Bootstrap-style layout
* Google Fonts (Inter)

---

## Project Structure

student-management-system/
│
├── app.py                 → Main Flask application
├── requirements.txt       → Python dependencies
├── README.txt             → Project description and usage info
│
├── static/
│   ├── style.css          → Custom ocean-themed CSS
│   └── images/
│       └── ocean-bg.jpg   → Optional login background image
│
├── templates/
│   ├── base.html          → Base layout template
│   ├── login.html         → Admin login page
│   ├── index.html         → Student dashboard (list view)
│   ├── add.html           → Add student form
│   └── edit.html          → Edit student form

---

## How to Run the App

1. Create a virtual environment (optional but recommended):

   * `python -m venv venv`
   * On Windows: `venv\Scripts\activate`
   * On macOS/Linux: `source venv/bin/activate`

2. Install dependencies:

   * `pip install -r requirements.txt`
   * Or manually: `pip install Flask`

3. Start the Flask server:

   * `python app.py`

4. Open your browser and visit:

   * [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Admin Login

Default credentials:

* Username: `dev`
* Password: `yazh19`

---

## CSV Export

* While logged in, go to `/export` or click **Export CSV** to download student data as a `.csv` file.

---

## Next Steps / Improvements

* Add persistent database (SQLite, MySQL, etc.)
* Implement search/filtering
* Add pagination
* Use Flask Blueprints for larger structure
* Upload profile pictures for students

---

## License

Free to use for learning, academic, or demo purposes.

