from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Quiz Page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Result Page
@app.route('/result')
def result():

    subject = request.args.get('subject')

    if subject == "cs":
        careers = [
            "Software Engineer",
            "Cybersecurity Analyst",
            "AI Engineer",
            "Data Scientist",
            "Cloud Engineer"
        ]

    elif subject == "bio":
        careers = [
            "Doctor",
            "Nurse",
            "Psychologist",
            "Biotechnologist",
            "Pharmacist"
        ]

    elif subject == "commerce":
        careers = [
            "Chartered Accountant",
            "Financial Analyst",
            "Investment Banker",
            "Entrepreneur",
            "Business Analyst"
        ]

    elif subject == "arts":
        careers = [
            "Fashion Designer",
            "Model",
            "Graphic Designer",
            "Actor",
            "Content Creator"
        ]

    else:
        careers = ["Career recommendation unavailable"]

    return render_template('result.html', careers=careers)

# Career Categories Page
@app.route('/c')
def careers():
    return render_template('careers.html')

# Run the App
if __name__ == "__main__":
    app.run(debug=True)