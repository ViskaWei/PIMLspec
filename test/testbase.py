import numpy as np
from unittest import TestCase
from spec.center.crust.data.basespec import StellarSpec
from test.dataloader import TestDataLoader

class TestBase(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.D = TestDataLoader()

    def get_Spec(self, t="F"):
        if t == "F":
            return StellarSpec(self.D.waveF, self.D.fluxF)
        elif t == "H":
            return StellarSpec(self.D.waveH, self.D.fluxH_mid)

    def same_array(self, a, b):
        return self.assertIsNone(np.testing.assert_array_equal(a, b))
        
    def close_array(self, a, b, tol=1e-3):
        return self.assertIsNone(np.testing.assert_allclose(a, b, atol=tol))

    def check_StellarSpec(self, Spec: StellarSpec):
        check_list = ['flux','logflux', 'num_pixel','num_spec', 'res', 'sky', 'skyH', 'step', 'wave']
        for key in check_list:
            self.same_array(getattr(self.D, key), getattr(Spec, key))

        #MapSNR
        nl_to_check  = np.array([157., 78., 47.])
        snr_to_check = np.array([140., 93., 47.])

        self.assertIsNone(np.testing.assert_allclose(
            Spec.map_snr    ([10, 20, 30]), nl_to_check,
            atol=1))
        self.assertIsNone(np.testing.assert_allclose(
            Spec.map_snr_inv([10, 20, 30]), snr_to_check,
            atol=1))
        
        # AddPfsObsSpecOperation
        self.assertEqual(Spec.Obs.step, self.D.step)
        self.same_array(Spec.Obs.sky, self.D.sky)
        flux_mid = Spec.flux[self.D.midx]
        self.same_array(Spec.Obs.get_sigma(flux_mid), self.D.sigma_mid)
