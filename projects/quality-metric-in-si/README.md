[Back to the projects list](../../)


# Quality metrics in SpikeInterface

## Key Investigators


Alessio Buccino
Matthias Henning
Olivier Winter
Marine Chaput
Josh Siegle
Aurélien Wyngaard
Robyn Greene
Ben Dichter


## Project Description

## Objectives

Computing quality metrics from a spike sorting output is an important postprocessing steps in spike sorting pieline.
The idea is to compute a set metrics of unsupervised metrics (e.g.based on spiketrains, waveforms, PCA projections)
to be able to quantify the goodness of a sorting output without ground-truth.

The quality metrics values can then used to automatically curate sorting output to filter out "bad" units using clear and reproducible criteria.


## Approach and Plan

Efforts in this direction have been initiated at several places:

  1. [This code is use in Allen Institute.](https://github.com/AllenInstitute/ecephys_spike_sorting/tree/master/ecephys_spike_sorting/modules/quality_metrics)
     It works mainly for Kilosort outputs and Neuropixels dataset.
  2. [This code is developed by the IBL and used in the IBL pieline](https://github.com/int-brain-lab/ibllib/tree/master/brainbox/metrics)
  3. [This was a port of (1.) in spikeinterface old API.](https://github.com/SpikeInterface/spikemetrics)
     This code is not used anymore in SpikeInterface>=0.90.
  4. [This is the new implementation in SpikeInterface.](https://github.com/SpikeInterface/spikeinterface/tree/master/spikeinterface/toolkit/qualitymetrics)
     It can be used on any dataset and any sorter given the flexibility of SpikeInterface.
     The port of this module is not totaly finished and still needs to be improved.

Given the importance of these quality metrics for automatic cleaning, having a unique source-code to implement quality metrics is clearly very important for reproducible science.
These 4 repos have been developed in parallel for severals years now, and converging to common, shared codebase would have a big impact for the community.


## Progress

The various implementations of metric calculation code was compared to identify disparities.

Documentation was updated to include descriptions, formulae and references for each quality metric in SpikeInterface.
These individual metric pages include comparisons between alternative, similar metrics, as well as information regarding their implementation and example use.
Additional pages were created for metrics which are to be included in SpikeInterface in future.

The structure of the documentation website was adjusted to allow more user-friendly navigation of the site, and clearer access to relevant API.
Links were added for objects within the documentation to increase navigability of the site.

The [toy_example](https://spikeinterface.readthedocs.io/en/latest/api.html#spikeinterface.extractors.toy_example) functionality in SpikeInterface was improved to allow for generation of sorting and recording extractor objects which are based on a specified spike train.
Unit tests for each metric were created and/or improved to increase the reliability and robustness of code.

## Next steps

Further quality metrics should be incorporated into SpikeInterface and documented to include the wide variety of metrics which are appearing in recent literature.
Reliable implementation of quality metrics lays the ground work for emerging work in the field of modelling unit validity using quality metrics.

If you would like to contribute to either the code or the documentation, please consult the [Quality metrics documentation page](https://spikeinterface.readthedocs.io/en/latest/module_toolkit.html#quality-metrics-module) for clarification on the current state of implementation within SpikeInterface.

## Materials


## Background and References

