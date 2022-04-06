import os
import numpy as np
from unittest import TestCase

from spec.interface.gateway.specloaderIF import BoszLoaderIF,\
    SkyLoaderIF, WaveSkyLoaderIF

BOSZ_PATH = os.path.join(os.environ["TEST"], "./testdata/test.h5")
SPEC_PATH = os.path.join(os.environ["TEST"], "./testdata/spec.h5")
SKY_PATH  = os.path.join(os.environ["TEST"], "./testdata/sky.h5")
WSKY_PATH = os.path.join(os.environ["TEST"], "./testdata/wavesky.npy")

class TestSpecLoader(TestCase):

    def test_BoszLoaderIF(self):
        loaderIF = BoszLoaderIF()
        PARAM = {"BOSZ_PATH": BOSZ_PATH}
        loaderIF.set_param(PARAM)
        spec = loaderIF.load()

        self.assertIsNotNone(spec.wave)
        self.assertEqual(spec.wave.shape, (1178,))

        self.assertIsNotNone(spec.flux)
        self.assertEqual(spec.flux.shape, (120, 1178))

    def test_SkyLoaderIF(self):
        sky = SkyLoaderIF(SKY_PATH).load("RedM", "1000")
        self.assertTrue(sky.shape == (220,))

    def test_WaveSkyLoaderIF(self):
        sky = WaveSkyLoaderIF(WSKY_PATH).load()
        sky_to_check = np.load(WSKY_PATH)
        self.assertIsNone(np.testing.assert_array_equal(sky, sky_to_check))

