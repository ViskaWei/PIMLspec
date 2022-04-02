import os
import h5py

from spec.crust.data.constants import Constants
from spec.core.obs.sky import StellarSky

ROOT     = os.environ["ROOT"]
TEST     = os.environ["TEST"]
SPECGRID = os.environ["SPECGRID"]
PREPNN   = os.environ["PREPNN"]



class TestDataLoader():
    def __init__(self):
        self.SPEC_PATH = os.path.join(TEST, "spec.h5")
        self.WSKY_PATH = os.path.join(TEST, "wavesky.npy")
        self.arm = "RedM"
        self.midx = 1377
        self.wave_rng = Constants.ARM_RNGS[self.arm]

        self.set_spec_data()
        # (['flux', 'fluxF', 'fluxH_mid', 'logflux', 'num_pixel', 'num_spec',\
        # 'res', 'sigma_mid', 'sky', 'skyH', 'step', 'wave', 'waveF', 'waveH'])
        self.set_spec_param()

    def set_spec_data(self):
        spec_dict = self.load_spec()
        
        self.flux      = spec_dict["flux"]
        self.fluxF     = spec_dict["fluxF"]
        self.fluxH_mid = spec_dict["fluxH_mid"]
        self.logflux   = spec_dict["logflux"]
        
        self.num_pixel = spec_dict["num_pixel"]
        self.num_spec  = spec_dict["num_spec"]
        
        self.res       = spec_dict["res"]
        self.sigma_mid = spec_dict["sigma_mid"]
        self.sky       = spec_dict["sky"]
        self.skyH      = spec_dict["skyH"]
        self.step      = spec_dict["step"]
        
        self.wave      = spec_dict["wave"]
        self.waveF     = spec_dict["waveF"]
        self.waveH     = spec_dict["waveH"]
        self.wavesky   = spec_dict["wavesky"]

    def set_spec_param(self):
        self.MODEL = {
            "ResTune" : {"type": "Alex", "param": {"step": self.step, "res":10000}},
        }
        self.PARAM = {"arm": self.arm}
        self.DATA  = {"wavesky": self.wavesky}

    
    def load_spec(self) -> dict:
        DArgvals = {}
        with h5py.File(self.SPEC_PATH, 'r') as f:
            for arg in f.keys():
                DArgvals[arg] = f[arg][()] 
        return DArgvals

