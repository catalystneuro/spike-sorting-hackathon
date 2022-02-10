[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Add Neuropixel Destriping tool in Spike Interface

## Key Investigators

Olivier Winter (IBL)
Kush Banga (IBL)
Mayo Faulkner (IBL)

## Project Description
We have developed a pre-processing module for Neuropixel probes that improves line noise removal over CAR.
This takes into account rephasing the channels, automatic detection of bad channels and spatial filtering.

## Objectives

Implement and distribute as part of Spike Interface.
Here the code should be straightforward, this is more about providing examples and documentation. 

## Approach and Plan
1)  Agree on the plan to move the code, alternatives are:
    -   depend on IBL packages
    -   fork: copy / paste in spike interface
    -   create and use a minimal common dependency in a separate repository that both IBL and SI would use
    -   use as part of the pykilosort sorter
2)  Write examples and move some tests over to SI. Provide an example dataset


## Progress and Next Steps

We currently have a running version in the pykilosort port of IBL, that depends on our signal processing library.
We also  have a draft white paper, that will be finished and part of the IBL methods procedure by the time we meet for the hackathon.

## Materials

-   [pykilosort IBL port](https://github.com/int-brain-lab/pykilosort)
-   [destriping white paper draft here](https://www.overleaf.com/read/nrdtftnjpcnn)
-   [Signal processing module of ibllib](https://github.com/int-brain-lab/ibllib/tree/master/ibllib/dsp)


## Background and References

