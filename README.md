
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

1.app.py – Main Flask application file

2.requirements.txt – List of Python dependencies

3.README.txt – Project documentation and instructions

4.static/ – Static files directory
4.1. style.css – Custom ocean-themed CSS stylesheet
4.2. images/ – Image assets
    4.2.1. ocean-bg.jpg – Optional background image for login page

5.templates/ – HTML templates folder
5.1. base.html – Base layout for all pages
5.2. login.html – Admin login page
5.3. index.html – Dashboard with list of students
5.4. add.html – Add student form
5.5. edit.html – Edit student form

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

