[Back to the projects list](../../)


# Quality metrics in SpikeInterface

## Key Investigators


Alessio Buccino
Matthias Henning
Olivier Winter


## Project Description

## Objectives

Computing quality metrics from a spike sorting output is an important postprocessing steps in spike sorting pieline.
The idea is to compute a set metrics of unsupervised metrics (e.g.based on spiketrains, waveforms, PCA projections)
to be able to quantify the goodness of a sorting output without ground-truth.

The quality metrics values can then used to automatically curate sorting output to filter out "bad" units using clear and reproducible criteria.


## Approach and Plan

Efforts in this direction have been initiated at several place:

  1. https://github.com/AllenInstitute/ecephys_spike_sorting/tree/master/ecephys_spike_sorting/modules/quality_metrics
     This code is use in Allen Institute.
     It works mainly for Kilosort outputs and Neuropixels dataset.
  2. https://github.com/int-brain-lab/ibllib/tree/master/brainbox/metrics
     This code is developed by the IBL and used in the IBL pieline
  3. https://github.com/SpikeInterface/spikemetrics
     This was a port of (1.) in spikeinterface old API.
     This code is not used anymore in SpikeInterface>=0.90.
  4. https://github.com/SpikeInterface/spikeinterface/tree/master/spikeinterface/toolkit/qualitymetrics
     This is the new implementation in SpikeInterface.
     It can be used on any dataset and any sorter given the flexibility of SpikeInterface.
     The port of this module is not totaly finished and still needs to be improved.

Given the importance of these quality metrics for automatic cleaning, having a unique source-code to implement quality metrics is clearly very important for reproducible science.
These 4 repos have been developed in parallel for severals years now, and converging to common, shared codebase would have a big impact for the community.


## Progress and Next Steps


[Go to the live HTML site](https://catalystneuro.github.io/spike-sorting-hackathon/)

[Isolation distance](https://github.com/scratchrealm/spike-sorting-hackathon/blob/metrics/projects/quality-metric-in-si/isolation_distance)

## Materials


## Background and References

