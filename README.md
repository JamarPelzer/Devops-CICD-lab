# Devops-CICD-lab

# DevOps CI/CD Lab with GitHub Actions & Pytest

This lab demonstrates how to set up a simple Continuous Integration (CI) pipeline using **GitHub Actions** to run automated tests with **pytest** on a Python application.

## 🔧 What I Built

- A basic Python function (`add`) inside `app.py`
- A test file (`test_app.py`) with unit tests using `pytest`
- A GitHub Actions workflow (`main.yml`) that:
  - Runs on every push to the `main` branch
  - Sets up a Python environment
  - Installs `pytest`
  - Runs all tests automatically

## 💡 What I Learned

- How to create and configure GitHub Actions workflows using YAML
- How to write and run unit tests with `pytest`
- How CI/CD pipelines detect errors before code is deployed
- How to troubleshoot and fix broken pipelines
- How to simulate real DevOps/SRE responsibilities in a practical way

## 🧪 How to Run the Tests Locally

```bash
pip install pytest
pytest
