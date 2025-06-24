from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
import csv
from io import StringIO

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session handling

# In-memory data storage
students = []
student_id_counter = 1

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    global student_id_counter
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        student = {
            'id': student_id_counter,
            'name': name,
            'email': email,
            'phone': phone
        }
        students.append(student)
        student_id_counter += 1
        flash('Student added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return "Student not found", 404

    if request.method == 'POST':
        student['name'] = request.form['name']
        student['email'] = request.form['email']
        student['phone'] = request.form['phone']
        flash('Student updated successfully!', 'info')
        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    global students
    if 'user' not in session:
        return redirect(url_for('login'))

    students = [s for s in students if s['id'] != id]
    flash('Student deleted.', 'warning')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'dev' and password == 'yazh19':
            session['user'] = username
            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/export')
def export_csv():
    if 'user' not in session:
        return redirect(url_for('login'))

    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['ID', 'Name', 'Email', 'Phone'])

    for student in students:
        writer.writerow([student['id'], student['name'], student['email'], student['phone']])

    output = si.getvalue()
    si.close()

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=students.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True)
