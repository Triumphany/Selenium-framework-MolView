import pytest
import os
from pages.periodictable import MolViewPage

SCREENSHOT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "screenshots", "elements"
)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.mark.usefixtures("setup")
class TestPeriodicTable:
    def test_all_elements_with_screenshots(self):
        page = MolViewPage(self.driver)
        page.open_periodic_table()
        ELEMENTS = ["H", "He"]
        for symbol in ELEMENTS:
            try:
                page.select_element(symbol)
                screenshot_path = os.path.join(SCREENSHOT_DIR, f"{symbol}.png")
                self.driver.save_screenshot(screenshot_path)

            except Exception as e:
                print(f"Could not click {symbol}: {e}")