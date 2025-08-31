from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MolViewPage:
    # Full periodic table symbols (IUPAC 2023, up to Oganesson)
    ELEMENTS = [
        "H", "He",
        "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
        "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr",
        "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
        "In", "Sn", "Sb", "Te", "I", "Xe",
        "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb",
        "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
        "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
        "Tl", "Pb", "Bi", "Po", "At", "Rn",
        "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
        "Es", "Fm", "Md", "No", "Lr",
        "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
        "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ]

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

    def select_element(self, symbol: str):
        """
        Clicks on an element in the periodic table by its chemical symbol.
        Example: page.select_element("H"), page.select_element("O")
        """
        element_xpath = (
            By.XPATH,
            f"//span[contains(@class, '_symbol_19stg_') and text()='{symbol}']"
        )
        element = self.wait.until(EC.element_to_be_clickable(element_xpath))
        element.click()

