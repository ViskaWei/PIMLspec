import numpy as np
from unittest import TestCase
from spec.center.core.obs.snrmapper import NoiseLevelSnrMapper

class TestSnrMapper(TestCase):
    def test_NoiseLevelSnrMapper(self):
        mapper = NoiseLevelSnrMapper()
        flux = np.arange(10) + 10
        sky = np.arange(10) +1
        # map_snr, map_snr_inv = OP.perform(self.D.fluxH_mid, self.D.skyH)
        map_snr, map_snr_inv = mapper.create_mapper(flux, sky)
        self.assertIsNotNone(map_snr_inv([20,50,100]))
        # self.assertIsNone(np.testing.assert_allclose(map_snr_inv([10,20,30]).round(),  np.array([152,  76,  46])))
        
        # self.assertIsNone(np.testing.assert_allclose(map_snr([10,20,30]).round(),  np.array([152,  76,  46])))
        #FIXME better example