from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MolViewPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)

    #Locators
    caffeine_name_XPATH = (By.XPATH, "//table[contains(@class,'_table_e5tmm_')]/tbody/tr[4]/td[2]")
    ball_stick_button_XPATH = (By.XPATH, "//div[@title='Ball and stick']")
    ball_stick_select_XPATH = (By.XPATH, "//span[contains(@class,'_label_tfgzn_') and text()='Ball and stick']")
    resonance_select_XPATH = (By.XPATH, "//span[contains(@class,'_label_tfgzn_') and text()='Resonance']")
    licorice_button_XPATH = (By.XPATH, "//div[@title='Licorice']")
    spacefill_button_XPATH = (By.XPATH, "//div[@title='Spacefill']")
    popup_button_XPATH = (By.XPATH, "//dialog[@open]//button")

    # Actions
    def popup(self):
        popup_button = self.wait.until(EC.element_to_be_clickable(self.popup_button_XPATH))
        popup_button.click()

    def caffeine_visible(self):
        caffeine_name = self.wait.until(EC.text_to_be_present_in_element(self.caffeine_name_XPATH, "Caffeine"))

    def ball_stick(self):
        ball_stick_button = self.wait.until(EC.element_to_be_clickable(self.ball_stick_button_XPATH))
        ball_stick_button.click()
        ball_stick_select = self.wait.until(EC.element_to_be_clickable(self.ball_stick_select_XPATH))
        ball_stick_select.click()

    def resonance(self):
        ball_stick_button = self.wait.until(EC.element_to_be_clickable(self.ball_stick_button_XPATH))
        ball_stick_button.click()
        resonance_select = self.wait.until(EC.element_to_be_clickable(self.resonance_select_XPATH))
        resonance_select.click()

    def licorice(self):
        licorice_button = self.wait.until(EC.element_to_be_clickable(self.licorice_button_XPATH))
        licorice_button.click()

    def spacefill(self):
        spacefill_button = self.wait.until(EC.element_to_be_clickable(self.spacefill_button_XPATH))
        spacefill_button.click()
