from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MolViewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    popup_button_XPATH = (By.XPATH, "//dialog[@open]//button")
    periodic_table_button_XPATH = (By.XPATH, "//div[@title='Periodic table']")

    # Actions
    def popup(self):
        popup_button = self.wait.until(
            EC.element_to_be_clickable(self.popup_button_XPATH)
        )
        popup_button.click()

    def open_periodic_table(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.periodic_table_button_XPATH)
        )
        button.click()

    def select_element(self, symbol):
        element_xpath = (By.XPATH, f"//span[contains(@class, '_symbol_19stg_') and text()='{symbol}']")
        element = self.wait.until(EC.element_to_be_clickable(element_xpath))
        element.click()

