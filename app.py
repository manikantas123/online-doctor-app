from flask import Flask, render_template_string, request, redirect, url_for, jsonify
import redis
import time

app = Flask(__name__)

# Redis client
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Simple in-memory doctor list (can be from DB in future)
doctors = [
    {"id": 1, "name": "Dr. Anjali Mehta", "specialty": "Cardiologist"},
    {"id": 2, "name": "Dr. Rakesh Sharma", "specialty": "Dermatologist"},
    {"id": 3, "name": "Dr. Nandini Rao", "specialty": "Psychiatrist"}
]

@app.route("/")
def home():
    return render_template_string(open("templates.html").read(), doctors=doctors)

@app.route("/consult", methods=["POST"])
def consult():
    name = request.form["name"]
    age = request.form["age"]
    doctor_id = request.form["doctor"]
    issue = request.form["issue"]
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    consultation = {
        "name": name,
        "age": age,
        "doctor_id": doctor_id,
        "issue": issue,
        "timestamp": timestamp
    }

    # Save in Redis
    r.lpush("consultations", str(consultation))
    return redirect(url_for("home"))

@app.route("/api/consultations")
def get_consultations():
    data = r.lrange("consultations", 0, 10)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
