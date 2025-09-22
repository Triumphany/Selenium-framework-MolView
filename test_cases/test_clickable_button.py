import pytest
import os, sys
from pages.clickable import MolViewToolsPage


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# screenshot dir
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots", "tools")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.mark.usefixtures("setup")
class TestTools:
    def test_all_tools(self):
        page = MolViewToolsPage(self.driver)

        titles = [
    "Move",
    "Lasso select",
    "Paste",
    "Delete",
    "Marker",
    "Center",
    "Zoom in",
    "Zoom out",
    "Single bond",
    "Double bond",
    "R group",
    "Formal charge +1",
    "Formal charge -1",
    "Add lone pair",
    "Carbon chain",
    "Phenyl",
    "Cyclohexane",
    "Cyclopentane",
    "Cyclopropane",
    "Hydrogen",
    "Carbon",
    "Nitrogen",
    "Oxygen",
    "Phosphorus",
    "Fluorine",
    "Chlorine",
    "Bromine",
    "Iodine",
    "Periodic table"
]

        for title in titles:
            page.click_tool(title)
            self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, f"{title}.png"))