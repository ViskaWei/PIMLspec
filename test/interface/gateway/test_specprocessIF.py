from test.testbase import TestBase
from spec.interface.gateway.specprocessIF import StellarSpecProcessIF

class TestBaseSpecProcessIF(TestBase):
        
    def test_BaseSpecProcessIF(self):
        pass

    def test_StellarSpecProcessIF(self):
        
        PIF = StellarSpecProcessIF()
        PIF.interact(self.D.PARAM)
        self.check_StellarSpec(PIF.Object)

        # self.assertIsNotNone(PIF.OP_OUT.keys())




    

