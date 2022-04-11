from .specloaderIF import WaveSkyLoaderIF
from base.interface.gateway.baseparamIF import ParamIF
from spec.center.crust.data.constants import Constants

class StellarSpecParamIF(ParamIF):
    required_attribute = ["arm", "step"]

    def set_param(self, PARAM):
        self.arm       = self.get_arg('arm', PARAM)
        self.step      = self.get_arg('step', PARAM)

        self.bosz_res  = self.get_arg('bosz_res', PARAM, 5000)
        self.ResTune   = self.get_arg('ResTune', PARAM, "Alex")
        self.wavesky   = self.get_arg('wavesky', PARAM, None)
        self.WSKY_PATH = self.get_arg('WSKY_PATH', PARAM, Constants.WSKY_PATH)
        self.BOSZ_PATH = self.get_arg('BOSZ_PATH', PARAM, Constants.BOSZ_PATH)

        self.pfs_res = self.bosz_res * 2
        self.load_wavesky()

        self.set_param_dict()
        

    def load_wavesky(self):
        if self.wavesky is None:
            self.wavesky  = WaveSkyLoaderIF(self.WSKY_PATH).load()

    def set_param_dict(self):
        self.OBJECT = {"BOSZ_PATH": self.BOSZ_PATH}

        self.MODEL = {'ResTune': {'type': self.ResTune, 'param': {'step': self.step, 'res': self.pfs_res}}}

        self.OP = {'arm': self.arm}

        self.DATA  =  {'wavesky': self.wavesky, 'WSKYPATH': self.WSKY_PATH}       