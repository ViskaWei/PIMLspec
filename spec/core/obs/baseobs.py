import numpy as np
from abc import ABC, abstractmethod

class BaseObs(object):
    @staticmethod
    def get_var(flux, sky):
        #--------------------------------------------
        # Get the total variance
        # BETA is the scaling for the sky
        # VREAD is the variance of the white noise
        # This variance is still scaled with an additional
        # factor when we simuate an observation.
        #--------------------------------------------
        assert flux.shape[-1] == sky.shape[0]
        BETA  = 10.0
        VREAD = 16000
        return  flux + BETA*sky + VREAD

    @staticmethod
    def get_noise(sigma):
        return np.random.normal(0, sigma, np.shape(sigma))

    @staticmethod
    def get_snr(obsfluxs, sigma, noise_level=1):
        return np.mean(np.divide(obsfluxs, noise_level*sigma))


class Obs(BaseObs):
    def __init__(self, sky, step=1) -> None:
        self.sky = sky
        self.step = step

    def get_var(self, flux):
        return BaseObs.get_var(flux, self.sky)

    def get_sigma(self, flux):
        var = self.get_var(flux)
        var /= self.step
        return np.sqrt(var)

    def get_log_sigma(self, flux, log=False):
        if log: flux = np.exp(flux)
        sigma = self.get_sigma(flux)
        return sigma / flux