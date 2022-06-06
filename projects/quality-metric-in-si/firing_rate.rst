Firing rate
===========



Calculation
-----------

Firing rate is simply the average number of spikes within the recording per second.

.. math::
    \textrm{firing rate} = \frac{N_s}{T_r}

- :math:`T_r` : duration of recording in seconds (:code:`total_duration` in spikeInterface).
- :math:`N_s` : number of spikes observed in full recording (:code:`n` in spikeInterface).

Expectation and use
-------------------

Both very high and very low values of firing rate can indicate errors.
Highly contaminated units (type I error) may have high firing rates as a result of inclusion of other neurons' spikes.
Low firing rate units are likely to be incomplete (type II error), although this is not always the case (some neurons have highly selective firing patterns).
The firing rate is expected to be approximately log-normally distributed [Buzsáki]_.

Literature
----------

Unknown origin.
Widely discussed eg: Buzsáki_.

Citations
---------

.. [Buzsáki] Buzsáki, György, and Kenji Mizuseki. “The Log-Dynamic Brain: How Skewed Distributions Affect Network Operations.” Nature reviews. Neuroscience 15.4 (2014): 264–278. Web.