# Jenkins CI/CD Pipeline with GitHub Integration

A complete CI/CD demonstration integrating an HTML form with GitHub and a Jenkins Pipeline for automated validation testing.

---

## 📋 Project Overview

- **HTML Form**: Contains required fields: **Name**, **Email**, **Contact Number**, and **Submit**.
- **Automated Tests**: Comprehensive Python test suite (`test_form.py`) verifying the presence and attributes of the form and inputs.
- **Jenkins Pipeline (`Jenkinsfile`)**: Declarative pipeline that clones/fetches the source code from GitHub, validates the environment, executes automated tests, and archives artifacts.

---

## 📁 Repository Structure

```
├── index.html       # Responsive registration form with required fields
├── style.css        # Modern UI design system (glassmorphism & gradients)
├── script.js       # Client-side input validation and interactive feedback
├── test_form.py     # Automated unittest suite validating form components
├── Jenkinsfile      # Jenkins Declarative Pipeline definition
└── README.md        # Documentation and verification guide
```

---

## 🧪 Automated Testing

The automated test suite in `test_form.py` verifies:
1. `test_01_html_file_exists`: Verifies `index.html` exists.
2. `test_02_form_element_exists`: Verifies the presence of `<form>`.
3. `test_03_name_field_exists`: Verifies the presence of the `Name` field (`type="text"`).
4. `test_04_email_field_exists`: Verifies the presence of the `Email` field (`type="email"`).
5. `test_05_contact_number_field_exists`: Verifies the presence of the `Contact Number` field (`type="tel"`).
6. `test_06_submit_button_exists`: Verifies the presence of the Submit button (`<button type="submit">`).

### Running Tests Locally:
```bash
python test_form.py
```

---

## 🚀 Jenkins Pipeline Stages

1. **Fetch Source Code from GitHub**: Clones the repository from `https://github.com/amansingh-develops/Jenkins-TestDemo.git`.
2. **Environment & Workspace Verification**: Checks Python runtime and verifies file presence.
3. **Automated Tests - Form Validation**: Executes `python test_form.py` and reports results.
4. **Archive Build Artifacts**: Archives the tested HTML and assets.
5. **Post-Build Actions**: Outputs status and test verdict.
