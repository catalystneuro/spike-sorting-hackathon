[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Deep Learning spike sorting steps into SpkeInterface

## Key Investigators

- Alessio Buccino
- Samuel Garcia
- Liam Paninski
<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->

## Project Description

Deep learning (DL) has tackled several complex applications and recently several attempts have been made to use DL 
methods for spike sorting.

Specifically, DL looks promising for signal denoising, spike detection, waveform denoising, and feature extraction.

Some major issues that we would like to solve with this project are to i) reduce/avoid computational time required for 
training and ii) generalize solutions across different probe designs/configurations


## Objectives

Incorporate the following DL methods into SpikeInterface
* [ ] DeepInterpolation (from [1][1])
* [ ] spike detection (from [2][2])
* [ ] waveform denoising (from [2][2])
* [ ] autoencoder-based feature extraction

A second major goal is to create a shared repo (e.g. on the [GIN platform](https://gin.g-node.org/)) for pre-trained 
network for different steps, probes, and configurations:
* [ ] Setup GIN repo with some pre-trained DL networks (e.g. DeepInterpolation for NP1.0)
* [ ] Implement in SpikeInterface methods to search and download a pre-trained network


## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

See the following articles for more information:

1. "Removing independent noise in systems neuroscience data using DeepInterpolation" (https://www.nature.com/articles/s41592-021-01285-2)
2. "YASS: Yet Another Spike Sorter applied to large-scale multi-electrode array recordings in primate retina" (https://www.biorxiv.org/content/10.1101/2020.03.18.997924v1.abstract)

[1]: https://www.nature.com/articles/s41592-021-01285-2 "Removing independent noise in systems neuroscience data using DeepInterpolation"
[2]: https://www.biorxiv.org/content/10.1101/2020.03.18.997924v1.abstract "YASS: Yet Another Spike Sorter applied to large-scale multi-electrode array recordings in primate retina"


<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

