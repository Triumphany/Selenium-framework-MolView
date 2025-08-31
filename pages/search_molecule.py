from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MolViewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    search_input = (By.XPATH, "//input[contains(@class,'input')]")
    infocard_button = (By.XPATH, "//span[contains(@class,'_label_tfgzn_') and text()='Infocard']")
    common_name = (By.XPATH, "//div[contains(@class,'property')]//span[text()='Common name']/following-sibling::span")
    iupac_name = (By.XPATH, "//div[contains(@class,'property')]//span[text()='IUPAC name']/following-sibling::span")
    smiles = (By.XPATH, "//div[contains(@class,'property')]//span[text()='Canonical SMILES']/following-sibling::span")

    # Actions
    def search_molecule(self, name):
        search_box = self.wait.until(EC.element_to_be_clickable(self.search_input))
        search_box.clear()
        search_box.send_keys(name + "\n")

    def open_infocard(self):
        button = self.wait.until(EC.element_to_be_clickable(self.infocard_button))
        button.click()

    def get_common_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.common_name)).text

    def get_iupac_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.iupac_name)).text

    def get_smiles(self):
        return self.wait.until(EC.visibility_of_element_located(self.smiles)).text