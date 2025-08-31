import pytest
import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.clickable import MolViewToolsPage

# add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# screenshot dir
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots", "tools")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


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
class TestTools:
    def test_all_tools(self):
        page = MolViewToolsPage(self.driver)

        tools = {
            "move": page.move_XPATH,
            "lasso_select": page.lasso_select_XPATH,
            "paste": page.paste_XPATH,
            "delete": page.delete_XPATH,
            "marker": page.marker_XPATH,
            "center": page.center_XPATH,
            "zoom_in": page.zoom_in_XPATH,
            "zoom_out": page.zoom_out_XPATH,
            "single_bond": page.single_bond_XPATH,
            "double_bond": page.double_bond_XPATH,
            "R_group": page.R_group_XPATH,
            "formal_charge_plus1": page.formal_charge_plus1_XPATH,
            "formal_charge_minus1": page.formal_charge_minus1_XPATH,
            "add_lone_pair": page.add_lone_pair_XPATH,
            "carbon_chain": page.carbon_chain_XPATH,
            "phenyl": page.phenyl_XPATH,
            "cyclohexane": page.cyclohexane_XPATH,
            "cyclopentane": page.cyclopentane_XPATH,
            "cyclopropane": page.cyclopropane_XPATH,
            "hydrogen": page.hydrogen_XPATH,
            "carbon": page.carbon_XPATH,
            "nitrogen": page.nitrogen_XPATH,
            "oxygen": page.oxygen_XPATH,
            "phosphorous": page.phosphorous_XPATH,
            "fluorine": page.fluorine_XPATH,
            "chlorine": page.chlorine_XPATH,
            "bromine": page.bromine_XPATH,
            "iodine": page.iodine_XPATH,
            "periodic_table": page.periodic_table_XPATH,
        }

        for tool_name, locator in tools.items():
            page.click_tool(locator)
            self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, f"{tool_name}.png"))