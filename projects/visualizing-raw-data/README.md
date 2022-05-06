[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Visualizing Raw Data

## Key Investigators

Josh Siegle (Allen Institute)

## Project Description

A crucial (but often ignored) step in the spike sorting process is visual inspection of the raw data before and after pre-processing steps have been performed. This can be done by looking at the raw traces for individual channels, but a qualitative assessment of overall data quality is often easier to grasp by looking at the `channels x samples` matrix displayed as an image. Using standard Python plotting libraries does not allow efficient interactions with large datasets, which is one reason why this step may be skipped.

We will attempt to overcome this limitation by using [deck.gl](https://deck.gl/), a visualization framework for big datasets that works well in the browser and in Python environments (via the [pydeck](https://deckgl.readthedocs.io/en/latest/) bindings). Many of its functions assume you're looking at geospatial data, but for the most part they are general enough to be adapted for ephys. Other frameworks may work as well, but [deck.gl](https://deck.gl/) seems the best for getting up and running quickly.

## Objectives

<!-- Briefly describe the objectives of your project. What would you like to achive?-->

1. Create an interactive visualization of high-channel-count raw + preprocessed data that can run in a browser or a Jupyter notebook
2. Overlay sorting results on top of the original data
3. Integrate with existing tools, such as [SpikeInterface](https://github.com/SpikeInterface/spikeinterface) and [sortingview](https://github.com/magland/sortingview)

## Approach and Plan

<!-- 1. Describe the steps of your planned approach to reach the objectives.-->
1. Talk with other hackathon attendees to determine whether there are any unforeseen limitations of [deck.gl](https://deck.gl/) that make it unsuitable for this application.
2. Select a visualization framework ([deck.gl](https://deck.gl/) or an alternative)
3. Create an interactive visualization of raw data. This will likely require an intermediate step in which the data is saved as an image pyramid or other multi-scale format.
4. Create an interactive visualization of spike sorting results, with spikes distributed in space and time.
5. Combine the outputs of 3 + 4 into one visualization.
6. Add raw data plotting functions to SpikeInterface and (time permitting) sortingview.

## Progress and Next Steps

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

[deck.gl TileLayer example](https://deck.gl/examples/tile-layer-non-geospatial/) - useful for displaying raw data
[pydeck ScatterplotLayer example](https://pydeck.gl/gallery/scatterplot_layer.html) - useful for displaying sorting results
