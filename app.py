from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(\"\"\"
        <h1>Online Doctor Consultation</h1>
        <form action='/consult' method='post'>
            <input name='name' placeholder='Your Name' required>
            <input name='symptom' placeholder='Your Symptoms' required>
            <button type='submit'>Consult Now</button>
        </form>
    \"\"\")

@app.route('/consult', methods=['POST'])
def consult():
    name = request.form['name']
    symptom = request.form['symptom']
    advice = f"Hi {name}, based on your symptoms ({symptom}), please consult a doctor if it persists."
    return jsonify({"message": advice})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
