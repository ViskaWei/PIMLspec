import logging
import numpy as np
from scipy.interpolate import interp1d
from abc import ABC, abstractmethod
from .baseobs import BaseObs

class BaseSnrMapper(ABC):
    @abstractmethod
    def create_mapper():
        pass
    @abstractmethod
    def map_to_snr():
        pass

class NoiseLevelSnrMapper(BaseSnrMapper):
    '''
    noise level to snr mapper
    '''
    def __init__(self) -> None:
        self.noise_level_grid = [10, 30, 40, 50, 100, 200, 300, 400, 500]

    def create_mapper(self, flux, sky, avg=10):
        assert flux.shape[-1] == sky.shape[0]
        var   = BaseObs.get_var(flux, sky)
        sigma = np.sqrt(var)
        SN = self.average_map_over_noise_realization(avg, flux, sigma)
        logging.info(f"snr2nl-SN: {SN}")

        f = interp1d(SN, self.noise_level_grid, fill_value=0)
        f_inv = interp1d(self.noise_level_grid, SN, fill_value=0)
        return f, f_inv

    def map_to_snr(self, flux, sigma):
        noise = BaseObs.get_noise(sigma)
        SN = []
        for noise_level in self.noise_level_grid:
            obsfluxs = flux + noise_level * noise
            sn = BaseObs.get_snr(obsfluxs, sigma, noise_level)
            SN.append(sn)
        return SN

    def average_map_over_noise_realization(self, avg, *args):
        SNS=[]
        for i in range(avg):
            SNS.append(self.map_to_snr(*args))
        SN = np.mean(SNS, axis=0)
        return SN
