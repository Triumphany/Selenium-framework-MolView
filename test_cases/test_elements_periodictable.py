import pytest
import os
from pages.periodictable import MolViewPage

# Define screenshot folder
SCREENSHOT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "screenshots", "elements"
)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.mark.usefixtures("setup")
class TestPeriodicTable:
    def test_all_elements_with_screenshots(self):
        page = MolViewPage(self.driver)

        # Open periodic table
        page.open_periodic_table()

        # Loop through all elements
        for symbol in MolViewPage.ELEMENTS:
            try:
                page.select_element(symbol)

                # Save screenshot for each element
                screenshot_path = os.path.join(SCREENSHOT_DIR, f"{symbol}.png")
                self.driver.save_screenshot(screenshot_path)

                print(f"✅ Clicked {symbol}, screenshot saved at {screenshot_path}")

            except Exception as e:
                print(f"❌ Could not click {symbol}: {e}")