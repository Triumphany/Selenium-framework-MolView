# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")

    serv_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    driver.get("https://app.molview.com/")
    driver.maximize_window()

    # handle popup if present
    try:
        popup_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//dialog[@open]//button"))
        )
        popup_button.click()
        print("Popup closed")
    except TimeoutException:
        print("No popup found")

    request.cls.driver = driver
    yield
    driver.quit()