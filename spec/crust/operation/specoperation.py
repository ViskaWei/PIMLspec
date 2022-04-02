from abc import ABC, abstractmethod

from base.crust.baseoperation import BaseOperation, BaseModelOperation, SplitOperation 

from ..data.constants import Constants
from ..data.spec import BaseSpec, StellarSpec
from ..model.specmodel import BaseSpecModel, AlexResolutionSpecModel, NpResolutionSpecModel
from .baseoperation import BaseOperation, ObsOperation,\
    LogOperation, SkyOperation, MapSNROperation


class BaseSpecOperation(BaseOperation):
    @abstractmethod
    def perform_on_Spec(self, Spec: StellarSpec):
        pass

class LogSpecOperation(LogOperation, BaseSpecOperation):
    def perform_on_Spec(self, Spec: StellarSpec):
        Spec.logflux = self.perform(Spec.flux) 

class SkySpecOperation(SkyOperation, BaseSpecOperation):
    def perform_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        Spec.sky = self.perform(Spec.wave)

class SplitSpecOperation(SplitOperation, BaseSpecOperation):
    def __init__(self, arm):
        self.arm = arm
        wave_rng = Constants.ARM_RNGS[arm]
        super().__init__(wave_rng)

    def perform_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        Spec.arm = self.arm
        Spec.wave = self.perform(Spec.wave)
        Spec.flux = self.split(Spec.flux, self.split_idxs)
        if Spec.sky is not None:
            Spec.sky = self.split(Spec.sky, self.split_idxs)

class MapSNRSpecOperation(MapSNROperation, BaseSpecOperation):
    def perform_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        Spec.map_snr, Spec.map_snr_inv = self.perform(Spec.flux, Spec.sky)

class TuneSpecOperation(BaseModelOperation, BaseSpecOperation):
    """ class for resolution tunable dataIF i.e flux, wave. """
    def set_model(self, model_type) -> BaseSpecModel:
        if model_type == "Alex":
            model = AlexResolutionSpecModel()
        elif model_type == "Np":
            model = NpResolutionSpecModel()
        else:
            raise ValueError("Unknown Resolution model type: {}".format(model_type))
        return model

    def perform(self, data):
        return self.model.apply(data)
    
    def perform_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        self.model.apply_on_Spec(Spec)
    
class AddPfsObsSpecOperation(ObsOperation, BaseSpecOperation):
    def perform_on_Spec(self, Spec: StellarSpec) -> StellarSpec:
        Spec.Obs = self.perform(Spec.sky, Spec.step)