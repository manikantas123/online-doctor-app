from flask import Flask, request, render_template_string, url_for

app = Flask(__name__, static_url_path='/static')

# HTML Template
html_home = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Online Doctor Consultation</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #e8f0fe, #ffffff);
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #2e7d32;
            color: white;
            padding: 1rem 2rem;
            text-align: center;
            position: relative;
        }
        header img.logo {
            width: 100px;
            position: center;
            left: 20px;
            top: 100px;
        }
        h1 {
            margin: 0;
            font-size: 2rem;
        }
        .container {
            max-width: 700px;
            margin: 3rem auto;
            padding: 2rem;
            background: white;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h2 {
            margin-bottom: 1rem;
            color: #333;
        }
        input, textarea {
            width: 100%;
            padding: 1rem;
            margin: 0.8rem 0;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 1rem;
        }
        button {
            background-color: #388e3c;
            color: white;
            padding: 1rem;
            border: none;
            border-radius: 6px;
            width: 100%;
            font-size: 1.1rem;
            cursor: pointer;
            margin-top: 1rem;
        }
        button:hover {
            background-color: #2e7d32;
        }
        footer {
            text-align: center;
            padding: 1rem;
            background-color: #f0f0f0;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <img src="https://www.shutterstock.com/shutterstock/photos/2496772443/display_1500/stock-photo-portrait-of-a-emirates-male-medical-doctor-gentle-smile-light-on-centre-of-face-carrying-2496772443.jpg" class="logo" alt="Doctor Logo">
        <h1>Online Doctor Consultation</h1>
    </header>
    <div class="container">
        <h2>Book Your Consultation</h2>
        <form action="/consult" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <textarea name="symptoms" placeholder="Describe your symptoms" required></textarea>
            <button type="submit">Submit Consultation</button>
        </form>
    </div>
    <footer>
        &copy; 2025 Online Doctor Platform. All rights reserved.
    </footer>
</body>
</html>
"""

thank_you_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Thank You</title>
    <style>
        body {
            background: #e3f2fd;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 4rem;
        }
        .card {
            background: white;
            padding: 2rem;
            margin: auto;
            max-width: 600px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.15);
        }
        blockquote {
            background: #f1f8e9;
            padding: 1rem;
            border-left: 5px solid #4caf50;
            font-style: italic;
            margin: 1rem auto;
        }
        a {
            display: inline-block;
            margin-top: 2rem;
            text-decoration: none;
            color: white;
            background: #4caf50;
            padding: 0.8rem 1.5rem;
            border-radius: 5px;
        }
        a:hover {
            background: #388e3c;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Thank You, {{ name }}!</h2>
        <p>Your symptoms have been recorded:</p>
        <blockquote>{{ symptoms }}</blockquote>
        <p>Our doctor will contact you shortly. Stay healthy!</p>
        <a href="/">Back to Home</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_home)

@app.route('/consult', methods=['POST'])
def consult():
    name = request.form.get("name")
    symptoms = request.form.get("symptoms")
    return render_template_string(thank_you_template, name=name, symptoms=symptoms)

@app.route('/doctor')
def doctor_info():
    return {
        "name": "Dr. R. Kiran",
        "specialization": "General Physician",
        "contact": "doctor@example.com",
        "available": "9AM - 6PM IST"
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
