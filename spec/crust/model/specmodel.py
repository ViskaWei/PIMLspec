import numpy as np
from abc import ABC, abstractmethod
from base.crust.basemodel import BaseModel

from spec.core.resolution import AlexResolution, NpResolution
from ..data.spec import StellarSpec

class BaseSpecModel(BaseModel):
    @property
    @abstractmethod
    def name(self):
        return "BaseSpecModel"
    
    @abstractmethod
    def apply_on_Spec(self, Spec):
        pass
    #basemodel
    def apply(self, data):
        pass
    def set_model_param(self, param):
        pass

class AlexResolutionSpecModel(AlexResolution, BaseSpecModel):
    def set_model_param(self, PARAM):
        self.step = PARAM["step"]
        if "res" in PARAM:
            self.res = int(PARAM["res"] / self.step)

    def apply(self, data):
        return self.tune(data, self.step)

    def apply_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        Spec.wave = self.apply(Spec.wave)
        Spec.flux = self.apply(Spec.flux)
        Spec.step = self.step
        Spec.res  = self.res

        if hasattr(Spec, "sky"):
            Spec.skyH = Spec.sky
            Spec.sky = self.apply(Spec.sky)

class NpResolutionSpecModel(NpResolution, BaseSpecModel):
    def set_model_param(self, param):
        self.wave = param["wave"]
        self.wref = param["wref"]
        self.res_in = param["res_in"]
        self.res_out = param["res_out"]
    def apply(self):
        pass
    def apply_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        pass