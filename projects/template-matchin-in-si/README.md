[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Improve template matching in spikeinterface

## Key Investigators

Pierre Yger
Samuel Garcia
(Some people from yass team ?)


## Project Description

## Objectives

Many sorters use *template matching* aka *peeler* aka *deconvolution* as a final step in 
the spike sorting pipeline. It is one of the best option to handle the spike colision issue.

There are many algorithm that can be use for that steps.

spikeinterface already include 3 of then:
  * tridesclous strategy
  * spyking-cicus strategy
  * cicus-omp (orthogonal matching pursuit) strategy

These 3 methods give descent results but bencmark ar still no perfect.

The hackathon would be an oportunity to improve and port more method for more systematic benchmark.


## Approach and Plan

Implement methods from other sorter :

 * [ ] yass
 * [ ] kilosort
 * [ ] hdsort

Make notebook to report benchmark in various situation
  * [ ] low/high channel count
  * [ ] stationary vs drifty dataset

  
## Progress and Next Steps



## Materials



## Background and References


