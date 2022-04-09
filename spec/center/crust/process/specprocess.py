
from base.center.crust.baseprocess import BaseProcess
from ..data.basespec import BaseSpec, StellarSpec

from ..operation.specoperation import BaseSpecOperation,\
    SplitSpecOperation, TuneSpecOperation, SkySpecOperation,\
    LogSpecOperation, MapSNRSpecOperation, AddPfsObsSpecOperation


class SpecProcess(BaseProcess):
    def __init__(self) -> None:
        self.operation_list: list[BaseSpecOperation] = None
    def set_process(self, PARAM, MODEL, DATA):
        pass
    def start(self, Spec: BaseSpec):
        for operation in self.operation_list:
            operation.perform_on_Spec(Spec)


class StellarSpecProcess(SpecProcess):
    def set_process(self, PARAM, MODEL, DATA):
        self.operation_list = [
            SplitSpecOperation(PARAM["arm"]),
            SkySpecOperation(DATA["wavesky"]),
            MapSNRSpecOperation(),
            TuneSpecOperation(MODEL["ResTune"]),
            AddPfsObsSpecOperation(),
            LogSpecOperation(),
        ]
    def start(self, Spec: StellarSpec):
        super().start(Spec)