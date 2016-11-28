sphinx-modern-theme
===================

A modern, bootstrap-based theme for sphinx.


Building
---------

    gem install sass
    npm install
    grunt sass
    python setup.py install

Packaging
---------

    grunt sass
    python setup.py sdist
    python setup.py bdist_wheel

Example
-------

    cd example1/
    make html
    cd _build/html
    python -m http.server


