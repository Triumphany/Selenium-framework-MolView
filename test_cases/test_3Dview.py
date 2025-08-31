import pytest
from pages.threeview import MolViewPage
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots", "threeDview")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)  # Create folder if not exists


@pytest.mark.usefixtures("setup")
class TestView:
    def test_ball_stick(self):
        page = MolViewPage(self.driver)
        page.ball_stick()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "ball_stick.png"))

    def test_resonance(self):
        page = MolViewPage(self.driver)
        page.resonance()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "resonance.png"))

    def test_licorice(self):
        page = MolViewPage(self.driver)
        page.licorice()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "licorice.png"))

    def test_spacefill(self):
        page = MolViewPage(self.driver)
        page.spacefill()
        self.driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "spacefill.png"))