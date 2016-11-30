sphinx-modern-theme
===================

A modern, bootstrap-based theme for sphinx.

 - [General/Docutils Example](http://sphinx-modern-theme.s3-website-us-west-1.amazonaws.com/example-example/html/)
 - [scikit-learn Example](http://sphinx-modern-theme.s3-website-us-west-1.amazonaws.com/example-sklearn/html/stable/)
 - [MSMBuilder Example](http://sphinx-modern-theme.s3-website-us-west-1.amazonaws.com/example-msmbuilder/html/)
 

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

    cd example-example/
    make html
    cd _build/html
    python -m http.server


