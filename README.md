 Online Doctor Consultation App – End-to-End DevOps Implementation
A cloud-native full-stack healthcare platform that enables patients—especially in rural or remote areas—to consult doctors virtually via their devices. Built using real-world DevOps tools and practices like Docker, GitHub Actions, Kubernetes, and GKE.

🚀 Features
🧑‍⚕️ Patient and doctor login system

📅 Appointment booking and management

📦 Fully containerized using Docker

🔁 CI/CD with GitHub Actions

☁️ Cloud deployment with Google Kubernetes Engine (GKE)

📈 Scalable and production-ready infrastructure

🛠️ Tech Stack
Frontend:

Flask (Python)

HTML/CSS/JavaScript

Backend:

Python Flask

SQLite (or any DB)

DevOps & Tools:

Git & GitHub

GitHub Actions (CI/CD)

Docker & Docker Compose

Kubernetes (GKE)

Google Container Registry (GCR)

Monitoring: Prometheus + Grafana (Planned)
🔁 CI/CD Pipeline
Code is pushed to GitHub

GitHub Actions:

Lints and tests the code

Builds Docker image

Pushes to Google Container Registry (GCR)

Deploys to GKE using kubectl apply

🐳 Docker Setup (Local)
bash
Copy
Edit
# Clone the repo
git clone https://github.com/manikantas123/online-doctor-app.git
cd online-doctor-app

# Build Docker image
docker build -t doctor-app .

# Run locally
docker run -p 5000:5000 doctor-app
Or using Docker Compose:

bash
Copy
Edit
docker-compose up --build
☁️ Kubernetes Setup on GKE
bash
Copy
Edit
# Set GCP project
gcloud config set project YOUR_PROJECT_ID

# Push image to GCR
docker tag doctor-app gcr.io/YOUR_PROJECT_ID/doctor-app
docker push gcr.io/YOUR_PROJECT_ID/doctor-app

# Deploy to GKE
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
✅ Testing and Validation
✔️ Patient & doctor login tested

✔️ Appointment flow tested manually

✔️ GitHub Actions CI runs on every push

✔️ Kubernetes services validated using kubectl

✔️ Container logs checked with docker logs

<img width="1904" height="923" alt="Screenshot 2025-07-21 154001" src="https://github.com/user-attachments/assets/aebe413d-9909-45f9-8ea5-b96e83ba0ecc" />


Login page

Doctor dashboard

GitHub Actions workflow

Kubernetes dashboard

GKE LoadBalancer IP output

📚 Learning Outcomes
Deployed a full-stack app using DevOps lifecycle

Practiced CI/CD, containerization, and cloud-native deployment

Gained hands-on exposure to Kubernetes and GitHub automation

Developed a real-world application solving a meaningful problem

📎 Links
🔗 GitHub Repository

🌐 Portfolio Website

👨‍💻 LinkedIn Profile

👨‍💻 Author
Mummidi Manikanta
B.Tech CSE @ Lovely Professional University
Open to roles in Data Science, DevOps, and Cloud Engineering

Built with ❤️ to bring healthcare and DevOps together.
