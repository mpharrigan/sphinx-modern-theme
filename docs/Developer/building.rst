Building
========

Pre-requisites
--------------

Sphinx Modern Theme uses the following technologies

sass
    Compiles to CSS. Used by bootstrap. Makes it easy to apply bootstrap classes to docutils classes.
    See ``scss/bootstrap.scss`` for the styles.
bootstrap
    Web theme/framework on which this is based. Obtained through npm
node and npm
    Used to fetch bootstrap and run the build system, grunt
grunt
    Fetched by npm. Used to manage compiling the sass styles
ruby
    sass runs under ruby.
python
    Sphinx runs under python. We compile our templates and styles into a python package for
    distribution.


Getting it all
--------------

Assuming you have working Python, Node, and Ruby intallations, you can fetch the dependencies and build
the package with::

    gem install sass
    npm install
    grunt sass
    python setup.py install
