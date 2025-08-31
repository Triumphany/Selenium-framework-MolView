import pytest
from pages.caffeine import MolViewPage
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.mark.usefixtures("setup")
class TestCaffeine:
    def test_caffeine_infocard(self):
        page = MolViewPage(self.driver)

        page.click_view()
        page.open_infocard()

        common = page.get_common_name()
        iupac = page.get_iupac_name()
        smiles = page.get_smiles()

        assert common == "Caffeine"
        assert iupac == "1,3,7-trimethylpurine-2,6-dione"
        assert smiles == "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"