from flask import Flask, request, jsonify
from datetime import datetime
import pytz
import random

app = Flask(__name__)

MCQ_TEMPLATE = [
    {"question": "What is the main concept in the notes?", "options": ["ConceptA", "ConceptB", "ConceptC", "ConceptD"], "answer": "ConceptA"},
    # Fill out 15 such entries dynamically in real scenario based on file content
]

feedback_list = []

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    content = file.read().decode('utf-8')
    # Parse and extract main concepts for MCQ generation here
    return jsonify({"status": "success", "message": "File uploaded.", "concepts": ["ConceptA", "ConceptB"] })

@app.route("/generate_mcq", methods=["POST"])
def generate_mcq():
    # Dynamically create 15 MCQs from uploaded notes
    questions = random.sample(MCQ_TEMPLATE, 15)
    return jsonify({"questions": questions})

@app.route("/submit_test", methods=["POST"])
def submit_test():
    data = request.json
    score = data.get('score', 0)
    if score > 12:
        feedback = "Wow! Very good, keep it up."
    elif 7 <= score <= 11:
        feedback = "Good, but you need to try harder."
    else:
        feedback = "Nice try, but you need more practice."
    return jsonify({"score": score, "feedback": feedback})

@app.route("/time", methods=["GET"])
def get_indian_time():
    india = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india)
    return jsonify({"indian_time": now.strftime("%d-%m-%Y %H:%M:%S")})

@app.route("/ai_teacher", methods=["POST"])
def ai_teacher():
    notes = request.json.get("notes")
    # Connect to cloud AI API, e.g., OpenAI API, for teacher-like answers (pseudo response)
    response = f"AI Teacher says: These notes talk about {notes}. Focus on the main points."
    return jsonify({"message": response})

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    fb = request.json.get("feedback")
    feedback_list.append(fb)
    return jsonify({"status": "success", "feedbacks": feedback_list})

@app.route("/all_feedbacks", methods=["GET"])
def all_feedbacks():
    return jsonify({"feedbacks": feedback_list})

if __name__ == "__main__":
    app.run(debug=True)




