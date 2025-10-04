@echo off
echo ========================================
echo    MolView Framework - ALL INDIVIDUAL TESTS
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ========== RUNNING ALL TESTS INDIVIDUALLY ==========
echo.

echo [1/16] Running Test...
pytest tests/test_3Dview.py --html=reports/html/3Dview_report.html --self-contained-html -v

echo [2/16] Running Test...
pytest tests/test_caffeine.py --html=reports/html/caffeine_report.html --self-contained-html -v

echo [3/16] Running Test...
pytest tests/test_clickable_button.py --html=reports/html/clickable_button_report.html --self-contained-html -v

echo [4/16] Running Test...
pytest tests/test_elements_periodictable.py --html=reports/html/elements_periodictable_report.html --self-contained-html -v

echo [5/16] Running Test...
pytest tests/test_search.py --html=reports/html/search_report.html --self-contained-html -v

echo.
echo ========== ALL TESTS COMPLETED ==========
echo.
pause