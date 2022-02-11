[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Improve template matching in SpikeInterface

## Key Investigators

Pierre Yger
Samuel Garcia
Joulien Boussard


## Project Description

## Objectives

Many spike sorters use *template matching* aka *peeler* aka *deconvolution* as a final step in 
the spike sorting pipeline. It is one of the best option to handle the spike collision issue.

There are many algorithms that can be used for that steps.

SpikeInterface already includes 3 of then:
  * tridesclous strategy
  * spyking-cicus strategy
  * cicus-omp (orthogonal matching pursuit) strategy

These 3 methods give decent results, but bencmarks are still limited.

The hackathon would be an oportunity to improve the existing strategies and port more methods for a more systematic and complete benchmark.


## Approach and Plan

Implement methods from other sorter:

 * [ ] YASS
 * [ ] Kilosort
 * [ ] HDSort

Make notebooks to report benchmarks in various conditions:
  * [ ] low/high channel count
  * [ ] stationary vs drift dataset
  * [ ] low/high spike collisions
  * [ ] low/high bursting modulation

  
## Progress and Next Steps



## Materials



## Background and References


