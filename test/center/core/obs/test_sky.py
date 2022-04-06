import os
from spec.center.core.obs.sky import StellarSky
from test.testbase import TestBase


class TestSky(TestBase):
    def test_StellarSky(self):
        Sky = StellarSky(self.D.wavesky)
        skyH = Sky.rebin_sky_for_wave(self.D.waveH)
        self.same_array(skyH, self.D.skyH)

        Sky2  = StellarSky.from_path(os.path.join(os.environ["TEST"], "wavesky.npy"))
        self.same_array(Sky.wave, Sky2.wave)
        self.same_array(Sky.sky,  Sky2.sky)
        sky2H = Sky2.rebin_sky_for_wave(self.D.waveH)
        self.same_array(sky2H, self.D.skyH)
