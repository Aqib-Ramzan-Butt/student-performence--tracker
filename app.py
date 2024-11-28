from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        """Calculate the average of the student's scores."""
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        """Check if the student is passing all subjects."""
        return all(score >= passing_score for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        """Add a new student to the tracker."""
        self.students[name] = Student(name, scores)

    def delete_student(self, name):
        """Delete a student from the tracker."""
        if name in self.students:
            del self.students[name]

    def calculate_class_average(self):
        """Calculate the overall average score for the entire class."""
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def get_all_students(self):
        """Retrieve all student data."""
        return [
            {
                "name": student.name,
                "average": student.calculate_average(),
                "status": "Passing" if student.is_passing() else "Needs Improvement",
            }
            for student in self.students.values()
        ]

tracker = PerformanceTracker()

@app.route("/")
def index():
    students = tracker.get_all_students()
    class_average = tracker.calculate_class_average()
    return render_template("index.html", students=students, class_average=class_average)

@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form.get("name")
    try:
        scores = list(map(int, [request.form.get("score1"), request.form.get("score2"), request.form.get("score3")]))
        tracker.add_student(name, scores)
    except ValueError:
        pass  # Handle invalid score input gracefully
    return redirect(url_for("index"))

@app.route("/delete_student", methods=["POST"])
def delete_student():
    name = request.form.get("name")
    tracker.delete_student(name)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
