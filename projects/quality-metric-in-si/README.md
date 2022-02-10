[Back to the projects list](../../)


# Quality metric in spikeinterface

## Key Investigators


Alessio Buccino
Matthias Henning
Olivier Winter


## Project Description

## Objectives

Quality metrics on a sorter output is a postprocessing steps in spiek sorting pieline.
The idea is to compute unit per unit some metrics based on spiketrain/waveform/ISI/...

The metrics list is then use to clean the sorting output and reduce the unit with clear criteria.


## Approach and Plan

Effort for this have been initiate at several place:

  1. https://github.com/AllenInstitute/ecephys_spike_sorting/tree/master/ecephys_spike_sorting/modules/quality_metrics
     This code is use in Aleen institute.
     It works mainly for kilosort output and neuropixel dataset.
  2. https://github.com/int-brain-lab/ibllib/tree/master/brainbox/metrics
     This code is develop by the IBL and used in the ibl pieline
  3. https://github.com/SpikeInterface/spikemetrics
     This was a port of (1.) in spikeinterface old API.
     This code is not used anymore.
  4. https://github.com/SpikeInterface/spikeinterface/tree/master/spikeinterface/toolkit/qualitymetrics
     This is the new code in spikeinterface.
     It can be used on any dataset and any sorter given the flexibility of spikeinterface.
     The port of this module was not totaly finish and still need to be improved.

Given the importance of theses metrics for automatic cleaning having a unique place to implement quality metrics is
clearly very important for reproducible science.
Theses 4 repo have been develop in parralel for severals years now, convergence of code would have a big impaact for the community.


## Progress and Next Steps


## Materials


## Background and References

