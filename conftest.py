# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.threeview import MolViewPage

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")

    serv_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    driver.get("https://app.molview.com/")
    driver.maximize_window()

    page = MolViewPage(driver)
    try:
        page.popup()
    except:
        print("No popup found")

    request.cls.driver = driver
    yield
    driver.quit()