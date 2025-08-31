from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class MolViewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    search_input_XPATH = (By.XPATH, "//input[contains(@class,'input')]")
    search_button_XPATH = (By.XPATH, "//div[contains(@class,'_wrapper_13ff3_')]/div/div/div")
    view_button_XPATH =(By.XPATH, "//div[text()='View']")
    infocard_button_XPATH = (By.XPATH, "//span[contains(@class,'_label_tfgzn_') and text()='Infocard']")
    common_name_XPATH = (By.XPATH, "//div[contains(@class,'property')]//span[text()='Common name']/following-sibling::span")
    iupac_name_XPATH = (By.XPATH, "//div[contains(@class,'property')]//span[text()='IUPAC name']/following-sibling::span")
    smiles_XPATH = (By.XPATH, "//div[contains(@class,'property')]//span[text()='Canonical SMILES']/following-sibling::span")

    # Actions
    def search_molecule_enterkey(self, name):
        search_box = self.wait.until(EC.element_to_be_clickable(self.search_input_XPATH))
        search_box.clear()
        search_box.send_keys(name + Keys.ENTER)

    def search_molecule_click_button(self, name):
        search_box = self.wait.until(EC.element_to_be_clickable(self.search_input_XPATH))
        search_box.clear()
        search_box.send_keys(name)
        search_button = self.wait.until(EC.element_to_be_clickable(self.search_button_XPATH))
        search_button.click()


    def open_infocard(self):
        view_button = self.wait.until(EC.element_to_be_clickable(self.view_button_XPATH))
        view_button.click()
        infocard_button = self.wait.until(EC.element_to_be_clickable(self.infocard_button_XPATH))
        infocard_button.click()

    def get_common_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.common_name_XPATH)).text

    def get_iupac_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.iupac_name_XPATH)).text

    def get_smiles(self):
        return self.wait.until(EC.visibility_of_element_located(self.smiles_XPATH)).text