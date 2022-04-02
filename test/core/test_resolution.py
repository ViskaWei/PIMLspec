import numpy as np
from unittest import TestCase
from spec.core.resolution import  AlexResolution, NpResolution

class TestResolution(TestCase):

    def test_AlexResolution(self):
        step = 10

        model = AlexResolution()
        self.assertTrue(model.name == "Alex")

        data1D = np.arange(1, 100) 
        self.check_tune(data1D, step, model)

        data2D = np.random.rand(2,100) * 100
        self.check_tune(data2D, step, model)
        
    def check_tune(self, data, step, model):
        data_tuned = model.tune(data, step)
        dataToCheck = np.diff(np.cumsum(data, axis=-1)[..., ::step], axis=-1) / step
        self.assertIsNone(np.testing.assert_array_equal(data_tuned, dataToCheck))


    def test_NpResolutionModel(self):
        pass