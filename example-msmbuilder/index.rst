.. _msmbuilder:

MSMBuilder
==========


.. raw:: html

    <h4>
    Statistical models for Biomolecular Dynamics</h4>

MSMBuilder is an application and python library. It builds
statistical models for high-dimensional time-series. The particular focus
of the package is on the analysis of atomistic simulations of biomolecular
dynamics such as protein folding and conformational change.

To get started via `Anaconda Python <https://www.continuum.io/downloads>`_,
use::

    conda install -c omnia msmbuilder

MSMBuilder includes algorithms for constructing dynamical models:

- :ref:`featurization`
- :ref:`decomposition`
- :ref:`cluster`
- :ref:`msm`
- :ref:`hmm`
- :ref:`ratematrix`

As well as methods for analysis and validation of the models:

- :ref:`gmrq`
- :ref:`tpt`

New users should check out:

- :ref:`background`
- :ref:`installation`
- :ref:`tutorial`
- :ref:`faq`

MSMBuilder is most effective as a library. Intermediate users should
familiarize themselves with:

- :ref:`apipatterns`
- :ref:`datasets`
- :ref:`changelog`


MSMBuilder is developed by primarily by researchers at Stanford University,
and we welcome contributions. The development all takes place on `Github
<https://github.com/msmbuilder/msmbuilder>`_.  MSMBuilder is licensed under
the GNU LGPL (v2.1 or later).



.. toctree::
    :hidden:

    getting-started/index
    reference/index
    ancillary/index

.. vim: tw=75
