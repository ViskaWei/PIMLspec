import numpy as np
from base.center.crust.baseoperation import BaseOperation

from spec.center.core.obs.baseobs import Obs
from spec.center.core.obs.sky import StellarSky
from spec.center.core.obs.snrmapper import NoiseLevelSnrMapper

class ObsOperation(BaseOperation):
    def perform(self, sky, step):
        if (step is None) or (step < 1): step = 1
        return Obs(sky, step=step) 

class LogOperation(BaseOperation):
    def perform(self, flux):
        return np.log(flux)

class SkyOperation(StellarSky, BaseOperation):
    def perform(self, wave):
        return self.rebin_sky_for_wave(wave)

class MapSNROperation(BaseOperation):
    '''    perform after sky is simulated with SimulateSkySpecOperation  '''
    def __init__(self) -> None:
        self.mapper = NoiseLevelSnrMapper()
    
    def perform(self, flux, sky):
        map, map_inv = self.mapper.create_mapper(flux, sky)
        return map, map_inv
    