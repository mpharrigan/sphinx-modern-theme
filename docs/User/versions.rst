.. _versions:

Hosting Multiple Doc Versions
=============================

Projects will often host multiple versions of the documentation corresponding to multiple released versions of
the software. Sphinx Modern Theme supports a drop-down to toggle between documentation versions. This requires
an external json file that records the various documentation versions. By convention,
this file is called ``versions.json``

Why Javascript
--------------

The ``versions.json`` file is loaded dynamically with javascript while the page loads. Since sphinx generates
static sites (with all the advantages of static sites), we need a way to inform old versions of the docs about
new versions as they are released (so users can toggle *from* past instances *to* future instances). You could
imagine re-rendering all docs for previous versions but this (a) is a huge pain (b) might not give you an exact
replica of what the docs used to look like (due to different sphinx versions, different build environments, etc.).
You could also imagine running a regular expression (or equivalent) over all past docs to add in new versions as they
become available. We choose to introduce a little bit of javascript to dynamically populate our drop-down.

``versions.json`` structure
---------------------------

The json file should be a list of release specifications::

    [
      {
        "url": "http://www.msmbuilder.org/3.4.0",
        "version": "3.4.0",
        "display": "3.4",
        "latest": false
      },
      {
        "url": "http://www.msmbuilder.org/3.5.0",
        "version": "3.5.0",
        "display": "3.5",
        "latest": true
      }
    ]

url
    The location of the docs at that version
version
    The full version of the docs. This needs to be javascript-sortable
display
    The actual text that is displayed. This can be a friendlier version of the version string
latest
    Set to true for the latest release. This can be used in the landing page to direct users to the
    latest released version of the docs.
