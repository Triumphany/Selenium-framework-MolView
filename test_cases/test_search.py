import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.search_molecule import MolViewPage

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")

    serv_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    driver.get("https://app.molview.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestCaffeine:
    def test_caffeine_infocard(self):
        page = MolViewPage(self.driver)

        page.search_molecule("Caffeine")
        page.open_infocard()

        common = page.get_common_name()
        iupac = page.get_iupac_name()
        smiles = page.get_smiles()

        assert common == "Caffeine", f"Expected 'Caffeine', got {common}"
        assert iupac == "1,3,7-trimethylpurine-2,6-dione", f"Unexpected IUPAC: {iupac}"
        assert smiles == "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", f"Unexpected SMILES: {smiles}"