Inter-spike-interval (ISI) violations
=====================================



Calculation
-----------

Neurons have a refractory period after a spiking event during which they cannot fire again.
Inter-spike-interval (ISI) violations refers to the rate of refractory period violations Hill_.



The following quantities are required:
- :math:`ISI_t` : biological threshold for ISI violation.
- :math:`ISI_{min}`: minimum ISI threshold enforced by the data recording system used.
- :math:`ISI_s$` : the array of ISI violations which are observed in the unit's spike train.
- :math:`\#`: denote count.
The threshold for ISI violations is the biological ISI threshold, :math:`ISI_t`, minus the minimum ISI threshold, :math:`ISI_{min}` enforced by the data recording system used.
The array of inter-spike-intervals observed in the unit's spike train, :math:`ISI_s$`, is used to identify the count (:math:`\#``) of observed ISI's below this threshold.
For a recording with a duration of :math:`T_r` seconds, and a unit with :math:`N_s` spikes, the rate of ISI violations is:

.. math::

    \textrm{ISI violations} = \frac{ \#( ISI_s < ISI_t) T_r  }{ 2  N_s^2  (ISI_t - ISI_{min}) }

Expectation and use
-------------------

ISI violations identifies unit contamination - a high value indicates a highly contaminated unit.
Despite being a ratio, ISI violations can exceed 1.

Literature
----------

Introduced by [Hill]_ (2011).

.. [Hill] Hill, Daniel N., Samar B. Mehta, and David Kleinfeld. “Quality Metrics to Accompany Spike Sorting of Extracellular Signals.” The Journal of neuroscience 31.24 (2011): 8699–8705. Web.
