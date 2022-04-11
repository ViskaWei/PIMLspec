from base.interface.gateway.baseprocessIF import ProcessIF

from spec.center.crust.data.basespec import StellarSpec
from spec.center.crust.process.specprocess import StellarSpecProcess

from .specloaderIF import BoszLoaderIF
from .specparamIF import StellarSpecParamIF

class StellarSpecProcessIF(ProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Loader   = BoszLoaderIF()
        self.ParamIF  = StellarSpecParamIF()

        self.Process  = StellarSpecProcess()
        self.Storer   = None

    def interact_on_Object(self, Spec: StellarSpec):
        super().interact_on_Object(Spec)
