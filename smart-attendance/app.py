from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def read_students():
    students = []
    with open('student.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

@app.route('/', methods=['GET', 'POST'])
def index():
    students = read_students()
    present = []
    absent = []

    if request.method == 'POST':
        present = request.form.getlist('present')

        for s in students:
            if s['roll'] not in present:
                absent.append(s['roll'])

    total = len(students)
    present_count = len(present)
    full_attendance = (present_count == total)

    return render_template(
        'index.html',
        students=students,
        present=present,
        absent=absent,
        total=total,
        present_count=present_count,
        full_attendance=full_attendance
    )

if __name__ == '__main__':
    app.run(debug=True)
