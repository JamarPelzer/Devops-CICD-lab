# 🔁 DevOps CI/CD Lab with GitHub Actions & Pytest

This lab demonstrates how to set up a basic Continuous Integration (CI) pipeline using **GitHub Actions** to automatically run unit tests written with **pytest**. It's a foundational DevOps exercise meant to simulate the workflow of building, testing, and ensuring code reliability before deployment.

---

## 🛠️ What I Built

- A simple Python calculator with the following functions:
  - `add(x, y)`
  - `subtract(x, y)`
  - `multiply(x, y)`
  - `divide(x, y)`
  - `exponent(x, y)`
- Unit tests for all functions in `test_app.py` using **pytest**
- A GitHub Actions workflow that:
  - Runs on every push to the `main` branch
  - Installs Python 3.10
  - Sets up a virtual environment
  - Installs `pytest`
  - Runs tests automatically on GitHub’s CI infrastructure

---

## 🚀 Technologies Used

- **Python 3.10**
- **Pytest**
- **GitHub Actions**
- **YAML**

---

## 🧪 How to Run the Tests Locally

```bash
# Optional: Set up virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # For PowerShell
# or
source venv/bin/activate  # For Linux/Mac

# Install pytest
pip install pytest

# Run tests
pytest
```

## 🧠 What I Learned
-  How to create a Python application and write unit tests

- How to use pytest to validate code logic

- How to set up GitHub Actions workflows using YAML

- How automated testing improves development workflows

- Real-world DevOps skills: CI/CD, automation, debugging broken pipelines

## 📸 Screenshots

- **WorkFlow Completed Succesfully**  
  <img width="1920" height="917" alt="Github_actions_deploy1" src="https://github.com/user-attachments/assets/d7c812b4-5972-4365-b7f7-644a92f9820f" />

- **Running the CI pipeline** 
  <img width="1914" height="631" alt="Github_actions_deploy" src="https://github.com/user-attachments/assets/090e62f2-3c4d-45bd-8d02-f92e3b0477f1" />

- **Workflow completed successfully Locally**  
   <img width="1617" height="689" alt="Github_actions_deploy2" src="https://github.com/user-attachments/assets/4300133e-3932-411a-babc-3c652430d2f0" />

## 📂 Project Structure

```cpp
Copy
Edit
.
├── app.py
├── test_app.py
├── venv/
├── requirements.txt (optional)
└── .github/
    └── workflows/
        └── main.yml
```



# **👤 Author**
Jamar
DevOps / SRE Engineer in Training



