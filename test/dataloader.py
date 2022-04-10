import os
import h5py

from spec.center.crust.data.constants import Constants
# from spec.center.core.obs.sky import StellarSky

ROOT     = os.environ["ROOT"]
TEST     = os.environ["TEST"]
PREPNN   = os.environ["PREPNN"]
SPECGRID = os.environ["SPECGRID"]
BOSZGRID = os.environ["BOSZGRID"]



class TestDataLoader():
    def __init__(self):
        self.bosz_res  = 5000
        self.box_name  = "R"
        self.BOSZ_PATH = os.path.join(BOSZGRID, f"bosz_{self.bosz_res}_{self.box_name}HB.h5")
        self.SPEC_PATH = os.path.join(TEST, "./testdata/spec.h5")
        self.WSKY_PATH = os.path.join(TEST, "./testdata/wavesky.npy")
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
        self.PARAM = {"OBJECTPATH": self.BOSZ_PATH, "bosz_res": self.bosz_res, "arm": self.arm, \
            "ResTune": "Alex", "step": 10, "WSKYPATH": self.WSKY_PATH, "wavesky": self.wavesky}
    
    def load_spec(self) -> dict:
        DArgvals = {}
        with h5py.File(self.SPEC_PATH, 'r') as f:
            for arg in f.keys():
                DArgvals[arg] = f[arg][()] 
        return DArgvals

