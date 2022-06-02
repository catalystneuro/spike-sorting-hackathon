from pathlib import Path
import spikeglx
"""
SET YOUR LOCAL DIRECTORY HERE
"""
ROOT_PATH = Path("/datadisk/Data/spike_sorting/benchmark/one")

cbin_files = [
    "CSH_ZAD_026/2020-09-04/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.ap.cbin",
    "CSH_ZAD_029/2020-09-09/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.ap.cbin",
    "SWC_054/2020-10-05/001/raw_ephys_data/probe01/_spikeglx_ephysData_g0_t0.imec1.ap.cbin",
    "SWC_054/2020-10-05/001/raw_ephys_data/probe00/_spikeglx_ephysData_g0_t0.imec0.ap.cbin"
]

cbin_file = ROOT_PATH.joinpath(cbin_files[0])


# Programmatic access: sr is sliceable like a conventional numpy array / memmap
sr = spikeglx.Reader(cbin_file)

# display and navigate the full file
from viewephys.gui import EphysBinViewer
EphysBinViewer(cbin_file)

