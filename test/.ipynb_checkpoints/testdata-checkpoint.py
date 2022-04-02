import os
import numpy as np
from spec.crust.data.constants import Constants

ROOT          = os.environ["ROOT"]
SPECGRID_PATH = os.environ["SPECGRID"]
SPECGRID_DATA_DIR  = os.path.join(ROOT, "test/testdata/testspecgriddata/")


class DataInitializer():
    def __init__(self):
        self.DATA_PATH=os.path.join(GRID_PATH, "bosz_5000_RHB.h5")
        self.set_SpecGrid_data()
        self.set_PrepNN_data()
        self.PARAMS = {
            "SpecGrid": self.SPEC_GRID_PARAMS,
            "PrepNN": self.NN_PREP_PARAMS,
        }

    def set_SpecGrid_data(self, DATA_DIR=SPECGRID_DATA_DIR):
        self.SpecGrid_TEST_PATH = DATA_DIR + "bosz_5000_test.h5"

        SGL = SpecGridLoaderIF()
        SGL.set_path(self.DATA_PATH)
        self.specGrid = SGL.load()

        self.wave =  self.specGrid.wave      #3000-14000, 15404
        self.flux =  self.specGrid.flux      #(2880, 15404)
        self.para = self.specGrid.coord      #(2880, 5)
        self.pdx  = self.specGrid.coord_idx  #(2880, 5)
        self.pdx0 = self.pdx - self.pdx[0]   #(2880, 5)
        self.midx = 1377

        SL = SpecLoaderIF()
        SL.set_path(self.DATA_PATH)
        self.spec = SL.load()

        self.SKY_PATH = DATA_DIR +"wavesky.npy"
        self.Sky  = WaveSkyLoaderIF().load(self.SKY_PATH)
        self.skyH = np.load(DATA_DIR + "skyH.npy")  #2204
        self.sky = np.load(DATA_DIR +"sky.npy")    #220
        assert(self.sky is not None)

        self.waveH_RedM = np.load(DATA_DIR +"waveH_RedM.npy")
        self.wave_RedM  = np.load(DATA_DIR +"wave_RedM.npy")
        self.fluxH_mid  = np.load(DATA_DIR +"fluxH_mid.npy") 
        self.flux_mid   = np.load(DATA_DIR + "flux_mid.npy")
        self.sigma_mid  = np.load(DATA_DIR + "sigma_mid.npy")
        self.coord_interp = np.array([-0.5,  6125,  2.5, -0.25,  0.0])
        self.coordx_interp = np.array([2., 2.5, 1., 2., 1.])

        self.logflux_interp = np.load(DATA_DIR + "logflux_interp.npy")

        self.OBJECT = {"path": self.DATA_PATH}

        self.SPECGRID_DATA = {"SKY_PATH": self.SKY_PATH, "Sky": self.Sky}

        self.arm      = "RedM"
        self.step     = 10
        self.box_name = "R"
        self.decor    = ""

        self.SPECGRID_PARAM = {
            "box_name": self.box_name,
            "arm"     : self.arm,
            "step"    : self.step,
            "wave_rng": Constants.ARM_RNGS[self.arm]
        }

        self.SPECGRID_MODEL = {
            "ResTune" : {"type": "Alex", "param": {"step": 10, "res":10000}},
            "Interp"  : {"type": "RBF"}
        }

        self.SPECGRID_OUT   = {
            "dir"   : PREPNN_DATA_DIR,
            "decor" : self.decor,
        }

        self.SPEC_GRID_PARAMS = {
            "object": self.OBJECT,
            "data"  : self.SPECGRID_DATA,
            "op"    : self.SPECGRID_PARAM,
            "model" : self.SPECGRID_MODEL,
            "out"   : self.SPECGRID_OUT
        }

    def set_PrepNN_data(self, DATA_DIR=PREPNN_DATA_DIR):
        self.ntrain = 5
        self.ntest  = 5
        self.res    = int(10000/self.step)
        self.name   = self.arm + f"_R{self.res}"
        self.decor  = "tst_"

        loader = ObjectLoaderIF()
        self.RBFinterp = loader.load(DATA_DIR + self.name + "_interp.pickle")
        self.PREPNN_OBJECT = {
            "path"  : DATA_DIR,
            "arm"   : self.arm,
            "res"   : self.res,
        }
        self.PREPNN_PARAM = {
            "step"  : self.step,
            "seed"  : 922,
            "ntrain": self.ntrain,
            "ntest" : self.ntest,
        }
        self.PREPNN_DATA = {
            "rng"   : np.array([4., 5., 3., 5., 3.]),
        }
        self.PREPNN_MODEL = {}
        self.PREPNN_OUT   = {
            "dir"   : STELLARNN_DATA_DIR,
            "decor" : self.decor,
        }

        self.NN_PREP_PARAMS = {
            "object": self.PREPNN_OBJECT,
            "data"  : self.PREPNN_DATA,
            "op"    : self.PREPNN_PARAM,
            "model" : self.PREPNN_MODEL,
            "out"   : self.PREPNN_OUT,
        }


    def set_StellarNN_data(self, DATA_DIR=STELLARNN_DATA_DIR):
        self.train_name = "RedM_R1000_N5_train.h5"
        self.test_name  = "RedM_R1000_N5_test.h5"
        self.STELLAR_NN_OBJECT = {
            "train_name"  : self.train_name,
            "test_name"   : self.test_name,
        }
