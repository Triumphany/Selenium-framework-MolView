from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MolViewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators
    view_button_XPATH = (By.XPATH, "//div[text()='View']")
    infocard_button_XPATH = (By.XPATH, "//span[contains(@class, '_label_tfgzn_') and text()='Infocard']")
    common_name_XPATH = (By.XPATH, "//table[contains(@class,'_table_e5tmm_')]/tbody/tr[4]/td[2]")
    iupac_name_XPATH = (By.XPATH, "//table[contains(@class,'_table_e5tmm_')]/tbody/tr[5]/td[2]")
    canonical_smiles_XPATH = (By.XPATH, "//table[contains(@class,'_table_e5tmm_')]/tbody/tr[6]/td[2]")
    popup_button_XPATH = (By.XPATH, "//dialog[@open]//button")

    # Actions
    def popup(self):
        popup_button = self.wait.until(EC.element_to_be_clickable(self.popup_button_XPATH))
        popup_button.click()

    def click_view(self):
        view_button = self.wait.until(EC.element_to_be_clickable(self.view_button_XPATH))
        view_button.click()

    def open_infocard(self):
        button = self.wait.until(EC.element_to_be_clickable(self.infocard_button_XPATH))
        button.click()

    def get_common_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.common_name_XPATH)).text

    def get_iupac_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.iupac_name_XPATH)).text

    def get_smiles(self):
        return self.wait.until(EC.visibility_of_element_located(self.canonical_smiles_XPATH)).text