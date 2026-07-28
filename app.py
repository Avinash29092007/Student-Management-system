from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    department = request.form["department"]
    year = request.form["year"]

    students.append({
        "name": name,
        "department": department,
        "year": year
    })

    return redirect("/students")

@app.route("/students")
def view_students():
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
