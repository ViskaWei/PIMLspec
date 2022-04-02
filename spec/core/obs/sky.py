import numpy as np
from scipy.interpolate import interp1d
from abc import ABC, abstractmethod

class BaseSky(ABC):
    required_attributes = ["sky", "sky_fn"]

class StellarSky(BaseSky):
    def __init__(self, wave_sky_template) -> None:
        self.wave= wave_sky_template[0]
        self.sky = wave_sky_template[1]

        self.wave2sky_fn = self.integrate_sky()

    @classmethod
    def from_path(cls, path):
        wave_sky_template = np.load(path)
        return cls(wave_sky_template)

    def integrate_sky(self): 
        intergrated = np.cumsum(self.sky)
        wave2sky_fn = interp1d(self.wave, intergrated, fill_value=0)
        return wave2sky_fn

    def rebin_sky_for_wave(self, wave):
        assert (wave[0] > self.wave[0]) and (wave[-1] < self.wave[-1])
        integrated_sky = self.wave2sky_fn(wave)
        sky_rebinned = np.diff(integrated_sky)
        # np.diff will decrease the length of the array by 1
        sky_rebinned_same_shape = np.insert(sky_rebinned, 0, sky_rebinned[0])
        return sky_rebinned_same_shape