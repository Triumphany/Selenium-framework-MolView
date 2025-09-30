from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from utils.logger import get_logger

class MolViewToolsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger(__class__.__name__)

    # Locators
    move_XPATH = (By.XPATH, "//div[@title='Move']")
    lasso_select_XPATH = (By.XPATH, "//div[@title='Lasso select']")
    paste_XPATH = (By.XPATH, "//div[@title='Paste']")
    delete_XPATH = (By.XPATH, "//div[@title='Delete']")
    marker_XPATH = (By.XPATH, "//div[@title='Marker']")
    center_XPATH = (By.XPATH, "//div[@title='Center']")
    zoom_in_XPATH = (By.XPATH, "//div[@title='Zoom in']")
    zoom_out_XPATH = (By.XPATH, "//div[@title='Zoom out']")
    single_bond_XPATH = (By.XPATH, "//div[@title='Single bond']")
    double_bond_XPATH = (By.XPATH, "//div[@title='Double bond']")
    R_group_XPATH = (By.XPATH, "//div[@title='R group']")
    formal_charge_plus1_XPATH = (By.XPATH, "//div[@title='Formal charge +1']")
    formal_charge_minus1_XPATH = (By.XPATH, "//div[@title='Formal charge -1']")
    add_lone_pair_XPATH = (By.XPATH, "//div[@title='Add lone pair']")
    carbon_chain_XPATH = (By.XPATH, "//div[@title='Carbon chain']")
    phenyl_XPATH = (By.XPATH, "//div[@title='Phenyl']")
    cyclohexane_XPATH = (By.XPATH, "//div[@title='Cyclohexane']")
    cyclopentane_XPATH = (By.XPATH, "//div[@title='Cyclopentane']")
    cyclopropane_XPATH = (By.XPATH, "//div[@title='Cyclopropane']")
    hydrogen_XPATH = (By.XPATH, "//div[@title='Hydrogen']")
    carbon_XPATH = (By.XPATH, "//div[@title='Carbon']")
    nitrogen_XPATH = (By.XPATH, "//div[@title='Nitrogen']")
    oxygen_XPATH = (By.XPATH, "//div[@title='Oxygen']")
    phosphorous_XPATH = (By.XPATH, "//div[@title='Phosphorus']")
    fluorine_XPATH = (By.XPATH, "//div[@title='Fluorine']")
    chlorine_XPATH = (By.XPATH, "//div[@title='Chlorine']")
    bromine_XPATH = (By.XPATH, "//div[@title='Bromine']")
    iodine_XPATH = (By.XPATH, "//div[@title='Iodine']")
    periodic_table_XPATH = (By.XPATH, "//div[@title='Periodic table']")

    # Generic click method
    def click_tool(self, locator):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@title='{locator}']")))
        button.click()
        return button