IS601 Module 8 - FastAPI Calculator Application

A FastAPI-based calculator web application with full test coverage, logging, CI/CD pipeline, and Docker support.

🚀 Live Demo
Docker Hub: https://hub.docker.com/r/kdulobo12/is601_module8
Github: https://github.com/kdulobo12/IS601_Module8_WebApplication

📋 Features

Calculator Operations: Add, Subtract, Multiply, Divide
REST API: FastAPI with Pydantic validation
Web UI: Browser-based calculator interface
Logging: Full request and error logging throughout the application
Tests: Unit, Integration, and End-to-End tests
CI/CD: GitHub Actions pipeline with security scanning and Docker deployment


🛠️ Tech Stack

Backend: Python 3.10, FastAPI, Uvicorn
Testing: Pytest, Playwright
Containerization: Docker, Docker Compose
CI/CD: GitHub Actions, Trivy Security Scanner
Registry: Docker Hub


📁 Project Structure
IS601_Module8/
├── .github/
│   └── workflows/
│       └── test.yml                    # GitHub Actions CI/CD workflow
├── app/
│   └── operations/
│       └── __init__.py                 # Calculator operations with logging
├── templates/
│   └── index.html                      # Web UI
├── tests/
│   ├── unit/
│   │   └── test_calculator.py          # Unit tests
│   ├── integration/
│   │   └── test_fastapi_calculator.py  # Integration tests
│   └── e2e/
│       └── test_e2e.py                 # End-to-end Playwright tests
├── main.py                             # FastAPI application
├── Dockerfile                          # Docker image definition
├── docker-compose.yml                  # Docker Compose configuration
├── requirements.txt                    # Python dependencies
└── pytest.ini                          # Pytest configuration

📦 Project Setup

🧩 1. Install Homebrew (Mac Only)

Skip this step if you're on Windows.

Homebrew is a package manager for macOS. You'll use it to easily install Git, Python, Docker, etc.
Install Homebrew:
bash/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Verify Homebrew:
bashbrew --version
If you see a version number, you're good to go.

🧩 2. Install and Configure Git
Install Git

MacOS (using Homebrew)

bashbrew install git

Windows

Download and install Git for Windows. Accept the default options during installation.
Verify Git:
bashgit --version
Configure Git Globals
Set your name and email so Git tracks your commits properly:
bashgit config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
Confirm the settings:
bashgit config --list
Generate SSH Keys and Connect to GitHub

Only do this once per machine.


Generate a new SSH key:

bashssh-keygen -t ed25519 -C "your_email@example.com"
(Press Enter at all prompts.)

Start the SSH agent:

basheval "$(ssh-agent -s)"

Add the SSH private key to the agent:

bashssh-add ~/.ssh/id_ed25519

Copy your SSH public key:


Mac/Linux:

bashcat ~/.ssh/id_ed25519.pub | pbcopy

Windows (Git Bash):

bashcat ~/.ssh/id_ed25519.pub | clip

Add the key to your GitHub account:

Go to GitHub SSH Settings
Click New SSH Key, paste the key, save.


Test the connection:

bashssh -T git@github.com
You should see a success message.

🧩 3. Clone the Repository
bashgit clone <repository-url>
cd <repository-directory>

🛠️ 4. Install Python 3.10+
Install Python

MacOS (Homebrew)

bashbrew install python

Windows

Download and install Python for Windows.
✅ Make sure you check the box Add Python to PATH during setup.
Verify Python:
bashpython3 --version
# or
python --version
Create and Activate a Virtual Environment
bashpython3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate.bat     # Windows
Install Required Packages
bashpip install -r requirements.txt
playwright install chromium

🐳 5. Docker Setup (Optional)
Install Docker

Install Docker Desktop for Mac
Install Docker Desktop for Windows

Pull from Docker Hub
bashdocker pull kdulobo12/is601_module8:latest
Build Docker Image
bashdocker build -t is601_module8 .
Run Docker Container
bashdocker run -p 8000:8000 is601_module8
Run with Docker Compose
bashdocker compose up

🚀 6. Running the Project

Without Docker:

bashuvicorn main:app --reload

With Docker:

bashdocker run -p 8000:8000 kdulobo12/is601_module8:latest
Visit: http://localhost:8000

📝 7. Submission Instructions
After finishing your work:
bashgit add .
git commit -m "Complete Module 8"
git push origin main
Then submit the GitHub repository link as instructed.

🧪 Running Tests
All tests
bashpytest
Unit tests only
bashpytest tests/unit/ -v
Integration tests only
bashpytest tests/integration/ -v
End-to-End tests
bash# Start the server first
uvicorn main:app --host 127.0.0.1 --port 8000 &
pytest tests/e2e/ -v

📡 API Endpoints
MethodEndpointDescriptionGET/Calculator web UIPOST/addAdd two numbersPOST/subtractSubtract two numbersPOST/multiplyMultiply two numbersPOST/divideDivide two numbers
Example Request
bashcurl -X POST http://localhost:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'
Example Response
json{ "result": 15.0 }

🔁 CI/CD Pipeline
The GitHub Actions workflow runs automatically on every push to main:
JobDescriptiontestRuns unit, integration, and E2E testssecurityTrivy vulnerability scan on Docker imagedeployBuilds and pushes image to Docker Hub

🔥 Useful Commands Cheat Sheet
ActionCommandInstall Homebrew (Mac)/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"Install Gitbrew install git or Git for Windows installerConfigure Git Usernamegit config --global user.name "Your Name"Configure Git Emailgit config --global user.email "you@example.com"Clone Repositorygit clone <repo-url>Create Virtual Environmentpython3 -m venv venvActivate Virtual Environmentsource venv/bin/activate / venv\Scripts\activate.batInstall Python Packagespip install -r requirements.txtBuild Docker Imagedocker build -t <image-name> .Run Docker Containerdocker run -p 8000:8000 <image-name>Push Code to GitHubgit add . && git commit -m "message" && git push

📋 Notes

Install Homebrew first on Mac.
Install and configure Git and SSH before cloning.
Use Python 3.10+ and virtual environments for Python projects.
Docker is optional but recommended for consistent environments.


📎 Quick Links

Homebrew
Git Downloads
Python Downloads
Docker Desktop
GitHub SSH Setup Guide


👤 Author
Krupa Adulobo
GitHub: @kdulobo12
Docker Hub: kdulobo12

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.