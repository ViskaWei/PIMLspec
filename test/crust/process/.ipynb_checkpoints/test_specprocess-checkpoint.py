import numpy as np
from test.testbase import TestBase
from spec.crust.process.specprocess import StellarSpecProcess

class TestSpecProcess(TestBase):
    def test_BaseProcess(self):
        pass

    def test_StellarSpecProcess(self):
        Spec = self.get_Spec("F")
        np.random.seed(922)

        Process = StellarSpecProcess()
        Process.set_process(self.D.PARAM, self.D.MODEL, self.D.DATA)
        Process.start(Spec)
        self.check_StellarSpec(Spec)
        
        







        



