from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Add Student
@app.route("/add")
def add_student():
    return render_template("add_student.html")


# View Students
@app.route("/students")
def students():
    return render_template("students.html")


if __name__ == "__main__":
    app.run(debug=True)
