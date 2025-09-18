import pytest
import os
from pages.periodictable import MolViewPage
from utils.logger import get_logger  

# Define screenshot folder
SCREENSHOT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "screenshots", "elements"
)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.mark.usefixtures("setup")
class TestPeriodicTable:
    def test_all_elements_with_screenshots(self):
        page = MolViewPage(self.driver)
        self.logger = get_logger(__class__.__name__)
        try:
            page.open_periodic_table()
            ELEMENTS = [
                "H", "He",
                "Li", "Be", "B", "C", "N", "O", "F", "Ne",
                "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
                "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
                "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
                "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
                "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
                "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
            ]

            for element in ELEMENTS:
                page.select_element(element)
                screenshot_path = os.path.join(SCREENSHOT_DIR, f"{element}.png")
                self.driver.save_screenshot(screenshot_path)
                page.open_periodic_table()

        except Exception as e:
            self.logger.error(f"Could not click {element}: {e}", exc_info=True)
            raise