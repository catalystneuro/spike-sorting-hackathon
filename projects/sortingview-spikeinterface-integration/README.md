[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# SortingView SpikeInterface Integration

## Key Investigators

Jeremy Magland, Jeff Soules, Samuel Garcia, Alessio Buccino

## Project Description

Integrate SortingView capabilities with the SpikeInterface project.


## Objectives

Create and document utilities for visualizating ephys data and spike sorting results.

## Approach and Plan

- Refactor widgets to have multiple backends

- Additional code to prepare data in SI and plot it/share it in figurl

## Progress and Next Steps

- During the hackathon, the widgets have been refactored to enable multiple backends (https://github.com/SpikeInterface/spikeinterface/pull/686)

- A proof of concept widget (UnitWaveforms) has been implemented in both backends

- An additional [notebook](prepare-data-for-sv.ipynb) uses the SI module to postprocess the data from a recording and a sorting object and prepare all the plotting elements for a figurl backend (see [partial example](https://www.figurl.org/f?v=gs://figurl/spikesortingview-5&d=sha1://e41a8d64a4b968e40ce3a6f4306a7adfd6c8045c&label=Alessio%20test%20data%20fixed))

- Next, we need to finalize the implementation of the sortingview backends in SI and port the notebook code
to the main repo as an `export_figurl_report()` function.

## Materials

## Background and References

* SpikeInterface: https://github.com/SpikeInterface/spikeinterface
* SortingView: https://github.com/magland/sortingview
* Figurl: https://github.com/scratchrealm/figurl2
* Kachery-cloud: https://github.com/scratchrealm/kachery-cloud
* Figurl-tiled-image: https://github.com/scratchrealm/figurl-tiled-image

Example load and preview ephys data:
https://gist.github.com/magland/470241dee3b36d37edc852f3f0707f35
