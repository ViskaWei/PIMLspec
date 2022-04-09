

from .specloaderIF import WaveSkyLoaderIF
from base.interface.gateway.baseparamIF import BaseParamIF


class SpecParamIF(BaseParamIF):

    def set_param(self, step=10, bosz_res=5000, arm="RedM", ResTune="Alex", WSKY_PATH=None, wavesky=None):
        self.step = step
        self.bosz_res = bosz_res
        self.arm = arm
        self.ResTune = ResTune
        self.pfs_res = bosz_res * 2
        self.load_wavesky(wavesky, WSKY_PATH)

    def load_wavesky(self, wavesky, WSKY_PATH):
        if wavesky is None:
            self.wavesky  = WaveSkyLoaderIF(WSKY_PATH).load()
        else:
            self.wavesky  = wavesky
        self.WSKY_PATH = WSKY_PATH

    def get(self):
        OP_MODEL = {'ResTune': {'type': self.ResTune, 'param': {'step': self.step, 'res': self.pfs_res}}}

        OP_PARAM = {'arm': self.arm}

        OP_DATA  =  {'wavesky': self.wavesky, 'WSKYPATH': self.WSKY_PATH}       

        OP_OUT   =  {}
        return OP_MODEL, OP_PARAM, OP_DATA, OP_OUT