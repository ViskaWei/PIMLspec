import os
from abc import ABC, abstractmethod
from base.interface.gateway.baseloaderIF import DataLoaderIF, DictLoaderIF, ObjectLoaderIF
from spec.center.crust.data.basespec import StellarSpec

class BoszLoaderIF(ObjectLoaderIF):
    """ class for loading Spec. """
    def set_param(self, PARAM):
        self.loader = DictLoaderIF(PARAM["OBJECTPATH"])

    def load(self):
        flux = self.loader.load_arg("flux")
        wave = self.loader.load_arg("wave")
        return StellarSpec(wave, flux)

class SkyLoaderIF(DictLoaderIF):
    def load(self, arm, bosz_res):
        name = f"{arm}_R{bosz_res}" #RedM_R5000
        sky = self.load_arg(name)
        return sky

class WaveSkyLoaderIF(DataLoaderIF):
    def load(self):
        return super().load()