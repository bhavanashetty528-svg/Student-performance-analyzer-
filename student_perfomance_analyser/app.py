from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    roll = request.form['roll']
    section = request.form['section']

    marks = {
        "Maths": int(request.form['maths']),
        "Chemistry": int(request.form['chemistry']),
        "Mechanics": int(request.form['mechanics']),
        "AI": int(request.form['ai']),
        "Communication": int(request.form['communication']),
        "Python": int(request.form['python'])
    }

    total = sum(marks.values())
    average = total / 6

    suggestions = []
    fail = False

    for subject, mark in marks.items():
        if mark < 35:
            fail = True
        if mark < 50:
            suggestions.append(f"📌 Improve {subject} by practicing daily and revising basics.")

    if fail:
        status = "Fail ❌"
        category = "Needs Improvement 😢"
        reward = "No reward. Focus and try again 💪"
    else:
        if average >= 80:
            category = "Excellent 🌟"
            reward = "🏆 Gold Medal + Certificate"
        elif average >= 60:
            category = "Good 👍"
            reward = "🥈 Silver Medal"
        else:
            category = "Average 😐"
            reward = "🎖 Participation Certificate"

        status = "Pass ✅"

    return render_template(
        'result.html',
        name=name,
        roll=roll,
        section=section,
        marks=marks,
        total=total,
        average=round(average, 2),
        status=status,
        category=category,
        reward=reward,
        suggestions=suggestions
    )

if __name__ == '__main__':
    app.run(debug=True)
