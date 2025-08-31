import pytest
from selenium import webdriver
from pages.search_molecule import MolViewPage
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots", "search")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)  # Create folder if not exists


@pytest.mark.usefixtures("setup")
class TestCaffeine:
    def test_search_caffeine_ENTERkeys(self):
        page = MolViewPage(self.driver)

        page.search_molecule_enterkey("Acetylene")
        page.open_infocard()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "ENTERkeys.png"))

        common = page.get_common_name()
        iupac = page.get_iupac_name()
        smiles = page.get_smiles()

        assert common == "Acetylene"
        assert iupac == "acetylene"
        assert smiles == "C#C"

    def test_search_caffeine_SEARCHclick(self):
        page = MolViewPage(self.driver)

        page.search_molecule_click_button("Acetylene")
        page.open_infocard()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "CLICKsearch.png"))

        common = page.get_common_name()
        iupac = page.get_iupac_name()
        smiles = page.get_smiles()

        assert common == "Acetylene"
        assert iupac == "acetylene"
        assert smiles == "C#C"

    def test_search_caffeine_ENTERkeys_smiles(self):
        page = MolViewPage(self.driver)

        page.search_molecule_enterkey("C#C")
        page.open_infocard()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "smile_search.png"))

        common = page.get_common_name()
        iupac = page.get_iupac_name()
        smiles = page.get_smiles()

        assert common == "Acetylene"
        assert iupac == "acetylene"
        assert smiles == "C#C"