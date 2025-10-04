@echo off
echo ========================================
echo    MolView Framework - Full Test Suite
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo Running all PubChem tests...
pytest test_cases/ --html=reports/html/full_report.html --self-contained-html -v

echo Tests completed! Check reports/full_report.html
pause