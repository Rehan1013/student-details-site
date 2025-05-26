from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Add /student?id=101 to the URL to see student info."

@app.route('/student')
def student_page():
    student_id = request.args.get('id')
    if not student_id:
        return "No student ID provided."

    df = pd.read_csv("students.csv")
    student = df[df['ID'] == int(student_id)].to_dict(orient='records')
    if student:
        return render_template("student.html", student=student[0])
    else:
        return "Student not found."

if __name__ == '__main__':
    app.run()
