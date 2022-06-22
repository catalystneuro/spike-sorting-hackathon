[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Detection benchmark

## Key Investigators

<!-- - Investigator 1 (Affiliation)-->
<!-- - Investigator 2 (Affiliation)-->
Andrei Stefan (University of Edinburgh), Matthias Hennig (University of Edinburgh), Alessio Buccino

## Project Description

Currently, there is no reliable way of testing the accuracy of the spike detection component independently from an entire spike sorting pipeline. This renders the postprocessing benchmarking of such functions incomplete, slow and cumbersome. For example, when testing against a ground truth sorting, it is currently not possible to infer the origin of false positive clustered units -- are they misclustered true positive spikes or correctly detected, false positive spikes that yielded extra neuronal units?

To mitigate this, this project aims to evaluate the accuracy performance of a spike detection component by attempting to match its detected spikes against ground truth sorted data. It will then compute and analyse metrics such as precision and recall in order to determine the performance of the sorting component.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Create a module that can attempt the matching process between detected spikes and ground truth spikes and classify them into false positives, false negatives, true positives detections.
2. Create a function to compute and visualise metrics.
3. Test a spike detection method with different detection thresholds and analyse the change in metrics (especially recall).
4. Find a solution for spike detection methods that do not produce locally exclusive spikes.
5. Extend the module in order to work without ground truth sorted data.

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
1. Compute the peak amplitude channel for each ground truth unit based on its template.
2. For each ground truth unit, try to match its spikes with the detected ones on the peak channel.
3. If not found, search in phisical radius of channels on the probe.
4. Label the detected spikes as false positives, false negatives, true positives and compute the metrics (precision and recall).
5. Analyse the relevancy of false postitives. Mitigate non-locally exclusive spikes by detecting redundant spikes and treating them as a whole (i.e. peak detected spikes + its traces on nearby channel are assigned to 1 ground truth spike).

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
- Created a module that attempts the matching between detected spikes and ground truth units' spike trains and then classifies them in order to compute precision and recall.
- Ran experiments on spike detection algorithms with different detection thresholds and analysed the change in accuracy, precision and recall.
- Computed and analysed accuracy and SNR per unit.
- Clustered redundant detected spikes into groups before matching to ground truth spikes in order to analyse false positives.
<!--Describe the next steps you are planing to take to complete the project.-->
Next steps:
- Extend the module in order to work without ground truth sorted data.
- Use the findings to improve detection algorithms.

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

