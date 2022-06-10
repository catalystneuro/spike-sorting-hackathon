[Back to the projects list](../../)

<!-- For information on how to write GitHub .md files see https://guides.github.com/features/mastering-markdown/ -->

# Visualizing Raw Data

## Key Investigators

Josh Siegle (Allen Institute), Jeremy Magland (Flatiron Institute)

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

## Progress

<!--Populate this section as you are making progress before/during/after the hackathon-->
<!--Describe the progress you have made on the project,e.g., which objectives you have achieved and how.-->
<!--Describe the next steps you are planing to take to complete the project.-->

### Pre-hackathon

- The [`figurl-tiled-image` repository](https://github.com/scratchrealm/figurl-tiled-image) - creates a tiled image from a `numpy` array and makes it accessible through the browser (using [kachery-cloud](https://github.com/scratchrealm/kachery-cloud) and [figurl](https://github.com/scratchrealm/figurl2)). 

- [Proof-of-concept example](https://www.figurl.org/f?v=gs://figurl/tiled-image-1&d=ipfs://bafkreid3gmolclm5pjyd27hlbhnxlxefoh3yxi4cylwsph2po25wcqfm4e&label=Neuropixels%20Example) of Neuropixels data displayed as a deck.gl `TileLayer` via [figurl](https://github.com/scratchrealm/figurl2).

### During the hackathon

- [Code](https://github.com/scratchrealm/figurl-tiled-image/blob/main/examples/multipanel_mandelbrot.py) and [example](https://www.figurl.org/f?v=gs://figurl/figurl-tiled-image-2&d=ipfs://QmYDC6aw1dD3NLyvMjzhoZgXaU7XNMRScQ8NLLGS2gacM9&label=Mandelbrot%20tiled%20image) of a multi-layer image.

- [Example](https://www.figurl.org/f?v=gs://figurl/figurl-tiled-image-2&d=ipfs://QmcksfB7uq3aoYWn2Et9XRKxWMLmu88pos61RWmeCtiHyk&label=Neuropix-PXI-100_ProbeA-AP) of Neuropixels 1.0 data displayed after three different pre-processing steps (filtering, phase shifting, and referencing).

- [Code](https://github.com/scratchrealm/figurl-tiled-image/blob/main/examples/spikeinterface_example.py) and [example] of Neuropixels 2.0 data displayed after three different pre-processing steps (centering, filtering, and referencing).

The last example demonstrates how these plotting methods can be used in practice: given a set of `SpikeInterface` recording extractors, it's now possible to generate a link to a scrollable, zoomable visualization of the raw data.

## Next steps

- The code we have written could be more tightly integrated into `SpikeInterface` by creating an alternative backend for the `plot_timeseries` function. Currently, this method displays the raw traces using `matplotlib`, but there could also be an option to export the traces as a tiled image on `figurl`.

- We have not yet tried to overlay the sorting results on top of the raw data. This is a more involved project, but one that will be useful for comparing the output of different sorters.


## Materials

<!--If available add links to the materials relevant to the project, e.g., the code generated for the project or data used-->
<!--If available add pictures and links to videos that demonstrate what has been accomplished.-->
<!--![Description of picture](Example2.jpg)-->

[Example data](https://www.dropbox.com/sh/wkkudosfb7f4m5k/AAA8rcbdo4K95JREB3cWvg_ba?dl=0) for this project. Includes raw traces for a Neuropixels 1.0 and 2.0 recording, plus Kilosort 2 sorting results.

## Background and References

<!--Use this space for information that may help people better understand your project, like links to papers, source code, or data ,e.g:-->
<!-- - Source code: https://github.com/YourUser/YourRepository -->
<!-- - Documentation: https://link.to.docs -->
<!-- - Test data: https://link.to.test.data -->

[deck.gl `TileLayer` example](https://deck.gl/examples/tile-layer-non-geospatial/) - useful for displaying raw data

[pydeck `ScatterplotLayer` example](https://pydeck.gl/gallery/scatterplot_layer.html) - useful for displaying sorting results
