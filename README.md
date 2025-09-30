# 🧪 Selenium Automation Framework – MolView  

## 📖 Overview  
This project is a **Selenium-based test automation framework** designed to validate the features and functionalities of the **MolView web application**.  
It follows the **Page Object Model (POM)** design pattern to ensure **maintainability, scalability, and readability** of test scripts.  

The framework integrates with **Pytest** for test execution and reporting, supports **data-driven testing** using Excel files, and captures **screenshots, logs, and reports** for comprehensive test analysis.   

---

## ✨ Key Features  
- 📌 **Page Object Model (POM):** Modular design for reusability and maintainability.  
- 📌 **Data-Driven Testing:** Uses Excel files for test planning and test data. 
- 📌 **Logging & Reporting:** Custom logging plus HTML-based execution reports.  
- 📌 **Failure Evidence:** Automatic screenshot capture for failed test cases.  
- 📌 **Pytest Integration:** Fixtures, parameterization.

---

## 🚀 How It Works  
1. **Page Layer (`pages/`)**  
   - Contains reusable classes representing MolView UI components (Periodic Table, Molecule Search, 3D Viewer, etc.).  

2. **Test Layer (`test_cases/`)**  
   - Implements test cases by combining POM actions and assertions.  

3. **Utilities (`utils/`)**  
   - Logger and helper functions for reporting and error handling.  

4. **Execution**  
   Run tests using **Pytest**:  
   ```bash
   pytest -v --html=reports/html/report.html --self-contained-html

----
## 📝 Reporting  
* HTML reports  
* Logs  
* Screenshots  
---

## Prerequisites

- Python 3.x installed (≥ 3.8 recommended)  
- Chrome browser installed  
- Compatible ChromeDriver (matching Chrome version)  

---



## Folder Structure


```bash
 Selenium-framewoork-MolView/
  │── Excel_files/
  │   ├── manual_test.xlsx
  │   ├── TestPlan_Automation.xlsx
  ├── pages/            # POM definitions for MolView automation
  │   ├── caffeine.py
  │   ├── clickable_buttons.py
  │   ├── periodic_table_elements.py
  │   ├── search_molecule.py
  │   ├── three_d_views.py
  │── reports/
  │   ├── html/
  │   ├── log/
  │── screenshots/
  │── test_cases/        # test cases (not expanded here)
  │── utils/
  │   ├── logger.py
  │── conftest.py
  │── requirements.txt
  │── README.md

```
## Installation

Clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/Triumphany/Selenium-framework-MolView

# Move into the project directory
cd selenium-automation-PUBCHEM

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

Execute the test suite with:

```bash
  pytest -v
  pytest -v test_cases/test_name.py --html=reports/html/name.html
```
* -v runs pytest in verbose mode
* HTML reports are stored in reports/html

