# Student Performance Tracker

## Overview
The **Student Performance Tracker** is a web-based application designed to help teachers track and manage student performance across multiple subjects. This project leverages Python (Flask) for the backend and HTML/CSS for the frontend. Teachers can add students, input their scores, calculate individual and class averages, and even delete student records when necessary.

## Features
- **Add Students**: Input student names and their scores for three subjects.
- **View Performance**: Displays each student's average score and pass/fail status.
- **Class Average**: Calculates and displays the overall class average score.
- **Delete Students**: Remove student records from the tracker.
- **User-Friendly Interface**: Clean and intuitive design for seamless usage.

## Technologies Used
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- Basic understanding of Python and Flask.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-performance-tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd student-performance-tracker
   ```
3. Install required dependencies:
   ```bash
   pip install flask
   ```

### Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

### Using the Application
- **Add Students**: Fill out the form with the student’s name and scores for three subjects, then click "Add Student."
- **View Performance**: See a table displaying each student's name, average score, and pass/fail status.
- **Delete Students**: Use the delete button next to a student's record to remove them from the tracker.
- **Class Average**: View the overall class average at the bottom of the table.

## Project Structure
```
student-performance-tracker/
├── app.py           # Flask backend
├── templates/
│   └── index.html   # Frontend template
├── static/
│   └── style.css    # CSS styles
└── README.md        # Project documentation
```

## Future Enhancements
- Add support for more subjects.
- Enable score updates for existing students.
- Add authentication for teachers to secure data.

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- HTML and CSS tutorials: [W3Schools](https://www.w3schools.com/)

---

Feel free to fork the repository and contribute to the project!
