[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Dockerize spike sorters

## Key Investigators

- Ben Dichter
- Alessio Buccino
- Chuang Yu Min
- Julia Sprenger
- Vincent Prevosto

<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->

## Project Description

<!-- Add a short paragraph describing the project. -->


One of the biggest usability challenges of SpikeInterface is installing the different spike sorters. This is particularly challenging for sorters that run on MATLAB and those that have specific requirements like GPU. Creating docker containers for each sorter will make them easier to install locally and deploy remotely.

## Objectives

The goal of this project is to finalize and clean up the container images for all sorters in SpikeInterface.

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

<!-- 1. Objective A. Describe it in 1-2 sentences.-->
<!-- 1. Objective B. Describe it in 1-2 sentences.-->
<!-- 1. ...-->

## Approach and Plan

The plan is to proritize KS and PyKilosort implementations, since they are the most widely used sorters. 
If we have time, we'll move on to WaveClus first and then HDsort.
A parallel effort will involve setting up a testing suite on in github actions to test the built images on some toy
data using docker and/or singularity.

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
<!-- 1. ... -->
<!-- 1. ... -->

## Progress and Next Steps

- [ ] Dockerize KS1, KS2, and KS3 following KS3 approach (https://github.com/SpikeInterface/spikeinterface-dockerfiles/pull/21)
- [ ] Create images for missing sorters: pyKilosort, Waveclus (MATLAB) HDSort (MATLAB), YASS
- [ ] Cleanup spikeinterface-dockerfiles repo and push to all images to Docker Hub
- [ ] Test on different OS (Windows/Mac)
- [ ] Implement testing suite on spikeinterface-dockerfiles for CI
- [ ] Improve documentation on how to get docker/singularity installed


<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

- Docker files: https://github.com/SpikeInterface/spikeinterface-dockerfiles
- Official docker hub images: https://hub.docker.com/orgs/spikeinterface/repositories
- Chuang Yu Min's dev images: https://hub.docker.com/u/chyumin

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

