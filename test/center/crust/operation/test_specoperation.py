
import numpy as np
from test.testbase import TestBase
from spec.center.core.resolution import Resolution

from spec.center.crust.operation.specoperation import BaseSpecOperation, \
    LogSpecOperation, SplitSpecOperation, TuneSpecOperation,\
    SkySpecOperation, MapSNRSpecOperation


class TestSpecOperation(TestBase):

    def test_LogSpecOperation(self):
        flux = np.arange(1,10)
        logflux_to_check = np.log(flux)
        OP = LogSpecOperation()
        logflux = OP.perform(flux)
        self.same_array(logflux, logflux_to_check)

    def test_SkySpecOperation(self):
        OP = SkySpecOperation(self.D.wavesky)
        skyH = OP.perform(self.D.waveH)
        self.same_array(skyH, self.D.skyH)

    def test_MapSNRSpecOperation(self):
        OP = MapSNRSpecOperation()
        map_snr, map_snr_inv = OP.perform(self.D.fluxH_mid, self.D.skyH)
        self.close_array(map_snr([10,20,30]).round(),  np.array([152,  76,  46]))

    def test_SplitSpecOperation(self):
        
        OP = SplitSpecOperation(self.D.arm)
        wave = np.copy(self.D.waveF)
        wave_new = OP.perform(wave)
        self.assertIsNotNone(wave_new)

        Spec = self.get_Spec("F")
        OP.perform_on_Spec(Spec)
        self.assertIsNone(np.testing.assert_array_less(OP.rng[0], Spec.wave))
        self.assertIsNone(np.testing.assert_array_less(Spec.wave, OP.rng[1]))
        self.same_array(wave_new, self.D.waveH)
        self.assertEqual(OP.split_idxs.shape, (2,))

    def test_TuneSpecOperation(self):
        step = 10
        MODEL = {"type": "Alex", "param": {"step": 10, "res":10000}}
        OP = TuneSpecOperation(MODEL)
        wave = np.copy(self.D.waveH)
        wave_new = OP.perform(wave)
        
        self.assertIsInstance(OP.model, Resolution)
        self.same_array(wave_new, self.D.wave)

        Spec = self.get_Spec("H")
        OP.perform_on_Spec(Spec)
        self.same_array(Spec.wave, self.D.wave)


