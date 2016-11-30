MarkovStateModel
================

Reversible Markov State Model

This model fits a first-order Markov model to a dataset of integer-valued
timeseries. The key estimated attribute, ``transmat_`` is a matrix
containing the estimated probability of transitioning between pairs
of states in the duration specified by ``lag_time``.

Unless otherwise specified, the model is constrained to be reversible
(satisfy detailed balance), which is appropriate for equilibrium chemical
systems.::

    MarkovStateModel(lag_time=1, n_timescales=None, reversible_type='mle',
                     ergodic_cutoff='on', prior_counts=0, sliding_window=True,
                     verbose=True)

Parameters
----------

lag_time : int
    The lag time of the model
n_timescales : int
    The number of dynamical timescales to calculate when diagonalizing
    the transition matrix. If not specified, it will compute n_states - 1
reversible_type : {'mle', 'transpose', None}
    Method by which the reversibility of the transition matrix
    is enforced. 'mle' uses a maximum likelihood method that is
    solved by numerical optimization, and 'transpose'
    uses a more restrictive (but less computationally complex)
    direct symmetrization of the expected number of counts.
ergodic_cutoff : float or {'on', 'off'}
    Only the maximal strongly ergodic subgraph of the data is used to build
    an MSM. Ergodicity is determined by ensuring that each state is
    accessible from each other state via one or more paths involving edges
    with a number of observed directed counts greater than or equal to
    ``ergodic_cutoff``. By setting ``ergodic_cutoff`` to 0 or
    'off', this trimming is turned off. Setting it to 'on' sets the
    cutoff to the minimal possible count value.
prior_counts : float
    Add a number of "pseudo counts" to each entry in the counts matrix
    after ergodic trimming.  When prior_counts == 0 (default), the assigned
    transition probability between two states with no observed transitions
    will be zero, whereas when prior_counts > 0, even this unobserved
    transitions will be given nonzero probability.
sliding_window : bool
    Count transitions using a window of length ``lag_time``, which is slid
    along the sequences 1 unit at a time, yielding transitions which
    contain more data but cannot be assumed to be statistically
    independent. Otherwise, the sequences are simply subsampled at an
    interval of ``lag_time``.
verbose : bool
    Enable verbose printout

References
----------
.. [1] Prinz, Jan-Hendrik, et al. "Markov models of molecular kinetics:
   Generation and validation." J Chem. Phys. 134.17 (2011): 174105.
.. [2] Pande, V. S., K. A. Beauchamp, and G. R. Bowman. "Everything you
   wanted to know about Markov State Models but were afraid to ask"
   Methods 52.1 (2010): 99-105.

Attributes
----------
n_states_ : int
    The number of states in the model
mapping_ : dict
    Mapping between "input" labels and internal state indices used by the
    counts and transition matrix for this Markov state model. Input states
    need not necessarily be integers in (0, ..., n_states\_ - 1), for
    example. The semantics of ``mapping_[i] = j`` is that state ``i`` from
    the "input space" is represented by the index ``j`` in this MSM.
countsmat_ : array, (n_states_, n_states_)
    Number of transition counts between states. countsmat\_[i, j] is counted
    during ``fit()``. The indices `i` and `j` are the "internal" indices
    described above. No correction for reversibility is made to this
    matrix.
``transmat_`` : array, (n_states_, n_states_)
    Maximum likelihood estimate of the reversible transition matrix.
    The indices ``i`` and ``j`` are the "internal" indices described above.
populations_ : array, (n_states_,)
    The equilibrium population (stationary eigenvector) of transmat\_
